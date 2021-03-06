from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'radiologyapp.views.home', name='home'),
    # url(r'^radiologyapp/', include('radiologyapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),


    # include urls for custom apps
    url(r'^', 'usermanagement.views.home'),

    url(r'^users/', include('usermanagement.urls')),
    url(r'^patients/', include('patientmanagement.urls')),

)
