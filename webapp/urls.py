from django.urls import path
from webapp.views import index_create

urlpatterns = [
    path('', index_create),
]
