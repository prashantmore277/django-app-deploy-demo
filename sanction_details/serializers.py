from rest_framework import serializers
from .models import  SanctionDetails, SanctionLetters,TrnDetails

class SanctionDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SanctionDetails
        fields = '__all__'


class SanctionLettersSerializer(serializers.ModelSerializer):
    class Meta:
        model = SanctionLetters
        fields = '__all__'


class TrnDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrnDetails
        fields = '__all__'

        