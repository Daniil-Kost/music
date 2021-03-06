"""music URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, url
from django.contrib import admin
from .settings import MEDIA_ROOT, DEBUG
from catalog.views import TrackView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', 'catalog.views.singers_list',
        name='home'),
    url(r'^albums/$', 'catalog.views.albums_list',
        name='albums'),
    url(r'^genres/$', 'catalog.views.genres_list',
        name='genres'),
    url(r'^track/(?P<pk>\d+)/$',
        TrackView.as_view(),
        name='track'),

]

if DEBUG:
    # serve files from media folder
    urlpatterns += patterns('',
                            url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                                {'document_root': MEDIA_ROOT}))
