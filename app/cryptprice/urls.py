from django.conf.urls import url

from cryptprice.views import CryptoPriceView

urlpatterns = [url(r"^price/", CryptoPriceView.as_view())]
