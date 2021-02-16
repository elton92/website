from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name="home"),
	path('posts/', views.posts, name="posts"),
	path('post/<slug:slug>/', views.post, name="post"), # visualizar cada publicacion
	path('contacto/', views.profile, name="contacto"),

# CRUD PATH:
	path('create_post/', views.createPost, name="create_post"),
	path('update_post/<slug:slug>/', views.UpdatePost, name="update_post"),
	path('delete_post/<slug:slug>/', views.deletePost, name="delete_post"),

	#

	path('send_email/', views.sendEmail, name="send_email"),

]