from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from relationship_app.utils import is_member

@user_passes_test(is_member)
def member_dashboard(request):
    return render(request, 'member_dashboard.html')
