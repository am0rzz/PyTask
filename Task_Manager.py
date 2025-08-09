class Task:
    def __init__(self, title, description):
        self.title = title  
        self.description = description
        self.completed = False
    
    def mark_completed(self):
        self.completed = True

    def __str__(self):
        if self.completed:
            status = "✅"
        else:
            status = "❌"
        if self.description == "":
            return f"{self.title} --> {status}"
        else:
            return f"{self.title} --> {self.description} -- {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self,task):
        self.tasks.append(task)
    
    def show_tasks(self):
        for task in self.tasks:
            print(task)
    
    def find_task(self, title):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                return task
        return None

    def remove_task(self, title):
        task = self.find_task(title)
        if task:
            self.tasks.remove(task)
            print("Task Deleted Successfully!")
        else:
            print("Task not Found!")
    
    def save_tasks(self):
        with open('tasks.txt', 'w') as file:
            for task in self.tasks:
                file.write(f"{task.title}|{task.description}|{task.completed}\n")
    
    def load_tasks(self):
        self.tasks.clear()
        try:
            with open('tasks.txt' , 'r') as file:
                for line in file:
                    title, description, completed = line.split('|')
                    task = Task(title,description)
                    if completed.strip() == "True":
                        task.completed = True
                    else:
                        task.completed = False
                    self.tasks.append(task)
        except FileNotFoundError:
            open("tasks.txt", "x")


if __name__ == '__main__':
    manager = TaskManager()
    manager.load_tasks()
    while True:
        title = input("Enter task title (or 'q' to quit): ")
        if title.lower() == 'q':
            manager.save_tasks()
            break
        description = input("Enter task description: ")
        task = Task(title, description)
        manager.add_task(task)
    
