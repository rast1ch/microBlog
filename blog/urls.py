from django.urls import path

from . import views

app_name = 'blog'
urlpatterns  = [
    path("", views.HomePageView.as_view(), name = 'index'),
    path('post/<int:pk>/', views.BlogDetailView.as_view(), name = 'post_detail'),
    path('post/<int:pk>/edit' , views.BlogUpdateView.as_view(), name = 'post_edit'),
    path('post/<int:pk>/delete' , views.BlogDeleteView.as_view() , name = 'post_delete'),
    path('post/new/', views.BlogCreateView.as_view(), name = 'new'),


]