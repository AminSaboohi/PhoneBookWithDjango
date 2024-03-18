from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('phone_book_record/<int:pk>',
         views.phone_book_record,
         name='phone_book_record'),
    path('delete_phone_book_record/<int:pk>',
         views.delete_phone_book_record,
         name='delete_phone_book_record'),
    path('add_phone_book_record/',
         views.add_phone_book_record,
         name='add_phone_book_record'),
    path('add_city/',
         views.add_city,
         name='add_city'),
    path('add_province/',
         views.add_province,
         name='add_province'),
    path('update_record/<int:pk>',
         views.update_phone_book_record,
         name='update_record'),
]
