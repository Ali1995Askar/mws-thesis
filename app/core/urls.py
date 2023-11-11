from . import views
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Basic
    path('', views.HomeView.as_view(), name='home'),
    path('faq/', views.FAQView.as_view(), name='f-a-q'),

    # Apps
    path('tasks/', include('tasks.urls')),
    path('workers/', include('workers.urls')),
    path('accounts/', include('accounts.urls')),
    path('management/', include('management.urls')),
    path('categories/', include('categories.urls')),
    path('educations/', include('educations.urls')),
    path('presentation', views.PresentationView.as_view(), name='presentation'),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
