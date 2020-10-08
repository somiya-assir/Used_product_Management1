"""Used_product_Management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
import django.contrib.auth.urls
from django.conf import settings
from django.conf.urls.static import static

from Seller import views as seller_views
from Buyer import views as buyer_views
from Sellercost import  views as sellercost_views
from Employee import views as employee_views
from Payment import views as pay_views
from pickup import views as pickup_views
from Usermanagement import views as user_views
from Usedproduct import views as product_views
from pickup import views as pickup_views
from Home import views as home_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('seller/',seller_views.showseller,name='sellerlist'),
    path('buyer/',buyer_views.buyerinfo,name='buyer'),
    path('showsellercost',sellercost_views.showsellercost,name='sellercost'),
    path('employee/',employee_views.employee,name='employee'),
    path('payment/',pay_views.showpayment,name='payment'),
    path('pickup/',pickup_views.pickUp,name='pickup'),

    path('sellerinsert/',seller_views.insertseller,name='insertseller'),
    path('registration',user_views.registration,name='registration'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('createprofile/', user_views.create_profile, name='create_profile'),
    path('viewprofile/', user_views.view_profile, name='view_profile'),
    path('showproduct/', product_views.showsproduct, name='show_product'),
    path('insertproduct/', product_views.insertpoduct, name='insert_product'),
    path('insertpickup/',pickup_views.insertpickup,name='insertpickup'),
    path('home/', home_views.showhome, name='home'),
    path('pricelist/', home_views.showpricelist, name='pricelist'),
    path('showproduct/<int:product_id>', product_views.showDetails, name='detail_views'),



]
if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
