from rest_framework import serializers
from.models import BucketList

class BucketSerializer(serializers.ModelSerializer):
    """This serializer converts model in JSON, so it can be used by api"""
    
    class Meta:
        """meta class to be used to define field mappings"""
        model = BucketList
        fields = ('id', 'name', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')
