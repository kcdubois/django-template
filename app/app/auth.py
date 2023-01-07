from django.urls import path, include
from django.http.request import HttpRequest
from django.shortcuts import render


def account_profile(request: HttpRequest):
    return render(
        request,
        template_name="registration/profile.html"
    )


urlpatterns = [
    path('profile/', account_profile),
    path('', include('django.contrib.auth.urls'))
]