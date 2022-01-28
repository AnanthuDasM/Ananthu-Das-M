from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from  .import views

urlpatterns = [
    path('',views.add,name='add'),
    # path('details',views.details,name='details')
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvhome1/',views.Tasklistview.as_view(),name='cbvhome1'),
    path('cbvdetail/<int:pk>/',views.TaskDetailview.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.TaskUpdateview.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.TaskDetailview.as_view(),name='cbvdelete'),

]

