
from django.contrib import admin
from django.urls import include , path

#from django.conf.urls import  patterns, include, url

from django.conf.urls import include ,url

from django.contrib import admin

from django.urls import include, path


from . import views

'''urlpatterns = [

    url(r'^$',views.index),

    url(r'^(?P<Home_id>[0-9]+)/$',views.detail),

    #url(r'^[\w]+[<page_id>[0-9]]+/$',views.page_view_count)

     url(r'^[\w]+/(?P<page_id>[0-9]+)/$',views.page_view_count),  # correct url http://127.0.0.1:8000/Home/video_view/12/

     url(r'^[\d]+/[\w]+/(?P<video_id>[0-9]+)/$',views.video_view_count),  # correct url http://127.0.0.1:8000/Home/1/video_view/12/

     url(r'^/w+//d[0-9]/$',views.ad_impression)

    #url(r'^[\W]/[\w]+/(?P<ad_im>[0-9]+)/$',views.ad_impression)  #http://127.0.0.1:8000/Home/*/ad_imp/12/


]

#urlpatterns = path('', path(r'^ hello/', 'Home.views.hello', name = 'hello'),)


'''
urlpatterns = [

    path('devleopment_1', Home.views.index, name='index')
    #path('articles/<int:year>/', views.year_archive),
    #path('articles/<int:year>/<int:month>/', views.month_archive),
    #path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
]