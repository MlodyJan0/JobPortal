from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from User.views import loginRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  loginRedirect, name='redirect'),
    path('company/', include("Company.urls")),
    path('users/', include("django.contrib.auth.urls")),
    path('users/', include("User.urls")),
    path('offers/', include("JobOffer.urls"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()