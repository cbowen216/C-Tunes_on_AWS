from django.urls import path
from artists import views as artist_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', artist_views.index.as_view(), name='home'),
    path('api/artists/', artist_views.Artist_list),
    path('api/artists/<int:pk>/', artist_views.Artist_detail),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
