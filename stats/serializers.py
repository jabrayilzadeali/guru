from rest_framework import serializers
from .models import TeacherFinancialOverview


class TeacherFinancialOverviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherFinancialOverview
        fields = "__all__"
        extra_kwargs = {"instructors": {"read_only": True}}
        
