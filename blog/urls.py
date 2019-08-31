from django.urls import path, include, reverse
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from blog.views import login,join, eventcreate

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'blog', BlogViewSet)


app_name = 'blog'

urlpatterns = [
    path('passchform/', password_change_form, name="password_change"),
    path('logout/', logout, name="logout"),
    path('userevent/', event_user_page, name="event_user"),
    path('create/', EventCreate.as_view(), name="create_event"),
    path('register/', register, name="reg"),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', BlogViews, name='home'),
    path('blog/<slug:slug>/', BlogDetail, name='detail'),
    path('signup/', SignUp, name='signup'),
    path('success/', Success, name='success'),
    path('contact/', Contact, name='contact'),
    path('login/', login, name="login"),
    path('esas/', login_required, name="login"),
    path('join/', join, name="joinevent")
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)