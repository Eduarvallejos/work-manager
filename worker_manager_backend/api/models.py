from django.db import models

# Create your models here.

class Supervisor(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    registration_date = models.DateTimeField(auto_now_add=True)

class Employees(models.Model):
    name = models.CharField(max_length=255)
    dni = models.CharField(max_length=8, unique=True)
    password = models.CharField(max_length=255)
    active_user = models.BooleanField(default=False)
    registration_date = models.DateTimeField(auto_now_add=True)

class WorkOrder(models.Model):
    ot_number = models.CharField(max_length=20, unique=True)
    empresa = models.CharField(max_length=255)
    state = models.CharField(max_length=50, choices=[('Pendiente', 'Pendiente'), ('En Progreso', 'En Progreso'), ('Finalizado', 'Finalizado')], default='Pendiente')
    registration_date = models.DateTimeField(auto_now_add=True)
    employees = models.ForeignKey(Employees, on_delete=models.SET_NULL, null=True, blank=True)


class AdvanceOt(models.Model):
    progress = models.DecimalField(max_digits=5, decimal_places=2)
    state = models.CharField(max_length=50, choices=[('Pendiente', 'Pendiente'), ('En Progreso', 'En Progreso'), ('Finalizado', 'Finalizado')], default='Pendiente')
    updated = models.DateTimeField(auto_now=True)
    workorder = models.ForeignKey(WorkOrder, on_delete=models.CASCADE)

class Items(models.Model):
    item_number = models.CharField(max_length=20)
    description = models.TextField()
    state = models.CharField(max_length=50, choices=[('Pendiente', 'Pendiente'), ('En Progreso', 'En Progreso'), ('Finalizado', 'Finalizado')], default='Pendiente')
    workorder = models.ForeignKey(WorkOrder, on_delete=models.CASCADE)
    employees = models.ForeignKey(Employees, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['item_number', 'workorder'], name='unique_item_per_ot')
        ]

class AdvanceItem(models.Model):
    progress = models.DecimalField(max_digits=5, decimal_places=2)
    state = models.CharField(max_length=50, choices=[('Pendiente', 'Pendiente'), ('En Progreso', 'En Progreso'), ('Finalizado', 'Finalizado')], default='Pendiente')
    updated = models.DateTimeField(auto_now=True)
    items = models.ForeignKey(Items, on_delete=models.CASCADE)
    employees = models.ForeignKey(Employees, on_delete=models.SET_NULL, null=True, blank=True)

class Tasks(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

class ItemTasks(models.Model):
    state = models.CharField(max_length=50, choices=[('Pendiente', 'Pendiente'), ('En Progreso', 'En Progreso'), ('Finalizado', 'Finalizado')], default='Pendiente')
    items = models.ForeignKey(Items, on_delete=models.CASCADE)
    tasks = models.ForeignKey(Tasks, on_delete=models.CASCADE)

class ActivityRecord(models.Model):
    entry_date = models.DateTimeField(auto_now_add=True)
    exit_date = models.DateTimeField(auto_now=True)
    session_duration = models.DurationField(null=True, blank=True)
    employees = models.ForeignKey(Employees, on_delete=models.CASCADE)

class EmployeeProgress(models.Model):
    overall_progress = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now=True)
    state = models.CharField(max_length=50, choices=[('Pendiente', 'Pendiente'), ('En Progreso', 'En Progreso'), ('Finalizado', 'Finalizado')], default='Pendiente')
    employees = models.ForeignKey(Employees, on_delete=models.CASCADE)
    items = models.ForeignKey(Items, on_delete=models.CASCADE)
