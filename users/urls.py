from django.urls import path

from .views import *

urlpatterns = [
    path('', CourseListView.as_view(), name='course_list'),
    path('course/create/', CourseCreateView.as_view(), name='course_create'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('course/<int:pk>/update/', CourseUpdateView.as_view(), name='course_update'),
    path('course/<int:pk>/delete/', CourseDeleteView.as_view(), name='course_delete'),

    path('user/', UserListView.as_view(), name='user_list'),
    path('user/create/', CreateUserView.as_view(), name='user_create'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('user/<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('user/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),

    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('category/<int:pk>/update/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
]
