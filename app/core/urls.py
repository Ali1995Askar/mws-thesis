from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Basic
    path('', views.HomeView.as_view()),
    path('contact-us/', views.ContactUsView.as_view()),
    path('about-us/', views.AboutUsView.as_view()),
    # path('', AboutUs.as_view(), name="aboutus")
    # Apps
    # path('auth/', admin.site.urls),
    # path('management/', include('management.urls')),
    # path('tasks/', include('management.urls')),
    # path('workers/', include('management.urls')),

]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
