from django.shortcuts import render, get_object_or_404, resolve_url
from .forms import BlogForm
from .models import *
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def blogs(request):
    blog_list = Blogs.objects.all()
    paginator = Paginator(blog_list, 6)

    page = request.GET.get('page')
    try:
        all_blog = paginator.page(page)
    except PageNotAnInteger:
        all_blog = paginator.page(1)
    except EmptyPage:
        all_blog = paginator.page(paginator.num_pages)
        
    return render(request, 'blog.html', {'blogs': all_blog})

# class BlogList(ListView):
#     model = Blogs
#     template_name = 'blog.html'
#     context_object_name = 'blogs'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context

# def blog_details(request, id):
#     blog = get_object_or_404(Blogs, id=id)
#     return render(request, 'blog-details.html', {'blog': blog})

# class BlogDetailView(View):
#     def get_object(self):
#         return Blogs.objects.get(id=self.kwargs.get('id'))
    
#     def get(self, request, *args, **kwargs):
#         blog = self.get_object()
#         return render(request, 'blog-details.html', {'blog': blog})

class BlogDetail(DetailView):
    model = Blogs
    template_name = 'blog-details.html'
    context_object_name = 'blog'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class CreateBlogPost(CreateView):
    model = Blogs
    form_class = BlogForm
    template_name = 'create_blog.html'
    
    def get_success_url(self):
        return resolve_url('/blog/blogs')
    
    
class UpdateBlogPost(UpdateView):
    model = Blogs
    form_class = BlogForm
    template_name = 'update_blog.html'
    
    def get_success_url(self):
        return resolve_url('blog_details', pk=self.kwargs['pk'])    
    
class DeleteBlogPost(DeleteView):
    model = Blogs
    template_name = 'delete_blog.html'
    success_url = '/blog/blogs'    