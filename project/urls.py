from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^measurments/$','app.views.measurments' ),
    url(r'^model_list/$','app.views.model_list' ),
    url(r'^model_detail/(?P<pk>.+)/$', 'app.views.model_detail'),
    url(r'^fabric_list/$','app.views.fabric_list' ),
    url(r'^fabric_detail/(?P<pk>.+)/$', 'app.views.fabric_detail'),
    url(r'^tailor_list/$','app.views.tailor_list' ),
    url(r'^tailor_detail/(?P<pk>.+)/$', 'app.views.tailor_detail'),



    url(r'^create_model/$', 'app.views.create_model'),
    url(r'^edit_model/(?P<pk>.+)/$', 'app.views.edit_model'),
    url(r'^delete_model/(?P<pk>.+)/$', 'app.views.delete_model'),



    url(r'^create_fabric/$', 'app.views.create_fabric'),
    url(r'^edit_fabric/(?P<pk>.+)/$', 'app.views.edit_fabric'),
    url(r'^delete_fabric/(?P<pk>.+)/$', 'app.views.delete_fabric'),



    url(r'^signup/$', 'app.views.sign_up'),
    url(r'^logout/$', 'app.views.logout_view'),
    url(r'^signin/$', 'app.views.login_view'),
    url(r'^profile/$', 'app.views.profile_page'),
    url(r'^edit_profile/$', 'app.views.edit_profile'),






    url(r'^$', include('social.apps.django_app.urls', namespace='social')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
