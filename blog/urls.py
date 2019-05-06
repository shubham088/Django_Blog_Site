from django.conf.urls import url
from . import views
from blog.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    #url('^$', views.home, name = 'blog-home'),
    url('^$', PostListView.as_view(), name='blog-home'),
    url('about/', views.about, name = 'blog-about'),
    url('post/(?P<pk>[0-9]+)/', PostDetailView.as_view(), name = 'post-detail'), #url for specific post
    url('post/new/', PostCreateView.as_view(), name = 'post-create'), #working
    url('post/(?P<pk>[0-9]+)/update/', PostUpdateView.as_view(), name = 'post-update'),
    url('post/(?P<pk>[0-9]+)/del/', PostDeleteView.as_view(), name= 'post-delete'),

]
#
