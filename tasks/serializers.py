from rest_framework import serializers
from .models import Tasks

class TasksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ('id', 'titulo', 'descripcion', 'technology', 'created_at')
        read_only_fields = ('created_at', )