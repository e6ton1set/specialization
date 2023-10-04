from django.urls import path
from myapp4.views import user_form, many_fields_form

urlpatterns = [
    path('user/add/', user_form, name='user_form'),
    path('forms/', many_fields_form, name='many_fields_form'),
]
