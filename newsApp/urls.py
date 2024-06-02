
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views 
urlpatterns = [
    path("news/",views.getnews,name='getnews'),
    path("loans/",views.get_loan_data,name='get_loan_data'),

]
