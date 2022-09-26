from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name="about"),
    path('addpage/', add_page, name="add_page"),
    path('contact/', contact, name="contact"),
    path('login/', login, name="login"),
    path('register/', register, name="register"),
    path('post/<int:id>', show_post, name="post"),
    path('category/<int:category_id>', show_category, name="category"),

]


