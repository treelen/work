
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.settings.urls')),
    path('users/', include('apps.users.urls')),
    path('blog/', include('apps.blog.urls')),
    path('contacts/', include('apps.contacts.urls')),
    
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)