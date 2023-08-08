from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="nfactorial"),
    path("<int:first>/add/<int:second>/", views.add, name="sum"),
    path("transform/<str:text>/", views.upper, name="upper"),
    path("check/<str:word>/", views.palindrome, name="palindrome"),
    path("calc/<int:first>/<str:operation>/<int:second>/", views.calculator, name="calculator")
]