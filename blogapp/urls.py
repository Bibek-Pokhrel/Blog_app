from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('base',views.base),
    path('home',views.home,name='home'),
    path('comment/<pk>',views.blogcomment,name='commentpost'),
    path("delete/<pk>",views.cmtdelete,name='delete'),
    path("editcmt/<pk>",views.cmtedit,name='editcmt'),
    path('profile',views.profile,name='profile'),
    path('register',views.register,name='register'),
    path('',views.userlogin,name='login'),
    path('logout',views.user_logout,name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
