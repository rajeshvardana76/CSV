
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import profile_upload

urlpatterns = [
    path('upload-csv/', profile_upload, name="profile_upload"),
]