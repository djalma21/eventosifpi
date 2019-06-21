from django.contrib import admin
from .models import Evento, Tipo, Inscricao

admin.site.register(Evento)
admin.site.register(Tipo)
admin.site.register(Inscricao)
