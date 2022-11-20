"""proyectofinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    # De la siguiente forma ya no es necesario colocar core/ antes de las búsquedas
    path('', include('core.urls')),
    # urls contact
    path('contact/', include('contact.urls')),
    # urls biography
    path('biography/', include('biography.urls')),
    # urls gallery
    path('gallery/', include('gallery.urls')),
    # Si colocamos de esta forma 0path('core/', include('core.urls')),
    # tendremos que especificar primero core/gallery por ejemplo.
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
