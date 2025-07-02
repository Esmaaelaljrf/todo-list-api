from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'  # ممكن نخصص الحقول لاحقًا حسب الأمان
        read_only_fields = ['owner', 'created_at']
