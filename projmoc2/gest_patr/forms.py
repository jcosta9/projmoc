from django import forms

from .models import Bem, Uge, Ugb, Sector, TipoAquisicao, Fornecedor

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

class FornecedorForm(forms.ModelForm):

    class Meta:
        model = Fornecedor
        fields = ('nome','nuit', 'enderecoFornecedor','cidade')

class BemForm(forms.ModelForm):

    class Meta:
        model = Bem
        fields = ('nome','marca', 'valor','uge','ugb', 'sector','tipoAquisicao', 'fornecedor')

# Caso queira mudar o CSS da classe de algum campo específico do formulário.
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'textinputclass'}),
        #     'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        # }
