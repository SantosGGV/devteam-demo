class TodoManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: str):
        """Añade una tarea a la lista de tareas.

        Args:
            task (str): La tarea a añadir.

        Returns:
            list: La lista de tareas actualizada.
        """
        self.tasks.append(task)
        return self.tasks

    def complete_task(self, task: str):
        """Marca una tarea como completada.

        Args:
            task (str): La tarea a marcar como completada.

        Returns:
            list: La lista de tareas actualizada.
        """
        if task in self.tasks:
            self.tasks.remove(task)
        return self.tasks

    def delete_task(self, task: str):
        """Elimina una tarea de la lista de tareas.

        Args:
            task (str): La tarea a eliminar.

        Returns:
            list: La lista de tareas actualizada.
        """
        if task in self.tasks:
            self.tasks.remove(task)
        return self.tasks

    def list_tasks(self):
        """Devuelve la lista de tareas.

        Returns:
            list: La lista de tareas.
        """
        return self.tasks