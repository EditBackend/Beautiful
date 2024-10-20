from django.urls import path
from .views import index, about, client, contact, products, productdetailView,caruseldetailView,aboutdetailView
urlpatterns = [
    path('', index,name = "index"),
    path('about/', about, name = 'about'),
    path('client/', client, name = "client"),
    path('products/', products, name = "products"),
    path('contact/', contact, name="contact"),
    # --------------------------------deteils-------------------------

    path('product/<int:id>/', productdetailView, name = 'detail'),
    path('carusel/<int:id>/', caruseldetailView, name='carusel'),
    path('about/<int:id>/',aboutdetailView,  name = 'aboutdetail'),


    # --------------------------------deteils end-------------------------

]











