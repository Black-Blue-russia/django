from django.shortcuts import render
from .models import Post
def post_list(request):
    post_objects_all = Post.objects.all()
    context ={
        'post_objects': post_objects_all

    }
    return render(request, "index.html", context)
