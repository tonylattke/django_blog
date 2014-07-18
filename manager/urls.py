import os
from django.conf.urls import patterns, include, url
import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^'		, include('website.urls')),
	url(r'^admin/'	, include(admin.site.urls)),
)

if settings.DEBUG:
	urlpatterns += staticfiles_urlpatterns()

	urlpatterns += patterns('',
		url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
			'document_root': settings.MEDIA_ROOT,
		}),

		url(r'^templates/(?P<path>.*)$', 'django.views.static.serve', {
			'document_root': settings.TEMPLATE_DIRS[0],
		}),
	)

if settings.DEBUG404:
	urlpatterns += patterns('',
		(r'^static/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root': os.path.join(os.path.dirname(__file__), 'static')} ),
		)