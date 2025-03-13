from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Items, ItemTasks, Tasks

@receiver(post_save, sender=Items)
def assign_tasks_to_item(sender, instance, created, **kwargs):
    """
    Cuando se crea un Item, se asignan automáticamente todas las tareas de su WorkOrder,
    pero el estado de cada tarea es independiente por Item.
    """

    if created:  # Solo cuando se crea por primera vez
        tasks = Tasks.objects.all()
        for task in tasks:
            ItemTasks.objects.create(items=instance, tasks=task)