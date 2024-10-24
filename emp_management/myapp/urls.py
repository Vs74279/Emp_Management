
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home ,name='home' ),
    path('about/',views.about ,name='about'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('success/', views.success_view, name='success'),
    path('view_employees/', views.view_employees, name='view_employees'),
    path('follow/', views.follow_view, name='follow'),
    path('subscribe/', views.subscribe_view, name='subscribe'), 
     path('update_employee/<int:id>/',views.update_employee, name='update_employee'),
    path('delete_employee/<int:id>/',views.delete_employee, name='delete_employee'),
]
