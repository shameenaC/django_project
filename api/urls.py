from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('employees',views.EmployeeViewset, basename='employee')

urlpatterns=[
    path('students/',views.studentsview),
    path('students/<int:pk>' ,views.studentdetialview),

    #path('employees/',views.Employeeview.as_view()),
    #path('employees/<int:pk>',views.EmployeeDetialview.as_view()),

    path('',include(router.urls)),

    path('blogs/',views.BlogView.as_view()),
    path('comments/',views.CommentView.as_view()),

    path('blogs/<int:pk>', views.BlogDetialView.as_view()),
    path('comments/<int:pk>', views.CommentDetialView.as_view()),

 
]