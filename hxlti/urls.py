
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^lti_launch/', views.lti_launch, name='lti_launch'),
]
