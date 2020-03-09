from rest_framework import serializers
from .models import Interaction,Herb,Drug

class InteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interaction
        fields = ['nom_plante','effets_plante','intensite_plante','nom_med','effets_med','intensite_med','consequence']

class HerbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Herb
        fields = ['nom_herb']

class DrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = ['nom_drug']