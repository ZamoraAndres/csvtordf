from django.conf.urls import patterns, url
from csvtottl import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
	url(r'^csvtordf$', views.csvtordf, name='csvtordf'),	
	url(r'^deleteFile/$', views.deleteFile, name='deleteFile'),
    url(r'^convertFile/$', views.convertFile, name='convertFile'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)