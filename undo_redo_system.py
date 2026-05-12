# ==========================================
# UNIVERSIDAD MARIANO GÁLVEZ
# Curso: Programación III
# Tarea: [S11] Deque - Undo and Redo
#
# Nombre: Louis Neil Voyer García
# Carnet: 2890-24-16741
# Catedrático: Ing. Yoel Monzón 
# ==========================================

import tkinter as tk
from tkinter import messagebox, simpledialog
import unittest

# ==========================================
# 1. CLASE DEQUE
# ==========================================
class Deque:

    def __init__(self):
        self._items = []

    def add_front(self, item):
        self._items.append(item)

    def add_rear(self, item):
        self._items.insert(0, item)

    def remove_front(self):

        if self.is_empty():
            return None

        return self._items.pop()

    def remove_rear(self):

        if self.is_empty():
            return None

        return self._items.pop(0)

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def get_all(self):
        return list(self._items)

    def set_all(self, new_list):
        self._items = new_list


# ==========================================
# 2. CLASE PRINCIPAL DEL SISTEMA
# ==========================================
class UndoRedoSystem:

    def __init__(self):

        self.history = Deque()

        self.redo_stack = Deque()

        self.current_state = "INICIO"

        # RESPALDO ORIGINAL
        self.backup_history = []

    # ======================================
    # REGISTRAR NUEVA ACCIÓN
    # ======================================
    def add_action(self, action):

        if not action or action.strip() == "":
            raise ValueError("LA ACCIÓN NO PUEDE ESTAR VACÍA.")

        self.history.add_front(action)

        self.current_state = action

        while not self.redo_stack.is_empty():
            self.redo_stack.remove_front()

    # ======================================
    # UNDO
    # ======================================
    def undo(self):

        if self.history.is_empty():
            return None

        last = self.history.remove_front()

        self.redo_stack.add_front(last)

        self.current_state = (
            "INICIO"
            if self.history.is_empty()
            else self.history.get_all()[-1]
        )

        return last

    # ======================================
    # REDO
    # ======================================
    def redo(self):

        if self.redo_stack.is_empty():
            return None

        action = self.redo_stack.remove_front()

        self.history.add_front(action)

        self.current_state = action

        return action

    # ======================================
    # BORRAR LETRA O PALABRA
    # ======================================
    def delete_specific_text(self, text):

        # GUARDAR COPIA ORIGINAL
        self.backup_history = self.history.get_all().copy()

        current_list = self.history.get_all()

        nueva_lista = []

        encontrado = False

        for item in current_list:

            if text.lower() in item.lower():

                encontrado = True

                nuevo_item = item.replace(text, "")
                nuevo_item = nuevo_item.replace(text.lower(), "")
                nuevo_item = nuevo_item.replace(text.upper(), "")

                nuevo_item = " ".join(nuevo_item.split())

                nueva_lista.append(nuevo_item)

            else:

                nueva_lista.append(item)

        if not encontrado:
            return False

        self.history.set_all(nueva_lista)

        self.current_state = (
            "INICIO"
            if self.history.is_empty()
            else self.history.get_all()[-1]
        )

        return True

    # ======================================
    # RESTAURAR TEXTO ORIGINAL
    # ======================================
    def restore_original_text(self):

        if self.backup_history:

            self.history.set_all(self.backup_history)

            self.current_state = (
                "INICIO"
                if self.history.is_empty()
                else self.history.get_all()[-1]
            )

            return True

        return False


