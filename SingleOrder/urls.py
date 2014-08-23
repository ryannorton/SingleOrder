from django.conf.urls import patterns, include, url
from django.contrib import admin
from app import views
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^meal/(?P<group>.+)/?', views.meal),    
    url(r'^joinmeal/', views.joinmeal),
    url(r'^createmeal/', views.createmeal),
    url(r'^admin/', include(admin.site.urls)),
)
