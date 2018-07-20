
import logging

from lti.contrib.django import DjangoToolProvider

from django.conf import settings
from django.http import HttpResponseBadRequest
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .validators import LTIRequestValidator


@require_http_methods(['POST'])
@csrf_exempt
@xframe_options_exempt  # allows rendering in Canvas|edx frame
def lti_launch(request):

    # is this an lti launch request?
    is_basic_lti_launch = \
            request.POST.get('lti_message_type', '') == 'basic-lti-launch-request'
    has_lti_version = request.POST.get('lti_version', '') == 'LTI-1p0'
    oauth_consumer_key = request.POST.get('oauth_consumer_key', None)
    resource_link_id = request.POST.get('resource_link_id', None)

    if not (is_basic_lti_launch and has_lti_version and \
            oauth_consumer_key and resource_link_id):
        return HttpResponseBadRequest()

    # lti request authentication
    validator = LTIRequestValidator()
    tool_provider = DjangoToolProvider.from_django_request(
        secret=validator.get_client_secret(oauth_consumer_key, request),
        request=request)

    valid_lti_request = tool_provider.is_valid_request(validator)

    if valid_lti_request:
        # redirect to landing page
        return landing_page(request)

    else:
        return HttpResponseForbidden()


@xframe_options_exempt  # allows rendering in Canvas|edx frame
def landing_page(request):
    return render(request, 'hxlti/index.html')
