from django.urls import path

from uploads.views import index

urlpatterns = [path("", index, name="index")]
