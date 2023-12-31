from django.urls import path, include
from . import views


app_name = 'learning_logs'
#app_name = 'users'
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    # Страница с подробной информацией по отдельной теме
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Страница со списком всех тем.
    path('topics/', views.topics, name='topics'),
    # Страница для добавления новой темы
    path('new_topic/', views.new_topic, name='new_topic'),
    # Страница для добавления новой записи
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Страница для редактирования записи
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

]

