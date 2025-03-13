from rest_framework.views import APIView
from rest_framework.parsers import FormParser
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Supervisor, Employees, WorkOrder, Items, Tasks, ItemTasks
from .serializers import SupervisorSerializer, EmployeesSerializer, WorkOrderSerializer, ItemsSerializer, TaskSerializer

class SupervisorView(APIView):
    def get(self, request):
        supervisors = Supervisor.objects.all()
        serializer = SupervisorSerializer(supervisors, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = SupervisorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EmployesView(APIView):
    def get(self, request, id=None):
        if id:
            employee = get_object_or_404(Employees, id=id)
            serializer =  EmployeesSerializer(employee).data
            items = Items.objects.filter(employees=employee).values_list("item_number", flat=True)
            workorder = WorkOrder.objects.filter(employees=employee).values_list("ot_number", flat=True)
            serializer["ot"] = list(workorder) if workorder else None
            serializer['items'] = list(items) if items else None
            return Response({
                'employee': serializer
            })
        else:    
            employees = Employees.objects.all()
            serializer = EmployeesSerializer(employees, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = EmployeesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class WorkOrderView(APIView):
    def get(self, request, id=None):
        if id:
            workorder = get_object_or_404(WorkOrder, id=id)
            serializer = WorkOrderSerializer(workorder).data
            employee = Employees.objects.filter(workorder=workorder).values_list("name", flat=True)
            items = Items.objects.filter(workorder=workorder).values_list("item_number", flat=True)
            serializer["employees"] = list(employee) if employee else None
            serializer["items"] = list(items) if items else None
            return Response({'ot': serializer})
        else:
            workorders = WorkOrder.objects.all()
            serializer = WorkOrderSerializer(workorders, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = WorkOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ItemsView(APIView):
    def get(self, request, id=None):
        if id:
            item = get_object_or_404(Items, id=id)
            serializer = ItemsSerializer(item).data
            serializer["ot"] = item.workorder.ot_number
            return Response({'item': serializer})
        else:  
            items = Items.objects.all()
            serializer = ItemsSerializer(items, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = ItemsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateItemTaskView(APIView):
    def patch(self, request, item_id, task_id):
        item_task = get_object_or_404(ItemTasks, item_id=item_id, task_id=task_id)
        new_state = request.data.get("state", None)

        if new_state not in ["Pendiente", "En progreso", "Finalizado"]:
            return Response({'error': "Estado no valido"}, status=400)
        
        item_task.state = new_state
        item_task.save()

        return Response({"message": "Estado actualizado correctamente", "new_state": item_task.state})

class TasksView(APIView):
    def get(self, request):
        tasks = Tasks.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)