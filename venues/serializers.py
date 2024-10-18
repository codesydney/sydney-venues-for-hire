from rest_framework import serializers
from .models import VenuesForHire

class SydneyVenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = VenuesForHire
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.createdate is None:
            representation['createdate'] = None  # Handle null date gracefully
        if instance.modifieddate is None:
            representation['modifieddate'] = None  # Handle null date gracefully
        return representation
