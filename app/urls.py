from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),

    # url(r'^hoods', views.hoods, name='hoods'),
    url(r'^join/(\d+)$',views.join, name = 'joinhood'),
    url(r'^createHood/$', views.createHood, name='createHood'),
    url(r'^showprofile/(?P<id>\d+)', views.display_profile, name='showprofile'),
    url(r'^exithood/(\d+)$', views.exithood, name='exithood'),
    url(r'^createbusiness/$', views.createbiz, name='createbiz'),
    url(r'^createpost/$', views.createPost, name='createpost'),
    # url(r'^new/createbusiness/$', views.createbusiness, name='createbusiness'),
    # url(r'^businesses/$',views.businesses,name= 'businesses'),
    url(r'search/', views.search, name='search'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

