from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect

from .models import Post
from .forms import PostForm


# Create your views here.
def post_create(request):
    form = PostForm(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Successfully Created' )
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, 'Not Successfully Created')
    context={'form':form}
    return render(request, 'create.html', context)

def post_detail(request, id):
    instance=get_object_or_404(Post, id=id)
    context={'title':instance.title,
             'instance':instance}
    return render(request,'detail.html',context)

def post_list(request):

    queryset = Post.objects.all().order_by('-timestamp')
    context = { 'post_list': queryset,
                'title': 'list'}
    return render(request, 'list.html',context)


def post_update(request, id=None):
    instance=get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Successfully Created' )
        return HttpResponseRedirect(instance.get_absolute_url())

    context={'title':instance.title,
             'instance':instance,
             'form':form,}
    return render(request,'create.html',context)


def post_delete(request, id=None):
    instance=get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, 'Successfully Deleted')
    return redirect('post:post')

