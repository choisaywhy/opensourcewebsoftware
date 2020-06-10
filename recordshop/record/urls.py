from django.urls import path, include
from record import views
urlpatterns = [
    path('', views.main, name="main"),

    path('login/', views.login, name="login"),
    path('join/', views.join, name="join"),
    path('reset_account/',views.reset_account, name="reset_account"),

    path('pop_hiphop/', views.pop_hiphop, name="pop_hiphop"),
    path('pop_rnb/', views.pop_rnb, name="pop_rnb"),

    path('kpop_indi/', views.kpop_indi, name="kpop_indi"),
    path('kpop_hiphop/', views.kpop_hiphop, name="kpop_hiphop"),

    path('ost/', views.ost, name="ost"),

    path('cart/', views.cart, name="cart"),
    path('order/', views.order, name="order"),
    
]


