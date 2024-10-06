from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),  # Home page
    path('<slug:slug>/', views.post_detail, name='post_detail'),  # Post detail
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
     path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]
