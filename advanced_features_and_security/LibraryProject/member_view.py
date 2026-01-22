from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from relationship_app.utils import is_member
from django.urls import reverse_lazy

@user_passes_test(is_member, login_url=reverse_lazy('relationship_app:login'))
def member_dashboard(request):
    return render(request, 'member_dashboard.html')
