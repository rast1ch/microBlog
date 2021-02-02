from django.urls import path

from . import views

app_name = 'blog'
urlpatterns  = [
    path("", views.HomePageView.as_view(), name = 'index'),
    path('post/<int:pk>/', views.BlogDetailView.as_view(), name = 'post_detail')
]