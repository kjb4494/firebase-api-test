from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ListHelloWolrd.as_view()),
    path('<int:pk>/', views.DetailHelloWolrd.as_view()),
]
