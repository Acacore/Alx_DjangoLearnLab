from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Author, Book



class BookAPITestCase(APITestCase):

    def setUp(self):
        """
        Set up test data and authenticated user.
        """
        self.client = APIClient()

        # Create user for authentication
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.client.force_authenticate(user=self.user)

        # Create author
        self.author = Author.objects.create(name='George Orwell')

        # Create books
        self.book1 = Book.objects.create(
            title='Animal Farm',
            publication_year=1945,
            author=self.author
        )
        self.book2 = Book.objects.create(
            title='1984',
            publication_year=1949,
            author=self.author
        )


    def test_list_books(self):
        """
        Test retrieving all books.
        """
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


    def test_create_book(self):
        """
        Test creating a new book.
        """
        data = {
            'title': 'Homage to Catalonia',
            'publication_year': 1938,
            'author': self.author.id
        }
        response = self.client.post('/books/create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.get(id=response.data['id']).title, 'Homage to Catalonia')


    def test_retrieve_book_detail(self):
        """
        Test retrieving a single book by ID.
        """
        response = self.client.get(f'/books/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Animal Farm')


    def test_update_book(self):
        """
        Test updating a book.
        """
        data = {
            'title': 'Animal Farm (Updated)',
            'publication_year': 1945,
            'author': self.author.id
        }
        response = self.client.put(f'/books/{self.book1.id}/update/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Animal Farm (Updated)')

    def test_delete_book(self):
        """
        Test deleting a book.
        """
        response = self.client.delete(f'/books/{self.book1.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)


    def test_filter_books_by_year(self):
        """
        Test filtering books by publication year.
        """
        response = self.client.get('/books/?publication_year=1945')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


    def test_search_books(self):
        """
        Test searching books by title.
        """
        response = self.client.get('/books/?search=animal')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Animal Farm')

    def test_order_books_by_year_desc(self):
        """
        Test ordering books by publication year descending.
        """
        response = self.client.get('/books/?ordering=-publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], '1984')


    def test_unauthenticated_access_denied(self):
        """
        Ensure unauthenticated users cannot access endpoints.
        """
        self.client.force_authenticate(user=None)
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
