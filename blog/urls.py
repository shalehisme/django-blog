from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aboutme/', include('aboutme.urls')),
    path('', include('posts.urls'))
]
