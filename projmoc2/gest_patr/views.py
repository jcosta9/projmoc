from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.decorators import login_required
from .models import Bem, Uge, Ugb, Sector
from django.utils import timezone
from .forms import BemForm, UgeForm, UgbForm, SectorForm

from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

from django.urls import reverse_lazy
# from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class AboutView(TemplateView):
    template_name = 'about.html'

class BemListView(ListView):
    model = Bem

    def get_queryset(self):
        return Bem.objects.filter(dataPreenchimento__lte=timezone.now()).order_by('-dataPreenchimento')

class BemDetailView(DetailView):
    model = Bem

class CreateBemView(CreateView):
    # login_url = '/login/'
    redirect_field_name = 'bem_detalhe.html'

    form_class = BemForm
    model = Bem

class BemUpdateView(UpdateView):
    # login_url = '/login/'
    redirect_field_name = 'bem_detalhe.html'

    form_class = BemForm

    model = Bem

class BemDeleteView(DeleteView):
    model = Bem
    success_url = reverse_lazy('gest_patr:bens_lista')


##########################################################
##  Uge
##########################################################

class UgeListView(ListView):
    model = Uge

    def get_queryset(self):
        return Uge.objects.order_by('cod')

class UgeDetailView(DetailView):
    model = Uge

class CreateUgeView(CreateView):
    # login_url = '/login/'
    redirect_field_name = 'uge_detalhe.html'

    form_class = UgeForm
    model = Uge

class UgeUpdateView(UpdateView):
    # login_url = '/login/'
    redirect_field_name = 'uge_detalhe.html'

    form_class = UgeForm

    model = Uge

class UgeDeleteView(DeleteView):
    model = Uge
    success_url = reverse_lazy('gest_patr:uge_lista')

##########################################################
##  Ugb
##########################################################

class UgbListView(ListView):
    model = Ugb

    def get_queryset(self):
        return Ugb.objects.order_by('cod')

class UgbDetailView(DetailView):
    model = Ugb

class CreateUgbView(CreateView):
    # login_url = '/login/'
    redirect_field_name = 'ugb_detalhe.html'

    form_class = UgbForm
    model = Ugb

class UgbUpdateView(UpdateView):
    # login_url = '/login/'
    redirect_field_name = 'ugb_detalhe.html'

    form_class = UgbForm

    model = Ugb

class UgbDeleteView(DeleteView):
    model = Ugb
    success_url = reverse_lazy('gest_patr:ugb_lista')


##########################################################
##  Sector
##########################################################

class SectorListView(ListView):
    model = Sector

    def get_queryset(self):
        return Sector.objects.order_by('cod')

class SectorDetailView(DetailView):
    model = Sector

class CreateSectorView(CreateView):
    # login_url = '/login/'
    redirect_field_name = 'sector_detalhe.html'

    form_class = SectorForm
    model = Sector

class SectorUpdateView(UpdateView):
    # login_url = '/login/'
    redirect_field_name = 'sector_detalhe.html'

    form_class = SectorForm

    model = Sector

class SectorDeleteView(DeleteView):
    model = Sector
    success_url = reverse_lazy('gest_patr:sector_lista')
