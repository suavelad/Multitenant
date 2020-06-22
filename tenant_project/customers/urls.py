from rest_framework.routers import DefaultRouter
from django.conf.urls import url
from .api import UserViewSet,UserView

router=DefaultRouter()
router.register(r'users', UserViewSet)
urlpatterns = router.urls

urlpatterns += [

    url(r'all_users/$',UserView.as_view()),
]

