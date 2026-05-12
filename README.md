UndoRedoSystem - Sistema Undo y Redo con Deque
Descripción

UndoRedoSystem es una aplicación desarrollada en Python que simula un sistema de edición con funcionalidades de Undo y Redo, utilizando una estructura de datos tipo Deque (Double Ended Queue) implementada manualmente.

El sistema permite registrar acciones realizadas por el usuario, almacenarlas en un historial y administrar operaciones de deshacer y rehacer acciones, simulando el comportamiento de editores reales.

Además, el proyecto incluye una interfaz gráfica desarrollada con Tkinter para facilitar la interacción con el sistema.

Objetivo

Implementar y analizar el funcionamiento de una estructura Deque aplicada a un entorno de edición, permitiendo administrar historiales de acciones mediante operaciones de:

agregar acciones
undo
redo
mostrar historial
mostrar estado actual
Tecnologías utilizadas
Python 3
Tkinter (Interfaz gráfica)
Programación orientada a objetos
unittest
Requisitos del sistema

Antes de ejecutar el proyecto, asegúrese de contar con:

Python 3.10 o superior instalado
Tkinter habilitado (incluido por defecto en Python)
Instalación y ejecución
1. Clonar el repositorio
git clone https://github.com/usuario/UndoRedoSystem.git

Ejemplo:

git clone https://github.com/Lvoyerg-Cloud/UndoRedoSystem.git
2. Ingresar al directorio del proyecto
cd UndoRedoSystem
3. Ejecutar el programa
python undo_redo_system.py

Ejecución desde la terminal:

git clone https://github.com/Lvoyerg-Cloud/UndoRedoSystem.git
cd UndoRedoSystem
python undo_redo_system.py
Funcionamiento del sistema

El sistema realiza las siguientes operaciones:

Registro de acciones.
Almacenamiento de acciones en una Deque.
Operaciones de Undo.
Operaciones de Redo.
Visualización del historial.
Visualización del estado actual.
Eliminación de letras o palabras específicas.
Restauración del texto original.
Estructura principal del sistema

El proyecto está organizado en tres componentes principales:

1. Clase Deque

Implementa manualmente la estructura de datos Deque.

Incluye métodos como:

add_front(item)
add_rear(item)
remove_front()
remove_rear()
is_empty()
size()
2. Clase UndoRedoSystem

Encapsula toda la lógica principal del sistema:

historial de acciones
estado actual
lógica undo
lógica redo
restauración de texto
3. Clase EditorApp

Gestiona la interfaz gráfica utilizando Tkinter.

Permite interactuar con el sistema mediante botones y cuadros de texto.

Funcionalidades del sistema
Registrar acción

Permite agregar nuevas acciones al historial.

Ejemplo:

system.add_action("ESCRIBIR HOLA")
Undo

Deshace la última acción registrada.

Ejemplo:

system.undo()
Redo

Rehace una acción previamente deshecha.

Ejemplo:

system.redo()
Mostrar historial

Visualiza todas las acciones almacenadas en el sistema.

Mostrar estado actual

Muestra la acción actual activa dentro del sistema.

Eliminar texto

Permite eliminar letras o palabras específicas.

Ejemplo:

system.delete_specific_text("HOLA")
Restaurar texto

Recupera el historial original antes de eliminar contenido.

Ejemplo:

system.restore_original_text()
Validaciones implementadas

El sistema maneja correctamente los siguientes casos:

Undo sin historial disponible.
Redo sin acciones pendientes.
Acciones vacías.
Restauración inválida.
Texto inexistente.
Estados inconsistentes.
Pruebas mínimas
Prueba 1: Verificación de inserción en Deque

Objetivo: Validar que la Deque almacene elementos correctamente.

Procedimiento:

Insertar elementos.
Verificar tamaño.
Validar contenido.

Resultado esperado:

Los elementos deben almacenarse correctamente.
Prueba 2: Validación de Undo

Objetivo: Confirmar funcionamiento de undo.

Procedimiento:

Registrar una acción.
Ejecutar undo.
Verificar estado actual.

Resultado esperado:

El sistema debe regresar al estado inicial.
Prueba 3: Validación de Redo

Objetivo: Confirmar funcionamiento de redo.

Procedimiento:

Registrar acción.
Ejecutar undo.
Ejecutar redo.

Resultado esperado:

La acción debe restaurarse correctamente.
Prueba 4: Validación de entradas vacías

Objetivo: Comprobar manejo de errores.

Procedimiento:

Ingresar una acción vacía.
Intentar agregarla.

Resultado esperado:

El sistema debe mostrar mensaje de error.
Interfaz gráfica

La interfaz gráfica incluye:

Campo de entrada
Botón agregar
Botón undo
Botón redo
Botón borrar palabra
Botón restaurar texto
Historial visual
Estado actual
Botón salir
Separación de responsabilidades

El proyecto mantiene separada la lógica y la interfaz gráfica.

Organización
Clase Deque

Maneja únicamente la estructura de datos.

Clase UndoRedoSystem

Controla toda la lógica del sistema.

Clase EditorApp

Gestiona únicamente la interfaz gráfica.

Esta estructura facilita:

mantenimiento
reutilización
pruebas
escalabilidad
Restricciones del proyecto
Python 3.12+ recomendado
No se utilizan bases de datos
No se utilizan frameworks web
La estructura principal es una Deque implementada manualmente
La lógica está separada de la interfaz
Autor

Louis Neil Voyer García
Carnet: 2890-24-16741
Universidad Mariano Gálvez
