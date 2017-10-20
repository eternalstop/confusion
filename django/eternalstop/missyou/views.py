# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
	# return HttpResponse("I miss you!I love you!")
	context_dict = {'boldmessage': "Love!"}
	return render(request, 'index.html', context=context_dict)


def about(request):
	context_dict = {'boldmessage': "Hua!"}
	return render(request, 'about.html', context=context_dict)
	# return HttpResponse("It's about love for you!From LH!""<br />""About(missyou)view<a href='/missyou/'>Index</a>. ")


def test(request):
	return HttpResponse("It's a test pages!Thank you!")
