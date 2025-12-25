from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path('why/', views.why, name='why'),
    path('about/', views.about, name='about'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
    path('bio/', views.bio, name='bio'),
    path('hashtag/', views.hashtags, name='hashtag'),
    path('posts/', views.posts, name='posts'),
    path('api/generate/', views.generate_ai_content, name='generate_ai'),
]