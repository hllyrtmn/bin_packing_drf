from rest_framework import serializers

class BaseTrackingSerializer(serializers.ModelSerializer):
    created_by_username = serializers.SerializerMethodField(read_only=True)
    updated_by_username = serializers.SerializerMethodField(read_only=True)

    class Meta:
        abstract = True
        fields = [
            'created_at', 
            'updated_at', 
            'created_by', 
            'updated_by',
            'created_by_username',
            'updated_by_username'
        ]
        read_only_fields = [
            'created_at', 
            'updated_at', 
            'created_by', 
            'updated_by'
        ]

    def get_created_by_username(self, obj):
        return obj.created_by.username if obj.created_by else None

    def get_updated_by_username(self, obj):
        return obj.updated_by.username if obj.updated_by else None