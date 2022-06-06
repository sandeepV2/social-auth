from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required

# # Create your views here.

def index(request):
    my_dict = {'insert_me': "Hello I am from views.py!"}
    context = {
        'posts': Post.objects.order_by('-date')
        if request.user.is_authenticated else []
    }
    return render(request, 'authentication/index.html',context)

def login(request):
    return render(request, 'authentication/index.html')


@login_required
def home(request):
    return render(request, 'authentication/index.html')