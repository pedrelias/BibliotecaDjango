from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name='index.html'),name = 'index'),
    path('consulta/',consulta, name='consultas'),
    path('reserva/',reserva,name='reservas'),
    path('autores/',autores,name='autores'),
    path('editoras/',editora,name='autores'),
    path('generos/',genero,name='generos'),
]
