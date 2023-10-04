from django.urls import path
from myapp4.views import user_form

urlpatterns = [
    path('user/add/', user_form, name='user_form'),
]
