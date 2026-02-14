from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm



# Create your views here.
def home(request):
    return render(request, 'blog/home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


@login_required
def profile(request):
    # You can access the profile like this:
    profile = request.user.profile
    return render(request, 'blog/profile.html', {'profile': profile})
