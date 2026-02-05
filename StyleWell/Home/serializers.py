from rest_framework import serializers
from .models import Lookbook

class LookbookSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Lookbook
        fields = ['id', 'user', 'title', 'image', 'image_url', 'uploaded_at']
        read_only_fields = ['user', 'uploaded_at']
    
    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None