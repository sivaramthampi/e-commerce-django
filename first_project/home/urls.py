from django.urls import path
from . import views
urlpatterns = [
    path("call", views.call),
    path("db",views.dbitemsdisp),
    path("productdetail/<str:reqid>",views.product),
    path("addtocart",views.addtocart),
    path("mycart",views.viewcart),
    path("jgetdata",views.jgetdata),
    path("search",views.search),
    path("contain/<str:val>",views.getdata),
    path("plotter",views.plotter)
]