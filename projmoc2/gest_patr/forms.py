from django import forms

from .models import Bem


class BemForm(forms.ModelForm):

    class Meta:
        model = Bem
        fields = ('nome','marca', 'valor',)

# Caso queira mudar o CSS da classe de algum campo específico do formulário.
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'textinputclass'}),
        #     'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        # }
