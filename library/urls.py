from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

import authors.views as author_views
import books.views as book_views
import genres.views as genre_views

router = DefaultRouter()
router.register(r'genre' , genre_views.GenreViewSet)
router.register(r'author', author_views.AuthorViewSet)
router.register(r'book', book_views.BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('schema/' , SpectacularAPIView.as_view() , name='schema'),
    path('schema/docs', SpectacularSwaggerView.as_view(url_name="schema"))
]
