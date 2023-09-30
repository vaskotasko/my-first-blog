from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User
from pprint import pprint
from django.utils import timezone

# Create your views here.

# def post_list(request):    # LOGIKA MOJEJ WEBSTRANKY
#     posts = Post.objects.all()    # toto znamena vytvorenie QUERY select * from Post
#     pprint(User.objects.all())
#     me = User.objects.get(username = 'mariana')
#     pprint(me)
#     contextB = Post(author=me, title='Pizza zjedena', text = 'uz')
#     contextB.save()
#     contextC = Post(author=me, title='No more pizza', text = 'nechcem')
#     contextC.save()
#     return render(request, 'blog/post_list.html', {'context': posts, 'postB':contextB, 'postC':contextC})    # volam query

# def post_list(request):    # LOGIKA MOJEJ WEBSTRANKY
#     me = User.objects.get(username = 'mariana')
#     posts = Post.objects.filter(author = me)    # toto znamena vytvorenie QUERY select * from Post    
#     return render(request, 'blog/post_list.html', {'context': posts})   

# def post_list(request):    # LOGIKA MOJEJ WEBSTRANKY
#     post_pizza = Post.objects.filter(title__contains = 'pizza')  # filter vypise vsetky,ktore obsahuju pizza
#     return render(request, 'blog/post_list.html', {'context': post_pizza})   

# def post_list(request):    # LOGIKA MOJEJ WEBSTRANKY
#     post_pizza = Post.objects.get(title__contains = 'pizza')  # !!!!! get vypise prave jednu hodnotu, cize ERROR, lebo viacere obsahuju PIZZA
#     return render(request, 'blog/post_list.html', {'context': post_pizza})


# def post_listB(request):
#     timez = Post.objects.filter(published_date__lte=timezone.now())
#     me = User.objects.get(username='mariana')
#     new_post = Post(author=me, title='cakam na kavu', text = 'teraz')
#     new_post.publish()
#     return render(request, 'blog/post_list.html', {'times': timez})

def post_listB(request):
    timez = Post.objects.filter(published_date__lte=timezone.now())
    return render(request, 'blog/post_list.html', {'times': timez})

def post_listC(request):
    timez = Post.objects.order_by('created_date')
    return render(request, 'blog/post_list.html', {'times': timez})

def post_listD(request):
    timez = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'times': timez})

def post_list(request):    # LOGIKA MOJEJ WEBSTRANKY
    posts = Post.objects.all()    # toto znamena vytvorenie QUERY select * from Post
    return render(request, 'blog/post_list.html', {'posts': posts})

def test(request):
    return render(request, 'blog/test.html', {})



