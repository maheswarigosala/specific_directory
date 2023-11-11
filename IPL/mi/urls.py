from mi.views import *
from django.urls import path
app_name="nothing"
urlpatterns=[
    path('rohit/',rohit,name="rohit"),
    path('boomra/',boomra,name="boomra"),
]