from django.conf.urls import url

from . import views
urlpatterns = [

    #par_get函数的路由
     #url(r"^par_get/$", views.par_get),
    # url(r'^par_get/(?P<addr>+)/(?P<port>+)/(?P<cmd>\d+)/$', views.par_get),
    url(r'^get_json/$', views.get_json)

    
    ]