from django.contrib import admin
from django.urls import include, path
from django_distill import distill_path
from front.views import test
from django.conf import settings
from django.conf.urls.static import static


def get_index():
    return None


urlpatterns = [
    path('admin/', admin.site.urls),
    distill_path('', test, name='index', distill_func=get_index, distill_file='index.html'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
