from django.urls import path
from manu import views

urlpatterns = [
    path('index/',views.index,name="index"),
    path('categoryreg/',views.categoryreg,name="categoryreg"),
    path('save/',views.save,name="save"),
    path('disp/', views.disp, name="disp"),
    path('edit/<int:sid>/', views.edit, name="edit"),
    path('eupload/<int:sid>/', views.eupload, name="eupload"),
    path('creg/',views.creg,name="creg"),
    path('cupload/',views.cupload,name="cupload"),
    path('ctable/',views.ctable,name="ctable"),
    path('cedit/<int:cid>/',views.cedit,name="cedit"),
    path('cepload/<int:cid>/',views.cepload,name="cepload"),
    path('cdel/<int:cid>/',views.cdel,name="cdel"),
    path('sdel/<int:sid>/',views.sdel,name="sdel"),
    path('adlog/',views.adlog,name="adlog"),
    path('adlogin/',views.adlogin,name="adlogin"),
    path('adlogout/',views.adlogout,name="adlogout"),
    path('contv/',views.contv,name="contv"),
    path('cdel/<int:cid>/',views.cdel,name="cdel"),
]