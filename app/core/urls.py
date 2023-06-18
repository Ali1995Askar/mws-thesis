from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Basic
    path('', views.HomeView.as_view(), name='home'),
    path('contact-us/', views.ContactUsView.as_view(), name='contact-us'),
    path('faq/', views.FAQView.as_view(), name='f-a-q'),

    # Apps
    path('auth/', include('auth.urls')),
    path('tasks/', include('tasks.urls')),
    path('workers/', include('workers.urls')),
    path('accounts/', include('accounts.urls')),
    path('management/', include('management.urls')),

]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
