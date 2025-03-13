from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Supervisor, Employees, WorkOrder, AdvanceOt, Items, AdvanceItem, Tasks, ItemTasks, ActivityRecord, EmployeeProgress

class SupervisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supervisor
        fields = '__all__'
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

class WorkOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrder
        fields = '__all__'

class AdvanceOtSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvanceOt
        fields = '__all__'

class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'

class AdvanceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvanceItem
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'

class ItemTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemTasks
        fields = '__all__'

class ActivityRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityRecord
        fields = '__all__'

class EmployeeProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeProgress
        fields = '__all__'