from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import generics


# from django.contrib.auth.decorators import login_required
from .models import Bem, Uge, Ugb, Sector, SubSector, Fornecedor
from django.utils import timezone
from .forms import BemForm, UgeForm, UgbForm, SectorForm, SubSectorForm, FornecedorForm
from .serializers import BemSerializer, UgeSerializer, UgbSerializer, SectorSerializer, SubsectorSerializer, FornecedorSerializer

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
    login_url = '/login/'
    redirect_field_name = 'bem_detalhe.html'

    form_class = BemForm
    model = Bem

class BemUpdateView(UpdateView):
    login_url = '/login/'
    redirect_field_name = 'bem_detalhe.html'

    form_class = BemForm

    model = Bem

class BemDeleteView(DeleteView):
    model = Bem
    success_url = reverse_lazy('gest_patr:bens_lista')

class BemList(generics.ListCreateAPIView):

    queryset = Bem.objects.all()
    serializer_class = BemSerializer

class BemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bem.objects.all()
    serializer_class = BemSerializer

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
    login_url = '/login/'
    redirect_field_name = 'uge_detalhe.html'

    form_class = UgeForm
    model = Uge

class UgeUpdateView(UpdateView):
    login_url = '/login/'
    redirect_field_name = 'uge_detalhe.html'

    form_class = UgeForm

    model = Uge

class UgeDeleteView(DeleteView):
    model = Uge
    success_url = reverse_lazy('gest_patr:uge_lista')

class UgeList(generics.ListCreateAPIView):

    queryset = Uge.objects.all()
    serializer_class = UgeSerializer

class UgeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Uge.objects.all()
    serializer_class = UgeSerializer

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
    login_url = '/login/'
    redirect_field_name = 'ugb_detalhe.html'

    form_class = UgbForm
    model = Ugb

class UgbUpdateView(UpdateView):
    login_url = '/login/'
    redirect_field_name = 'ugb_detalhe.html'

    form_class = UgbForm

    model = Ugb

class UgbDeleteView(DeleteView):
    model = Ugb
    success_url = reverse_lazy('gest_patr:ugb_lista')

class UgbList(generics.ListCreateAPIView):

    queryset = Ugb.objects.all()
    serializer_class = UgbSerializer

class UgbDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ugb.objects.all()
    serializer_class = UgbSerializer

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
    login_url = '/login/'
    redirect_field_name = 'sector_detalhe.html'

    form_class = SectorForm
    model = Sector

class SectorUpdateView(UpdateView):
    login_url = '/login/'
    redirect_field_name = 'sector_detalhe.html'

    form_class = SectorForm

    model = Sector

class SectorDeleteView(DeleteView):
    model = Sector
    success_url = reverse_lazy('gest_patr:sector_lista')

class SectorList(generics.ListCreateAPIView):

    queryset = Sector.objects.all()
    serializer_class = SectorSerializer

class SectorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer

##########################################################
##  SubSector
##########################################################

class SubSectorListView(ListView):
    model = SubSector

    def get_queryset(self):
        return SubSector.objects.order_by('cod')

class SubSectorDetailView(DetailView):
    model = SubSector

class CreateSubSectorView(CreateView):
    login_url = '/login/'
    redirect_field_name = 'subsector_detalhe.html'

    form_class = SubSectorForm
    model = SubSector

class SubSectorUpdateView(UpdateView):
    login_url = '/login/'
    redirect_field_name = 'subsector_detalhe.html'

    form_class = SubSectorForm

    model = SubSector

class SubSectorDeleteView(DeleteView):
    model = SubSector
    success_url = reverse_lazy('gest_patr:subsector_lista')

class SubSectorList(generics.ListCreateAPIView):

    queryset = SubSector.objects.all()
    serializer_class = SubsectorSerializer

class SubSectorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubSector.objects.all()
    serializer_class = SubsectorSerializer

##########################################################
##  Fornecedor
##########################################################

class FornecedorListView(ListView):
    model = Fornecedor

    def get_queryset(self):
        return Fornecedor.objects.order_by('nuit')

class FornecedorDetailView(DetailView):
    model = Fornecedor

class CreateFornecedorView(CreateView):
    login_url = '/login/'
    redirect_field_name = 'fornecedor_detalhe.html'

    form_class = FornecedorForm
    model = Fornecedor

class FornecedorUpdateView(UpdateView):
    login_url = '/login/'
    redirect_field_name = 'fornecedor_detalhe.html'

    form_class = FornecedorForm

    model = Fornecedor

class FornecedorDeleteView(DeleteView):
    model = Fornecedor
    success_url = reverse_lazy('gest_patr:fornecedor_lista')

class FornecedorList(generics.ListCreateAPIView):

    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer

class FornecedorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer
