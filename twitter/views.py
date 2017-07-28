from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'twitter/post_list.html', {'posts': posts})

def registrar(request):
	return render(request, 'twitter/registrar.html')

def postear(request):
	return render(request, 'twitter/postear.html')

def calendario(request):
	return render(request, 'twitter/Calendario.html')