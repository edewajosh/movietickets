from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movies.urls')),
    path('movies/', include('movies.urls')),
    path('logout/', LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
