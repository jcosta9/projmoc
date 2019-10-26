from django import forms

from .models import Bem, Uge, Ugb, Sector, TipoAquisicao

class UgeForm(forms.ModelForm):

    class Meta:
        model = Uge
        fields = ('cod','designacoes')

class UgbForm(forms.ModelForm):

    class Meta:
        model = Ugb
        fields = ('cod','designacoes')

class SectorForm(forms.ModelForm):

    class Meta:
        model = Sector
        # Entender como mudar o nome desses campos no formulário
        fields = ('cod',
                    'nome',
                    'ugb',
                    'provincia',
                    'distrito',
                    'postAdmin',
                    'localidade',
                    'classificadorTerr',
                    'bairro',
                    'endereco')

class TipoAquisicaoForm(forms.ModelForm):

    class Meta:
        model = TipoAquisicao
        fields = ('cod','tipo')

class BemForm(forms.ModelForm):

    class Meta:
        model = Bem
        fields = ('nome','marca', 'valor','uge','ugb', 'sector','tipoAquisicao')

# Caso queira mudar o CSS da classe de algum campo específico do formulário.
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'textinputclass'}),
        #     'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        # }
