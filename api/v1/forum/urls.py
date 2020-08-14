from django.conf.urls import url,include
from django.urls import path
from api.v1.forum import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
app_name = 'forum_api'
urlpatterns = [
    url(r'^$',views.forumlist),
    url(r'^(?P<pk>.*)/subforums/$',views.subforumlist),
    url(r'^subforums/(?P<subforum_id>.*)/treads/$',views.treadList),
    url(r'^subforums/(?P<subforum_id>.*)/treads/create/$',views.treadcreate),
    url(r'^treads/(?P<tread_id>.*)/view/$',views.treadView),
    url(r'^treads/(?P<tread_id>.*)/edit/$',views.editThread),
    url(r'^treads/(?P<tread_id>.*)/delete',views.deleteTread),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    url(r'^signup/$',views.signupView),
   
]