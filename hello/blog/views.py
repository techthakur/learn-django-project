from django.shortcuts import render
from blog.models import Post

# Create your views here.


def bloghome(request):
    allPostsss = Post.objects.all()
    # print(allPostsss)
    context = {'allPostsss': allPostsss}
    return render(request, "blog/bloghome.html",   context)

  
 

def blogpost(request):
    return render(request, "blog/blogpost.html")





def search(request):
    allPosts = Post.objects.all()
    params = {'allPosts': allPosts}
    return render(request, "search.html"  , params)
