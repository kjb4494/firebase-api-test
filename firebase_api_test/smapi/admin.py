from django.contrib import admin
from .models import HelloWorld
from drf_firebase_auth.models import FirebaseUser, FirebaseUserProvider

# Register your models here.
admin.site.register(HelloWorld)
admin.site.register(FirebaseUser)
admin.site.register(FirebaseUserProvider)
