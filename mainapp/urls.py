from django.urls import path, re_path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', NewsHome.as_view(), name='home'),
    path('about/', about, name="about"),
    path('addpage/', AddPage.as_view(), name="add_page"),
    path('develop/', develop, name="dev_page"),
    path('contact/', ContactFormView.as_view(), name="contact"),
    path('login/', loginUser.as_view(), name="login"),
    path('logout/', logout_user, name="logout"),
    path('register/', RegisterUser.as_view(), name="register"),
    path('post/<slug:slug>', ShowPost.as_view(), name="post"),
    path('category/<slug:slug>', NewsCategory.as_view(), name="categories"),
    path('<int:year>/<str:month>/', archive, name="archive")

]


