from django.conf.urls import patterns, include, url
from users.views import *
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'h_trader.views.home', name='home'),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^signup/', SignupView.as_view(), name='signup'),
    url(r'^register/', RegisterView.as_view(), name='register'),
    url(r'^login/', 'django.contrib.auth.views.login' , name='login'),
    url(r'^logout/', LogoutView.as_view(), name='logout'),
    url(r'^$', IndexView.as_view(), name='index'),
)
