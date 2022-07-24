from django.urls import path
from artists import views as artist_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', artist_views.index.as_view(), name='home'),
    path('api/artists/', artist_views.artist_list),
    path('api/artists/<int:pk>/', artist_views.artist_detail),
    path('api/artists/published/', artist_views.artist_list_published)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
