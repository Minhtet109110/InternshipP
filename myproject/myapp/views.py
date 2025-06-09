from django.shortcuts import render,redirect
<<<<<<< HEAD
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import *
from django.views import View

=======
from .forms import UserForm, UserProfileForm
>>>>>>> a93455c5bc173c7888c0e794e5e74afaf624b516
# Create your views here.

def homepage(request):
    return render(request,'base.html')

<<<<<<< HEAD
@method_decorator(login_required, name='dispatch')
class PostProjectView(View):
    def get(self, request):
        form = ProjectForm()
        return render(request, 'post_project.html', {'form': form})

    def post(self, request):
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.client = request.user
            project.save()
            return redirect('home')
        return render(request, 'post_project.html', {'form': form})
=======
def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            return redirect('login')
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'register.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def register(request):
 if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('register')
 else:
        user_form = UserForm()
        profile_form = UserProfileForm()
 return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form})
>>>>>>> a93455c5bc173c7888c0e794e5e74afaf624b516
