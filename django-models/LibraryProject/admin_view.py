from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy
from relationship_app.utils import is_admin

@user_passes_test(is_admin, login_url=reverse_lazy('login'))
def admin_dashboard(request):
    return render(request, 'relationship_app/admin_dashboard.html')
