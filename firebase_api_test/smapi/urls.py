# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('noModelTest/', views.NoModelTest.as_view()),
    path('smbotText/', views.SmbotTextQuery.as_view()),
    # path('<int:pk>/', views.DetailHelloWolrd.as_view()),
]
