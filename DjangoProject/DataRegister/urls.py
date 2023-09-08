from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.empdata,name='FrontPage'),

    path('<int:id>/',views.empdata,name='Update'),

    path('Krishna/',views.empList,name="ListData"),
     
    path('delete/<int:id>',views.Delete,name='delete')

]
