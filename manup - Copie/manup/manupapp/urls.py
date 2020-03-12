from django.urls import path
from. import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog', views.blog, name='blog'),
    path('blog_details', views.blog_details, name='blog_details'),
    path('about_us', views.about_us, name='about_us'),
    path('contact', views.contact, name='contact'),
    path('main', views.main, name='main'),
    path('speaker', views.speaker, name='speaker'),
    path('schedule', views.schedule, name='schedule'),
]