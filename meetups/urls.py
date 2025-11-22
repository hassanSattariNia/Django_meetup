from django.urls import path
from . import views

urlpatterns = [
    # url , then function have to called when this url witted on the browser
    path('meetups/',views.index)
]
