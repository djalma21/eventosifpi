from django.urls import path
from core.views import home, listar_inscritos, cadastrar_evento, fazer_inscricao, mostrar_evento

urlpatterns = [
    path('', home, name="home"),
    #path('listar_evento', listar_eventos, name="listar_evento"),
    path('listar_inscritos', listar_inscritos, name="listar_inscritos"),
    path('cadastrar/', cadastrar_evento, name="cadastrar_evento"),
    path('inscricao/', fazer_inscricao, name="fazer_inscricao"),
    path('mostrar/<int:id>/', mostrar_evento, name='mostrar_evento'),
]