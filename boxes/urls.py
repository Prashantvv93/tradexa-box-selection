
from django.urls import path
from .views import recommend_shipping_box

urlpatterns = [
    path(
        "recommend/",
        recommend_shipping_box,
        name="recommend-shipping-box",
    ),
]
