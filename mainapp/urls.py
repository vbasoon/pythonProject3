from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', NewsHome.as_view(), name='home'),
    path('about/', about, name="about"),
    path('addpage/', AddPage.as_view(), name="add_page"),
    path('develop/', develop, name="dev_page"),
    path('contact/', contact, name="contact"),
    path('login/', login, name="login"),
    path('register/', register, name="register"),
    path('post/<slug:slug>', ShowPost.as_view(), name="post"),
    path('category/<slug:slug>', NewsCategory.as_view(), name="categories"),

]


