from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Post
from django.views.generic import CreateView


def list_of_post(request):
    post = Post.objects.all()
    template = 'posty/posty.html'
    context = {'post': post}
    return render(request, template, context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    template = 'posty/posty_szczegoly.html'
    context = {'post': post}
    return render(request, template, context)


class PostCreateView(CreateView):
    template_name = 'posty/post_create.html'
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('posty')

