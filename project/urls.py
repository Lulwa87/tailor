from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from django.views.generic.base import TemplateView
from app import views


urlpatterns = [
	# Examples:
	# url(r'^$', 'project.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	url(r'^admin/', include(admin.site.urls)),
	url(r'^measurments/$','app.views.measurments'),

	url(r'^fabric_list/$','app.views.fabric_list'),
	url(r'^fabric_detail/(?P<pk>.+)/$', 'app.views.fabric_detail'),
	url(r'^tailor_list/$','app.views.tailor_list'),
	url(r'^tailor_detail/(?P<pk>.+)/$', 'app.views.tailor_detail'),

	#products
	url(r'^products/$', TemplateView.as_view(template_name='product.html'), name='products'),
	url(r'^product_design_list/$','app.views.product_design_list'),
	url(r'^product_detail/(?P<pk>.+)/$', 'app.views.product_design_detail'),
	url(r'^ready_to_wear/$', 'app.views.Ready_to_wear'),
	url(r'^ready_detail/(?P<pk>.+)/$', 'app.views.ready_detail'),


	url(r'^create_model/$', 'app.views.create_model'),
	url(r'^edit_model/(?P<pk>.+)/$', 'app.views.edit_model'),
	url(r'^delete_model/(?P<pk>.+)/$', 'app.views.delete_model'),



	url(r'^create_fabric/$', 'app.views.create_fabric'),
	url(r'^edit_fabric/(?P<pk>.+)/$', 'app.views.edit_fabric'),
	url(r'^delete_fabric/(?P<pk>.+)/$', 'app.views.delete_fabric'),



	url(r'^signup/$', 'app.views.sign_up'),
	url(r'^logout/$', 'app.views.logout_view'),
	url(r'^login/$', 'app.views.login_view'),
	url(r'^profile/$', 'app.views.profile_page'),
	url(r'^edit_profile/$', 'app.views.edit_profile'),


	url(r'^sendmail/$', 'app.views.sendmail'),
	
	url(r'^thankyou/$', TemplateView.as_view(template_name='thankyou.html'), name='thankyou'),
	url(r'^checkout/$', TemplateView.as_view(template_name='checkout.html'), name='checkout'),

	url(r'^homepage/$', TemplateView.as_view(template_name='index.html'), name='homepage'),

	url(r'^cart/', include('cart.urls', namespace='cart')),
	
	# url(r'^$', include('social.apps.django_app.urls', namespace='social')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
