'''
A view is a place where we put the "logic" of our application. 
It will request information from the model you created before 
and pass it to a template.
'''
from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import Post
def post_list(request):
	context = {
		'my_name' : 'Catman Tiger.',
		'my_address' : 'Peradeniya'
		}
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html',{'post': post})