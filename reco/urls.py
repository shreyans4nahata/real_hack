from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import patterns, url
from django.conf import settings
from reco import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'gplaces.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^gog/$', views.gog ,name= 'places'),
    url(r'^fb/$', views.fb ,name= 'fb'),
    url(r'^mongo/$', views.mongo ,name= 'mongo'),
   # url(r'^gog/', reco.views.goo,name= 'places'),

    url(r'^admin/', include(admin.site.urls)),
]
