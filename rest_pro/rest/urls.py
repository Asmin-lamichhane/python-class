from django.urls import path
import rest.views as views

urlpatterns = [
   
    # path('display_student/', views.display_student_data, name='student_view'),
    path('display_pizza/', views.Display_Pizza, name='pizza_view'),

]
