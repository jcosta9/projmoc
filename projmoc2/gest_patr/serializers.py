from rest_framework import serializers
from .models import Bem, Uge, Ugb, Sector, SubSector, Fornecedor

class BemSerializer(serializers.ModelSerializer):

    class Meta:

        model = Bem
        fields = '__all__'

class UgeSerializer(serializers.ModelSerializer):

    class Meta:

        model = Uge
        fields = '__all__'

class UgbSerializer(serializers.ModelSerializer):

    class Meta:

        model = Ugb
        fields = '__all__'

class SectorSerializer(serializers.ModelSerializer):

    class Meta:

        model = Sector
        fields = '__all__'

class SubsectorSerializer(serializers.ModelSerializer):

    class Meta:

        model = SubSector
        fields = '__all__'

class FornecedorSerializer(serializers.ModelSerializer):

    class Meta:

        model = Fornecedor
        fields = '__all__'
