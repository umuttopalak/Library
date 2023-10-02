from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

from .app import views

router = DefaultRouter()
router.register(r'genre' , views.GenreViewSet)
router.register(r'author', views.AuthorViewSet)
router.register(r'book', views.BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('schema/' , SpectacularAPIView.as_view() , name='schema'),
    path('schema/docs', SpectacularSwaggerView.as_view(url_name="schema"))
]
