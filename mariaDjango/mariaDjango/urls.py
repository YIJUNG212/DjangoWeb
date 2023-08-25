"""
URL configuration for webpro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

#要使用動態upload的media,必須調用下列的方法
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('seric/admin/', admin.site.urls),
    path("seric/base",views.base),
    path("css_index",views.css_index),
    path("seric/index",views.index),
    path("seric/api/vip",views.vip),
    path("seric/vip_register",views.vip_register),
    path("seric/api/vip_user_add",views.vip_user_add),
    path("seric/webuser_showfield",views.webuser_showfield),
    path("seric/webuser_get_all",views.webuser_get_all),
    path("seric/webuser_admin",views.webuser_admin),
    path("seric/webuser/<str:id>/update/<str:mode>",views.webuser_update),
    path("seric/webuser/<str:id>/delete/<str:mode>",views.webuser_delete),
    path("seric/set_cookie/<str:key>/<str:value>",views.set_cookie),
    path("seric/get_cookie/<str:key>",views.get_cookie),
    path("seric/get_cookie_all",views.get_cookie_all),
    path("seric/set_cookie_time/<str:key>/<str:value>",views.set_cookie_time),
    path("seric/del_cookie/<str:key>",views.del_cookie),
    path("seric/set_session/<str:key>/<str:value>",views.set_session),
    path("seric/get_session/<str:key>",views.get_session),
    path("seric/get_session_all",views.get_session_all),
    path("seric/del_session/<str:key>",views.del_session),
    path("seric/login",views.login),
    path("seric/logout",views.logout),
    path("seric/login2",views.login2),
    path("seric/login3",views.login3),
    path("seric/accounts/index",views.index_django),
    path('seric/register_django', views.sign_up, name='Register'),
    path("seric/accounts/login",views.sign_in),
    path("seric/logout_django",views.log_out_django),
    path("seric/test",views.test),
    path("seric/upload_image", views.upload_product_sql),
    path("seric/upload_show",views.upload_show),
    path("seric/shopitem",views.get_shopitem),
    path("seric/product_buy",views.product_buy),
    path("seric/product_select/<str:id>",views.buy_select),
    path("seric/shopcar",views.shopcar_add),
    path("seric/shopcar_show",views.shopcar_show),
    path("seric/shopitem_action",views.shopitem_action),
    path("seric/api_test",views.api_test),
    path("seric/api_webUser_get",views.api_webUser_get),
    path("seric/api_webuser_getall/<str:userid>",views.api_webuser_getall),
    path("seric/api_product_getall/<str:userid>",views.api_product_getall),
    path("seric/worldmap",views.worldmap),
    path("seric/mp3",views.download_mp3),
    path("seric/mp4",views.download_mp4),
    path("seric/mp3_open/<str:mp3Url>",views.mp3),
    path("seric/mp4_open/<str:mp4Url>",views.mp4),
    path("seric/av_url/<str:av>",views.av),
    path("seric/av",views.av_download),
    path('seric/download_complete/', views.download_complete, name='download_complete'),
    path("seric/index_1",views.index_1),

    
   
    
  


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



