from django.shortcuts import render

def post_list(request):
	return render(reqeuest, 'blog/post_list.html', {})
# Create your views here.
