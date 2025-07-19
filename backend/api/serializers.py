from rest_framework import serializers
from .models import Session
from .services.scheduling import has_conflicting_students


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'  # You can customize later

    def validate(self, data):
        students = data.get('students')

        # Defensive check if 'students' is present
        if students and has_conflicting_students(students):
            raise serializers.ValidationError(
                "Some students are incompatible with each other and cannot be scheduled together.")

        return data
