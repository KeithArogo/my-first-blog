from django.shortcuts import render
from django.utils import timezone
from .models import Post#The dot before models means it is in the current directtory
# Create your views here.
# request is anything you receive from the user via the internet
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})