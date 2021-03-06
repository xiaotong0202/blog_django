from django.conf.urls import url
from apps.blog_sign import views

urlpatterns = [
    url(r'^login$', views.LoginView.as_view(), name='login'),
    url(r'^register$', views.Register.as_view(), name='register'),
    url(r'^forget$', views.ForgetView.as_view(), name='forget'),
    url(r'^active/(?P<token>.*)$', views.ActiveView.as_view(), name='active'),
    url(r'^sendemail$', views.send_email, name='sendemail'),
    url(r'^logout$', views.user_logout, name='logout'),
]
