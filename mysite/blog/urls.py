from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path('', views.index, name='index'),
    path("blog/<int:blog_id>", views.blog, name='blog'),
    path("about/", views.about, name='about'),
    path("tips/", views.tips, name='tips'),
    path("comment/<int:blog_id>", views.comment, name='comment'),
    path("archive/", views.archive, name='archive')
]

