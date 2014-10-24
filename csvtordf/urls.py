from django.conf.urls import patterns, include, url
from django.contrib import admin
from csvtottl import views
from django.conf import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'csvtordf.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^csvtottl/', include('csvtottl.urls', namespace='csvtottl')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
    	'document_root': settings.MEDIA_ROOT})
)
