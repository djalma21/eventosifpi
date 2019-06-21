from django.urls import path
from .views import home, listar_inscritos, cadastrar_evento, fazer_inscricao, mostrar_evento, submeter_trabalho,\
    listar_trabalhos,alterar_evento, alterar_inscricao, alterar_trabalho_submetido, deletar_evento, deletar_inscricao, \
    deletar_trabalho

urlpatterns = [
    path('', home, name="home"),
    #path('listar_evento', listar_eventos, name="listar_evento"),
    path('listar_inscritos', listar_inscritos, name="listar_inscritos"),
    path('listar_trabalho', listar_trabalhos, name="trabalhos"),
    path('cadastrar/', cadastrar_evento, name="cadastrar_evento"),
    path('inscricao/', fazer_inscricao, name="fazer_inscricao"),
    path('submeter/', submeter_trabalho, name="submeter"),
    path('mostrar/<int:id>/', mostrar_evento, name='mostrar_evento'),
    path('alterar_evennto/<int:id>/', alterar_evento, name='alterar_evento'),
    path('alterar_inscricao/<int:id>/', alterar_inscricao, name='alterar_inscricao'),
    path('alterar_trabalho/<int:id>/', alterar_trabalho_submetido, name='alterar_trabalho'),
    path('deletar_evento/<int:id>/', deletar_evento, name='deletar_evento'),
    path('deletar_inscricao/<int:id>/', deletar_inscricao, name='deletar_inscricao'),
    path('deletar_trabalho/<int:id>/', deletar_trabalho, name='deletar_trabalho'),
]