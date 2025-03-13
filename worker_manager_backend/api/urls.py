from django.urls import path
from .views import SupervisorView, EmployesView, WorkOrderView, ItemsView, TasksView

urlpatterns = [
    path('worker_manager/supervisor', SupervisorView.as_view(), name='supervisors'),
    path('worker_manager/employees', EmployesView.as_view(), name='employees'),
    path('worker_manager/employees/<int:id>', EmployesView.as_view(), name='employees-details'),
    path('worker_manager/work-order', WorkOrderView.as_view(), name='works-orders'),
    path('worker_manager/work-order/<int:id>', WorkOrderView.as_view(), name='workorder-details'),
    path('worker_manager/items', ItemsView.as_view(), name='items'),
    path('worker_manager/items/<int:id>', ItemsView.as_view(), name='items-details'),
    path('worker_manager/tasks', TasksView.as_view(), name='tasks'),
]