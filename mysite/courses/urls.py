from django.urls import path
from .views import CoursesViewSet

urlpatterns = [
    path('courses', CoursesViewSet.as_view({
        'get':'list',
        'post':'create'      
    })),
    
    path('courses/add-vector', CoursesViewSet.as_view({
         'post':'addVector'
    }))
]
