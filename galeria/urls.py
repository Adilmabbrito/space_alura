from django.urls import path
from galeria.views import index, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', include('galeria.urls')),
]