# ==========================================
# 3. INTERFAZ GRÁFICA
# ==========================================
class EditorApp:

    def __init__(self, root):

        self.system = UndoRedoSystem()

        self.root = root

        self.root.title("SIMULADOR DE EDICIÓN CON DEQUE")

        self.root.geometry("500x700")

        self.root.configure(bg="#f0f0f0")

        # ======================================
        # TÍTULO
        # ======================================
        tk.Label(
            root,
            text="SISTEMA UNDO Y REDO",
            font=("Arial", 18, "bold"),
            fg="#1a237e",
            bg="#f0f0f0"
        ).pack(pady=15)

        # ======================================
        # DATOS PERSONALES
        # ======================================
        tk.Label(
            root,
            text="Nombre: Louis Neil Voyer García",
            font=("Arial", 10, "bold"),
            fg="#1b5e20",
            bg="#f0f0f0"
        ).pack()

        tk.Label(
            root,
            text="Carnet: 2890-24-16741",
            font=("Arial", 10, "bold"),
            fg="#4e342e",
            bg="#f0f0f0"
        ).pack()

        tk.Label(
            root,
            text="Ing. Yoel Monzón",
            font=("Arial", 10, "bold"),
            fg="#6a1b9a",
            bg="#f0f0f0"
        ).pack(pady=5)

        # ======================================
        # ESTADO ACTUAL
        # ======================================
        tk.Label(
            root,
            text="ESTADO ACTUAL:",
            font=("Arial", 12, "bold"),
            bg="#f0f0f0"
        ).pack()

        self.lbl_state = tk.Label(
            root,
            text=self.system.current_state,
            font=("Arial", 15, "bold"),
            fg="blue",
            bg="#f0f0f0"
        )

        self.lbl_state.pack(pady=10)

        # ======================================
        # ENTRADA
        # ======================================
        tk.Label(
            root,
            text="ESCRIBE UNA ACCIÓN:",
            font=("Arial", 11),
            bg="#f0f0f0"
        ).pack(pady=5)

        self.entry = tk.Entry(
            root,
            width=40,
            font=("Arial", 12),
            justify="center"
        )

        self.entry.pack(pady=10)

        # ======================================
        # FRAME BOTONES
        # ======================================
        frame_btn = tk.Frame(root, bg="#f0f0f0")

        frame_btn.pack(pady=10)

        # ======================================
        # BOTÓN AGREGAR
        # ======================================
        tk.Button(
            frame_btn,
            text="AGREGAR",
            command=self.add,
            width=12,
            bg="#bbdefb",
            font=("Arial", 10, "bold")
        ).pack(side=tk.LEFT, padx=5)

        # ======================================
        # BOTÓN UNDO
        # ======================================
        tk.Button(
            frame_btn,
            text="UNDO",
            command=self.undo,
            width=12,
            bg="#ffcdd2",
            font=("Arial", 10, "bold")
        ).pack(side=tk.LEFT, padx=5)

        # ======================================
        # BOTÓN REDO
        # ======================================
        tk.Button(
            frame_btn,
            text="REDO",
            command=self.redo,
            width=12,
            bg="#c8e6c9",
            font=("Arial", 10, "bold")
        ).pack(side=tk.LEFT, padx=5)

        # ======================================
        # BOTÓN BORRAR
        # ======================================
        tk.Button(
            root,
            text="BORRAR LETRA O PALABRA",
            command=self.delete_text,
            width=30,
            bg="#fff176",
            font=("Arial", 10, "bold")
        ).pack(pady=10)

        # ======================================
        # BOTÓN RESTAURAR
        # ======================================
        tk.Button(
            root,
            text="RESTAURAR LETRA O PALABRA",
            command=self.restore_text,
            width=30,
            bg="#80deea",
            font=("Arial", 10, "bold")
        ).pack(pady=5)

        # ======================================
        # HISTORIAL
        # ======================================
        tk.Label(
            root,
            text="HISTORIAL DE ACCIONES:",
            font=("Arial", 12, "bold"),
            bg="#f0f0f0"
        ).pack(pady=10)

        self.listbox = tk.Listbox(
            root,
            width=50,
            height=8,
            font=("Arial", 10)
        )

        self.listbox.pack(pady=10)

        # ======================================
        # BOTÓN SALIR
        # ======================================
        tk.Button(
            root,
            text="SALIR DEL PROGRAMA",
            command=self.exit_app,
            width=25,
            bg="#424242",
            fg="white",
            font=("Arial", 10, "bold")
        ).pack(pady=20)

    # ======================================
    # ACTUALIZAR INTERFAZ
    # ======================================
    def update_ui(self):

        self.lbl_state.config(
            text=self.system.current_state.upper()
        )

        self.listbox.delete(0, tk.END)

        for action in reversed(self.system.history.get_all()):

            self.listbox.insert(
                tk.END,
                f"• {action.upper()}"
            )

    # ======================================
    # AGREGAR ACCIÓN
    # ======================================
    def add(self):

        try:

            val = self.entry.get()

            self.system.add_action(val)

            self.entry.delete(0, tk.END)

            self.update_ui()

        except ValueError as e:

            messagebox.showwarning(
                "ATENCIÓN",
                str(e)
            )

    # ======================================
    # UNDO
    # ======================================
    def undo(self):

        result = self.system.undo()

        if result is None:

            messagebox.showwarning(
                "ATENCIÓN",
                "NO HAY ACCIONES PARA DESHACER."
            )

        self.update_ui()

    # ======================================
    # REDO
    # ======================================
    def redo(self):

        result = self.system.redo()

        if result is None:

            messagebox.showwarning(
                "ATENCIÓN",
                "NO HAY ACCIONES PARA REHACER."
            )

        self.update_ui()

    # ======================================
    # BORRAR LETRA O PALABRA
    # ======================================
    def delete_text(self):

        texto = simpledialog.askstring(
            "BORRAR",
            "ESCRIBE LETRA O PALABRA A ELIMINAR:"
        )

        if texto and texto.strip() != "":

            encontrado = self.system.delete_specific_text(texto)

            if encontrado:

                self.update_ui()

                restante = "\n".join(
                    self.system.history.get_all()
                )

                messagebox.showinfo(
                    "RESULTADO",
                    f"SE ELIMINÓ:\n\n"
                    f"{texto.upper()}\n\n"
                    f"TEXTO RESTANTE:\n\n"
                    f"{restante.upper()}"
                )

            else:

                messagebox.showerror(
                    "ERROR",
                    f"NO SE ENCONTRÓ:\n\n{texto.upper()}"
                )

        else:

            messagebox.showwarning(
                "ATENCIÓN",
                "DEBES ESCRIBIR ALGO."
            )

    # ======================================
    # RESTAURAR TEXTO
    # ======================================
    def restore_text(self):

        texto = simpledialog.askstring(
            "RESTAURAR",
            "ESCRIBE LETRA O PALABRA A RESTAURAR:"
        )

        if texto:

            restaurado = self.system.restore_original_text()

            if restaurado:

                self.update_ui()

                texto_restaurado = "\n".join(
                    self.system.history.get_all()
                )

                messagebox.showinfo(
                    "TEXTO RESTAURADO",
                    f"SE RESTAURÓ:\n\n"
                    f"{texto.upper()}\n\n"
                    f"TEXTO COMPLETO:\n\n"
                    f"{texto_restaurado.upper()}"
                )

            else:

                messagebox.showwarning(
                    "ATENCIÓN",
                    "NO HAY TEXTO PARA RESTAURAR."
                )

    # ======================================
    # SALIR
    # ======================================
    def exit_app(self):

        salir = messagebox.askokcancel(
            "SALIR",
            "¿DESEAS CERRAR EL PROGRAMA?"
        )

        if salir:
            self.root.destroy()


# ==========================================
# 4. PRUEBAS UNITARIAS
# ==========================================
class TestDeque(unittest.TestCase):

    def test_add_front(self):

        d = Deque()

        d.add_front("A")

        self.assertEqual(d.size(), 1)

    def test_remove_front(self):

        d = Deque()

        d.add_front("A")

        self.assertEqual(d.remove_front(), "A")

    def test_empty(self):

        d = Deque()

        self.assertTrue(d.is_empty())


class TestUndoRedo(unittest.TestCase):

    def test_undo(self):

        s = UndoRedoSystem()

        s.add_action("HOLA")

        s.undo()

        self.assertEqual(s.current_state, "INICIO")

    def test_redo(self):

        s = UndoRedoSystem()

        s.add_action("HOLA")

        s.undo()

        s.redo()

        self.assertEqual(s.current_state, "HOLA")


# ==========================================
# EJECUCIÓN PRINCIPAL
# ==========================================
if __name__ == "__main__":

    root = tk.Tk()

    app = EditorApp(root)

    root.mainloop()
