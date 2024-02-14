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
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('cadastros/', views.cadastros, name='cadastros'),
    path('cadastros/novo_cadastro', views.novo_cadastro, name='novo_cadastro'),
    path('cadastros/deletar_cadastro/<int:cadastro_id>', views.deletar_cadastro, name='deletar_cadastro'),
    path('cadastros/editar_cadastro/<int:cadastro_id>', views.editar_cadastro, name='editar_cadastro'),
    path('pesquisa', views.resultado_pesquisa, name='pesquisa'),
]
