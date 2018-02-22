from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView

from .models import Author

# Create your views here.
def index(request):
	return HttpResponse("Hello, cruel world!")
	
class AuthorListView(ListView):

	model = Author

def authors2(request):
	return render(request, 'blog/author_list.html', {
		'object_list': Author.objects.all()
		})
