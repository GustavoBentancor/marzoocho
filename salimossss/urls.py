"""salimossss URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from iniciosalimos.views import cine_list, festi_list, detalle_festi_list, crio_list, gastro_list, detalle_gastro_list, teatro_list, toques_list, boli_list, artdep_list, conamigos_list, enfmilia_list,ninos_list, paseos_list,turismo_list, airlib_list, montevideo_eventos_list, montevideo_inicio_list, montevideo_lugares_list, rocha_eventos_list, rocha_inicio_list, rocha_lugares_list, detalle_eventos_list, detalle_lugares_list, Detalleenfamilia_list
from iniciosalimos.views import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('Cine', cine_list, name='Cinellama'),
    path('Festivales', festi_list, name='Festillama'),
    path('Criollas', crio_list, name='Criollama'),
    path('Gastronomia', gastro_list, name='Gastrollama'),
    path('Teatros', teatro_list, name='Teatrollama'),
    path('Toques', toques_list, name='Toquesllama'),
    path('Boliches',boli_list, name='Bolillama'),
    path('Artdep',artdep_list, name='Artdepllama'),
    path('EnFamilia', enfmilia_list, name='familia'),
    path('Conamigos', conamigos_list, name='amigos'),
    path('ninos', ninos_list, name='ninos'),
    path('paseos', paseos_list, name='paseo'),
    path('Turismo', turismo_list, name='turi'),
    path('airelibre', airlib_list, name='aire'),
    path('Montevideo_inicio', montevideo_inicio_list, name='montevideo_inicio'),
    path('Montevideo_eventos', montevideo_eventos_list, name='montevideo_eventos'),
    path('Montevideo_lugares', montevideo_lugares_list, name='montevideo_lugares'),
    path('Rocha_inicio', rocha_inicio_list, name='rocha_inicio'),
    path('Rocha_eventos', rocha_eventos_list, name='rocha_eventos'),
    path('Rocha_lugares', rocha_lugares_list, name='rocha_lugares'),
    path('Detalle_eventos', detalle_eventos_list, name='detalle_eventos'),
    path('Detalle_lugares', detalle_lugares_list, name='detalle_lugares'),
    path('Detalle_Gastronomia', detalle_gastro_list, name='Detalle_Gastronomia'),
    path('Detalle_Festivales', detalle_festi_list, name='Detalle_Festivales'),
    path('Detalle_Enfamilia', Detalleenfamilia_list, name='Detalle_enfamilia'),
]
