from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import *
from django.views import View

# Create your views here.

def homepage(request):
    return render(request,'base.html')

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
