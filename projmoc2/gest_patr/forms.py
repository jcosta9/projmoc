from django import forms

from .models import Bem, Uge, Ugb

class UgeForm(forms.ModelForm):

    class Meta:
        model = Uge
        fields = ('cod','designacoes')

class UgbForm(forms.ModelForm):

    class Meta:
        model = Ugb
        fields = ('cod','designacoes')

class BemForm(forms.ModelForm):

    class Meta:
        model = Bem
        fields = ('nome','marca', 'valor','uge','ugb')

# Caso queira mudar o CSS da classe de algum campo específico do formulário.
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'textinputclass'}),
        #     'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        # }
