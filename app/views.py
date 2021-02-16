from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

from .models import Publicar
from .forms import PostForm
from .filters import PosFilter


def home(request):
    posts = Publicar.objects.filter(activo=True, destacar=True)[0:3]
    context = {'posts': posts}
    return render(request,'app/service.html', context)

def posts(request):
    posts = Publicar.objects.filter(activo=True)
    myFilter = PosFilter(request.GET, queryset=posts)
    posts = myFilter.qs

    page = request.GET.get('page')

    paginator = Paginator(posts, 6)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {'posts':posts, 'myFilter':myFilter}
    return render(request,'app/posts.html', context)

def post(request, slug):
	post =	Publicar.objects.get(slug=slug)

	context = {'post':post}

	return render(request, 'app/post.html', context)



    # return render(request, "registro.html")

def profile(request):
    return render(request,'app/crud/contacto.html')


# CRUD:

@login_required(login_url="home")
def createPost(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('posts')

    context = {'form': form}
    return render(request, 'app/post_form.html', context)


@login_required(login_url="home")
def UpdatePost(request, slug):
    post = Publicar.objects.get(slug=slug)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return redirect('posts')

    context = {'form': form}
    return render(request, 'app/post_form.html', context)


@login_required(login_url="home")
def deletePost(request, slug):
    post = Publicar.objects.get(slug=slug)

    if request.method == 'POST':
        post.delete()
        return redirect('posts')

    context = {'item': post}
    return render(request, 'app/delete.html', context)


def sendEmail(request):
    if request.method == 'POST':
        template = render_to_string('email_template.html', {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'message': request.POST['message'],
        })

        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['emiguelcachili@gmail.com']
        )

        email.fail_silently = False
        email.send()

    return render(request, 'email_send.html')


