from __future__ import print_function
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import usuario
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	post_borrar2 = request.POST.get('botoncito','')
	print(post_borrar2)
	print("post_borrar2")
	if (post_borrar2 != ""):
		postb2 = Post.objects.filter(title=post_borrar2)
		postb2.delete()
	return render(request, 'twitter/post_list.html', {'posts': posts})

def borrar_post(request):
	post_borrar = request.POST.get('borrarxd','')
	if (post_borrar != ""):
		postb = Post.objects.filter(title=post_borrar)
		postb.delete()

	return render(request, 'twitter/borrar_post.html',)


def registrar(request):
	nickname2 = request.POST.get('user1','')
	passw2 = request.POST.get('pass1','')
	mail2 = request.POST.get('mail1','')
	nombre2 = request.POST.get('nombre1','')
	apellido2 = request.POST.get('apellido1','')
	try:
		user = User.objects.create_user(nickname2,mail2,passw2)
		user.save()
	except ValueError as aValueError:
		pass
	return render(request, 'twitter/registrar.html')

def postear(request):
	usr = request.user
	title3 = request.POST.get('titulo2','')
	text3 =  request.POST.get('texto2','')
	link3 = request.POST.get('link2','')
	post12 = Post(author = usr, title = title3, text = text3, link = link3)
	if ((post12 is not None) and (request.POST.get('titulo2','') != "")):
		print("funciono el post")
		post12.save()
	else:
		print("no funciono el post")
	print(".-.-.-.-.-.-.")
	return render(request, 'twitter/postear.html')

def logear(request):
    username = request.POST.get('user3','')
    password = request.POST.get('pass3','')
    user2 = authenticate(username=username, password=password)
#    user2 = authenticate(username="asdf", password="asdf12")
    if (user2 is not None):
        login(request, user2)
        print("funciono el login")
        return render(request, 'twitter/postear.html')
    else:
        print("no funciono el login")
    return render(request, 'twitter/logear.html')

def calendario(request):
	return render(request, 'twitter/Calendario.html')