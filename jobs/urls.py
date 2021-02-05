from django.urls import path
from jobs import views
# from django.conf.urls.static import static

urlpatterns = [
    path('<int:job_id>', views.detail, name='detail'),
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
