from django.urls import path
import info.views as views

urlpatterns =[
    path('',views.info,name='info')
]