from django import forms
import .models import Uge, Ugb, Sector, TipoAquisicao, Fornecedor, BemMovel

class UgeForm(forms.ModelForm):
    class Meta():
        model = Uge
        fields = ('cod','designacoes')
        widgets = {
            'cod':forms.TextInput(attrs={'class':'textinputclass'}),
            'designacoes':forms.TextInput(attrs={'class':'textinputclass'})
        }
class UgbForm(forms.ModelForm):
    class Meta():
        model = Ugb
        fields = ('cod','designacoes')
        widgets = {
            'cod':forms.TextInput(attrs={'class':'textinputclass'}),
            'designacoes':forms.TextInput(attrs={'class':'textinputclass'})
        }
class SectorForm(forms.ModelForm):
    class Meta():
        model = Sector
        fields = ('cod','nome','ugb','provincia','distrito','postAdmin','localicade','classificadoTerr','bairro','endereco')
        widgets = {
            'cod':forms.TextInput(attrs={'class':'textinputclass'}),
            'nome':forms.TextInput(attrs={'class':'textinputclass'}),
            'ugb':forms.TextInput(attrs={'class':'textinputclass'}),
            'provincia':forms.TextInput(attrs={'class':'textinputclass'}),
            'distrito':forms.TextInput(attrs={'class':'textinputclass'}),
            'postAdmin':forms.TextInput(attrs={'class':'textinputclass'}),
            'localicade':forms.TextInput(attrs={'class':'textinputclass'}),
            'classificadoTerr':forms.TextInput(attrs={'class':'textinputclass'}),
            'bairro':forms.TextInput(attrs={'class':'textinputclass'}),
            'endereco':forms.TextInput(attrs={'class':'textinputclass'})
        }
class AquisicaoForm(forms.ModelForm):
    class Meta():
        model = TipoAquisicao
        fields = ('cod','forma')
        widgets = {
            'cod':forms.TextInput(attrs={'class':'textinputclass'}),
            'forma':forms.TextInput(attrs={'class':'textinputclass'})
        }
class FornecedorForm(forms.ModelForm):
    class Meta():
        model = Fornecedor
        fields = ('nome','nuit','enderecoFornecedor','cidade')
        widgets = {
            'nome':forms.TextInput(attrs={'class':'textinputclass'}),
            'nuit':forms.TextInput(attrs={'class':'textinputclass'}),
            'enderecoFornecedor':forms.TextInput(attrs={'class':'textinputclass'}),
            'cidade':forms.TextInput(attrs={'class':'textinputclass'})
        }
class BemMovelForm(forms.ModelForm):
    class Meta():
        model = BemMovel
        fields = ('numOrdem','dataPreenchimento','uge','ugb','sector',
            'codClassificacaoGeral','designacao','marca','numeroSerie','NIP',
            'modelo','comprimento','largura','altura','cor','materialPredominante',
            'tipoAquisicao','estadoBem','dataAquisicao','valorAquisicao','fornecedor',
            'tipoComprovativo','nroComprovativo','assistenciaTecnica','garantia',
            'utilizador','observacoes','preenchidoPor','responsavel')
        widgets = {
            'numOrdem':forms.TextInput(attrs={'class':'textinputclass'}),
            'dataPreenchimento':forms.TextInput(attrs={'class':'textinputclass'}),
            'uge':forms.TextInput(attrs={'class':'textinputclass'}),
            'ugb':forms.TextInput(attrs={'class':'textinputclass'}),
            'sector':forms.TextInput(attrs={'class':'textinputclass'}),
            'codClassificacaoGeral':forms.TextInput(attrs={'class':'textinputclass'}),
            'designacao':forms.TextInput(attrs={'class':'textinputclass'}),
            'marca':forms.TextInput(attrs={'class':'textinputclass'}),
            'NIP':forms.TextInput(attrs={'class':'textinputclass'}),
            'numeroSerie':forms.TextInput(attrs={'class':'textinputclass'}forms.TextInput(attrs={'class':'textinputclass'})),
            'modelo':forms.TextInput(attrs={'class':'textinputclass'}),
            'comprimento':forms.TextInput(attrs={'class':'textinputclass'}),
            'largura':forms.TextInput(attrs={'class':'textinputclass'}),
            'altura':forms.TextInput(attrs={'class':'textinputclass'}),
            'cor':forms.TextInput(attrs={'class':'textinputclass'}),
            'materialPredominante':forms.TextInput(attrs={'class':'textinputclass'}),
            'tipoAquisicao':forms.TextInput(attrs={'class':'textinputclass'}),
            'estadoBem':forms.TextInput(attrs={'class':'textinputclass'}),
            'dataAquisicao':forms.TextInput(attrs={'class':'textinputclass'}),
            'valorAquisicao':forms.TextInput(attrs={'class':'textinputclass'}),
            'fornecedor':forms.TextInput(attrs={'class':'textinputclass'}),
            'tipoComprovativo':forms.TextInput(attrs={'class':'textinputclass'}),
            'nroComprovativo':forms.TextInput(attrs={'class':'textinputclass'}),
            'assistenciaTecnica':forms.TextInput(attrs={'class':'textinputclass'}),
            'garantia':forms.TextInput(attrs={'class':'textinputclass'}),
            'utilizador':forms.TextInput(attrs={'class':'textinputclass'}),
            'observacoes':forms.TextInput(attrs={'class':'textinputclass'}),
            'preenchidoPor':forms.TextInput(attrs={'class':'textinputclass'}),
            'responsavel':forms.TextInput(attrs={'class':'textinputclass'})
        }
