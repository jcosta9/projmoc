from django.shortcuts import render
from .models import Uge, Ugb, Sector, TipoAquisicao, Fornecedor, BemMovel
from .forms import UgeForm, UgbForm, SectorForm, TipoAquisicaoForm, FornecedorForm, BemMovelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (TemplateView, ListView, DetailView,
                                    CreateView, UpdateView,DetailView)
# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'

@login_required
class ListaBensMoveisView(ListView):
    model = BemMovel

    def get_queryset(self):
        return BemMovel.objects.order_by('codClassificacaoGeral','numOrdem')

@login_required
class BemMovelDetalheView(DetailView):
    model = BemMovel

@login_required
class BemMovelCriarView(LoginRequiredMixin, CreateView):
    login_url = '/login'
    redirect_field_name = 'gestao_patrimonio/bemmovel_detalhe.html'
    form_class = BemMovelForm
    model = BemMovel

@login_required
class BemMovelAtualizarView(LoginRequiredMixin, UpdateView):
    login_url = '/login'
    redirect_field_name = 'gestao_patrimonio/bemmovel_detalhe.html'
    form_class = BemMovelForm
    model = BemMovel

@login_required
class BemMovelDeleteView(LoginRequiredMixin,DetailView):
    model = BemMovel
    success_url = reverse_lazy('BensMoveisLista')
