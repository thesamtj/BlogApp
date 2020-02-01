from django.urls import path

from . import views 

app_name = 'blog'

urlpatterns = [
	path('', views.post_list, name='post_list'),
    #path('', views.PostListView.as_view(), name='post_list'),
    
    path('tag/<str:tag_slug>/', views.post_list, name='post_list_by_tag'),
    #url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list, name='post_list_by_tag'),
	
	
	path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    #path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	
    path('<int:post_id>/share/', views.post_share, name='post_share')
    #url(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share')
    

]