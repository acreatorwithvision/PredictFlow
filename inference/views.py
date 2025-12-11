from django.shortcuts import render
from django.http import HttpResponse


def health(equest):
    return HttpResponse("PredictFlow is running.")
# Create your views here.
