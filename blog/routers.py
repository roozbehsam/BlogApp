from rest_framework import routers

from blog.post.viewsets import PostViewSet
from blog.user.viewsets import UserViewSet
from blog.auth.viewsets import RegisterViewSet, LoginViewSet, RefreshViewSet

router = routers.SimpleRouter()

# ################### AUTH
router.register(r'auth/register', RegisterViewSet, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')


# ################### USER
router.register(r'user', UserViewSet, basename='user')

# ################### POST
router.register(r'post', PostViewSet, basename='post')

urlpatterns = [
    *router.urls,
]