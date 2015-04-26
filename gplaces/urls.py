#from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
#import reco
urlpatterns = [
    # Examples:
    # url(r'^$', 'gplaces.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^reco/', include('reco.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
