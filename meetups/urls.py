from django.urls import path
from . import views

urlpatterns = [
    # url , then function have to called when this url witted on the browser
    path('meetups/',views.index,name='all-meetups'),
    path('meetups/success',views.confirm_registeration,name='confirm-registeration'),
    path('meetups/<slug:meetup_slug>/', views.meetup_details, name='meetup-details'), #using dynamic path segment
    
]
