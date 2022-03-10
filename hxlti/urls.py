from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r"^launch/", views.lti_landing_page, name="lti_landing"),
]
