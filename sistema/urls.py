"""
URL configuration for sistema project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls import handler403

# Define o caminho para uma nova view customizada para o erro 403 - Acesso negado
handler403 = 'cadastros.views.acesso_negado_usuario'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cadastros.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('vendas/', include('vendas.urls')),
]
