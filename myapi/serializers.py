from .models import Hero
from rest_framework import serializers

class HeroSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields=('name','alias')