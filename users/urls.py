from rest_framework.routers import DefaultRouter

from users.api import (AdminViewSet, CustomerAccountViewSet,
                       RegisterCustomerViewSet, TraderViewSet)

router = DefaultRouter()
router.register(r'admins', AdminViewSet, basename="admins")
router.register(r'traders', TraderViewSet, basename="traders")
router.register(r'customer-accounts',
                CustomerAccountViewSet, basename="customer-accounts")
router.register(r'register-customers',
                RegisterCustomerViewSet, basename='register-customers')

urlpatterns = router.urls
