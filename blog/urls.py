from django.urls import path
from . import views
from users import views as user_views
from django.contrib.auth import views as auth_views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView

urlpatterns = [

    path('', PostListView.as_view(), name='home'),
    path('blog/<int:pk>/', PostDetailView.as_view(), name='blog-detail'),
    path('blog/new/', PostCreateView.as_view(), name='create-blog'),
    path('blog/<int:pk>/update/', PostUpdateView.as_view(), name='update-blog'),
    path('about/', views.about, name='about'),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

]