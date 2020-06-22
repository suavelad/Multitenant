from rest_framework.routers import DefaultRouter
from django.conf.urls import url
from .api import AdminUserViewSet,AdminUserView

router=DefaultRouter()
router.register(r'admins', AdminUserViewSet)
urlpatterns = router.urls

urlpatterns += [

    url(r'all_admins/$',AdminUserView.as_view()),
]

