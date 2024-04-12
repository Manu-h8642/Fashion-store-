from django.urls import path
from frontend import views

urlpatterns = [
    path('',views.homep,name="homep"),
    path('store/',views.store,name="store"),
    path('searchitem/',views.searchitem,name="searchitem"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('blog/',views.blog,name="blog"),
    path('fstore/<cn>/',views.fstore,name="fstore"),
    path('itemd/<int:itemid>', views.itemd, name="itemd"),
    path('csave/', views.csave, name="csave"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('usave/', views.usave, name="usave"),
    path('ulogin/',views.ulogin,name="ulogin"),
    path('ulogout/', views.ulogout, name="ulogout"),
    path('savecart/', views.savecart, name="savecart"),
    path('cartpage/', views.cartpage, name="cartpage"),
    path('deletecart/<int:did>/', views.deletecart, name="deletecart"),
    path('checkout/', views.checkout, name="checkout"),
    path('savecheck/', views.savecheck, name="savecheck"),
    path('wishlist/<int:itemid>/', views.wishlist, name="wishlist"),
    path('wishlistv/', views.wishlistv, name="wishlistv"),
    path('witemdetails/<int:itemid>/', views.witemdetails, name="witemdetails"),
    path('deletewish/<int:itemid>/', views.deletewish, name="deletewish"),
]