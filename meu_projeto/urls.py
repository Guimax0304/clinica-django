"""
URL configuration for meu_projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import reverse_lazy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls', namespace='usuarios')),  # URLs do app 'usuarios'
    path('pacientes/', include('pacientes.urls', namespace='pacientes')),
    path('profissionais/', include('profissionais.urls', namespace='profissionais')),
    path('procedimentos/', include('procedimentos.urls', namespace='procedimentos')),
    path('salas/', include('salas.urls', namespace='salas')),
    path('contas/', include('django.contrib.auth.urls')),  # URLs padrão de autenticação do Django
    path('agendamentos/', include('agendamentos.urls', namespace='agendamentos')),  # URLs de agendamentos
    path('cadastros/', include('cadastros.urls', namespace='cadastros')),
    path('home/', include('home.urls', namespace='home')),  # Rota para o app home
    path('', RedirectView.as_view(pattern_name='usuarios:login', permanent=False)),  # Redireciona para login
]

# Servir arquivos estáticos em modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
