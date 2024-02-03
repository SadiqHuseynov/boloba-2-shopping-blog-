from django.urls import path

from . import views

urlpatterns = [
    # path('blogs/', views.BlogList.as_view(), name="blogs"),
    path('blogs/', views.blogs, name="blogs"),
    # path('blog_details/<int:id>/', views.blog_details, name="blog_details"),
    # path('blog_details/<int:id>/', views.BlogDetailView.as_view(), name="blog_details"),
    path('blog_details/<int:pk>/', views.BlogDetail.as_view(), name="blog_details"),
    path('create', views.CreateBlogPost.as_view(), name="blogcreate"),
    path('update/<int:pk>/', views.UpdateBlogPost.as_view(), name="blog_update"),
    path('delete/<int:pk>/', views.DeleteBlogPost.as_view(), name="blog_delete"),
]
 