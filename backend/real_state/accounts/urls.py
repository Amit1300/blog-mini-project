from django.urls import path

from accounts import views
urlpatterns = [
    path('blog',views.Blog.as_view()),
    path('blog/<int:id>/',views.Blog.as_view()),
    path("signup/",views.Signup),
   
 
]
