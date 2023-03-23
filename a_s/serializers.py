from rest_framework import serializers
from a_s.models import AutoSys

class AsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoSys
        fields = ('id', 'autosys')
