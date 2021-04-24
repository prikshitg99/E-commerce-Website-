from django.urls import path
from.import views

urlpatterns = [
    path('', views.index, name="ShopHome"),
    path("about/", views.about, name="About Us"),
    path("contact/", views.contact, name="Contact Us"),
    path("tracker/", views.tracker, name="Track us"),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>", views.productview, name="product view"),
    path("checkout/", views.checkout, name="checkout"),
]