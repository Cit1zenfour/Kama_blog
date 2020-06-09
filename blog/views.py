from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .forms import CommentForm, UserRegisterForm, UserAuthForm
from django.contrib.auth import login, logout


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserRegisterForm()
    return render(request, 'auth/register.html', {'form': form})



def user_login(request):

    if request.method == 'POST':
        form = UserAuthForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')

    else:
        form = UserAuthForm()
    return render(request, 'auth/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')



def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()


        context = {
            'queryset': queryset
        }
        return render(request, 'search_result.html', context)




def index(request):
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:3]
    context = {
        'object_list': featured,
        'latest': latest,
    }
    return render(request, 'index.html', context)


def blog(request):
    most_recent = Post.objects.order_by('-timestamp')[:3]
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'post_list': paginated_queryset,
        'most_recent': most_recent,
        'page_request_var': page_request_var,
    }
    return render(request, 'blog.html', context)

def post(request, id):
    post = get_object_or_404(Post, id=id)
    form = CommentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse('post', kwargs={
                'id': post.id,
            }))
    context = {
        'post': post,
        'form': form,
    }

    return render(request, 'post.html', context)

