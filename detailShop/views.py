from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse


def main(request):
    return TemplateResponse(request, 'menu.html')