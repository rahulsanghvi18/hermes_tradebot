from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
import apps.frontend.views as view

urlpatterns = [
    path('', view.IndexPageView.as_view(), name="index"),
]
