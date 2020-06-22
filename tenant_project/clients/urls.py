from rest_framework.routers import DefaultRouter
from django.conf.urls import url
from .api import AdminUserViewSet,AdminUserView,ClientViewSet,DomainViewSet

router=DefaultRouter()
router.register(r'admins', AdminUserViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'domain', DomainViewSet)
urlpatterns = router.urls

urlpatterns += [

    url(r'all_admins/$',AdminUserView.as_view()),
]

