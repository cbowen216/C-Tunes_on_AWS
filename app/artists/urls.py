from django.urls import path
from artist import views as artist_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', artists_views.index.as_view(), name='home'),
    path('api/artists/', artists_views.artist_list),
    path('api/artists/<int:pk>/', artists_views.artist_detail),
    path('api/artists/published/', artists_views.artist_list_published)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
