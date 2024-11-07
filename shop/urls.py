"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.urls import path
from django.conf import settings

from detailShop import views
from detailShop.views import Index, delivery, about, search

urlpatterns = [
    path('', views.Index.as_view(), name = 'index'),
    path('admin/', admin.site.urls),


    path('detail_list/', views.DetailList.as_view(), name = 'detail_list'),
    path('detail/<int:pk>/', views.DetailDetail.as_view(), name ='detail_detail'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('delivery/', delivery, name = 'delivery'),
    path('about/', about, name='about'),
    path('search/', search, name='search'),
    path('create_order', views.OrderCreate.as_view(), name='create_order'),
    path('order_list', views.OrderList.as_view(), name='order_list'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)