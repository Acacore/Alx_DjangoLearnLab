from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from .models import Post

class PostModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="pass1234"
        )
        self.post = Post.objects.create(
            title="Test Post",
            content="Content here",
            author=self.user
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.author.username, "testuser")
