from django.forms import ModelForm
from .models import Inscricao, Evento, Submissao

class InscricaoForm(ModelForm):
    class Meta:
        model = Inscricao
        fields = ['nome', 'sobrenome', 'cpf', 'email', 'evento']


class EventoForm(ModelForm):
    class Meta:
        model = Evento
        fields = ['foto','nome', 'tipo', 'data_inicial', 'data_final', 'local']

class SubmissaoForm(ModelForm):
    class Meta:
        model = Submissao
        fields = ['nome', 'cpf', 'email', 'evento', 'descricao', 'trabalho']