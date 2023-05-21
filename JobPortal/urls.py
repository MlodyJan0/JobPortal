
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',  loginRedirect, name='redirect'),
    # path('company/', include("apps.company.urls")),
    # path('users/', include("django.contrib.auth.urls")),
    # path('users/', include("apps.user.urls")),
    # path('offers/', include("apps.joboffer.urls"))
]