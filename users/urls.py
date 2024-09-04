from django.urls import path
from rest_framework.routers import DefaultRouter

from users.api import (AdminViewSet, CustomerAccountViewSet,
                       RegisterCustomerAPIView, TraderViewSet)

router = DefaultRouter()
router.register(r'admins', AdminViewSet, basename="admins")
router.register(r'traders', TraderViewSet, basename="traders")
router.register(r'customer-accounts',
                CustomerAccountViewSet, basename="customer-accounts")

urlpatterns = router.urls
urlpatterns += [
    path('register-customers/',
         RegisterCustomerAPIView.as_view(), name='register-customers'),
]
