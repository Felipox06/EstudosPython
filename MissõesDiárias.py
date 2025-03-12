import json
import tkinter as tk
from tkinter import ttk
import sys
from pathlib import Path

class TaskManager:
    def __init__(self):
        # Determinar o caminho base (para rodar tanto em desenvolvimento quanto empacotado)
        if getattr(sys, 'frozen', False):
            base_path = Path(sys._MEIPASS)
        else:
            base_path = Path(__file__).parent

        self.tasks_file = base_path / "tasks.json"
        self.load_tasks()

        self.root = tk.Tk()
        self.root.title("Gerenciador de Tarefas")

        # Usar ttk para uma aparência mais moderna
        style = ttk.Style()
        style.theme_use("default")

        self.create_gui()
        
        # Salvar as tarefas antes de entrar no loop
        self.save_tasks()
        self.root.mainloop()

    def load_tasks(self):
        try:
            with open(self.tasks_file, "r") as f:
                data = json.load(f)
                self.active_tasks = data.get("Pendentes", [])
                self.completed_tasks = data.get("Completadas", [])
        except FileNotFoundError:
            self.active_tasks = []
            self.completed_tasks = []

    def save_tasks(self):
        data = {"Pendentes": self.active_tasks, "Completadas": self.completed_tasks}
        with open(self.tasks_file, "w") as f:
            json.dump(data, f)

    def create_gui(self):
        # Lista de tarefas ativas
        self.active_listbox = tk.Listbox(self.root)
        for task in self.active_tasks:
            self.active_listbox.insert(tk.END, task)

        # Lista de tarefas concluídas
        self.completed_listbox = tk.Listbox(self.root)
        for task in self.completed_tasks:
            self.completed_listbox.insert(tk.END, task)

        # Campo de entrada e botões
        self.entry = ttk.Entry(self.root)
        self.add_button = ttk.Button(self.root, text="Adicionar Tarefa", command=self.add_task)
        self.mark_button = ttk.Button(self.root, text="Marcar como Concluída", command=self.mark_task)
        self.unmark_button = ttk.Button(self.root, text="Desmarcar", command=self.unmark_task)

        # Layout usando grid
        self.active_listbox.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        self.completed_listbox.grid(row=0, column=2, columnspan=2, padx=5, pady=5)
        self.entry.grid(row=1, column=0, padx=5, pady=5)
        self.add_button.grid(row=1, column=1, padx=5, pady=5)
        self.mark_button.grid(row=2, column=0, padx=5, pady=5)
        self.unmark_button.grid(row=2, column=1, padx=5, pady=5)

    def add_task(self):
        task = self.entry.get()
        if task:
            self.active_tasks.append(task)
            self.active_listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
            self.save_tasks()

    def mark_task(self):
        selected = self.active_listbox.curselection()
        if selected:
            index = selected[0]
            task = self.active_listbox.get(index)
            self.active_listbox.delete(index)
            self.active_tasks.remove(task)
            self.completed_tasks.append(task)
            self.completed_listbox.insert(tk.END, task)
            self.save_tasks()

    def unmark_task(self):
        selected = self.completed_listbox.curselection()
        if selected:
            index = selected[0]
            task = self.completed_listbox.get(index)
            self.completed_listbox.delete(index)
            self.completed_tasks.remove(task)
            self.active_tasks.append(task)
            self.active_listbox.insert(tk.END, task)
            self.save_tasks()

if __name__ == "__main__":
    TaskManager()