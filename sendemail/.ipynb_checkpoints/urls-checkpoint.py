from django.urls import path

from .views import emailView, successView, postView

urlpatterns = [
  path('email/', emailView, name='email'),
  path('post/', postView, name='email'),
  path('success/', successView, name='success'),
]
