from django.contrib import admin
from django.urls import include, path
from front.views import home, search, basics, set_lang
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('admin/', admin.site.urls),

    path('set_lang/(?P<lang>[\w\-]+)', set_lang, name="set_lang"),

    path('', home, name='home'),
    path('search', search, name='search'),
    path('basics', search, name='basics'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
