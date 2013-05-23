from django.conf.urls import patterns, include, url
from proyecto import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',views.index,name="index"),
    url(r'^proyecto/registro/$',views.registro ,name="registro"),
    url(r'^terminar/$',views.registro),
    # Examples:
    # url(r'^$', 'ciencias2.views.home', name='home'),
    # url(r'^ciencias2/', include('ciencias2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
