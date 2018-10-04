from django.shortcuts import render
from django.views.generic.base import TemplateView

import json
from django.http import JsonResponse

# Create your views here.
app_name='RestApi'

def getTasks(request):
    response_data = {}
    response_data['result'] = 'error'
    response_data['message'] = 'Some error message'

    return JsonResponse(response_data)
