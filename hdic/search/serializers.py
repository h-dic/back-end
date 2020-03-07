from rest_framework import serializers
from .models import Interaction

class InteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interaction
        fields = ['nom_plante','effets_plante','intensite_plante','nom_med','effets_med','intensite_med','consequence']