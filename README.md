# UndoRedoSystem - Sistema Undo y Redo con Deque

## Descripción

UndoRedoSystem es una aplicación desarrollada en Python que simula un sistema de edición con funcionalidades de **Undo** y **Redo**, utilizando una estructura de datos tipo **Deque** implementada manualmente.

El sistema permite registrar acciones realizadas por el usuario, deshacer cambios, rehacer acciones eliminadas y visualizar el historial completo de operaciones mediante una interfaz gráfica desarrollada con Tkinter.

## Objetivo

Implementar una estructura de datos Deque aplicada a un problema práctico de edición, separando correctamente la lógica del sistema y la interfaz gráfica.

## Tecnologías utilizadas

* Python 3
* Tkinter (Interfaz gráfica)
* Programación orientada a objetos (POO)
* unittest para pruebas unitarias

## Requisitos del sistema

Antes de ejecutar el proyecto, asegúrese de contar con:

* Python 3.12 o superior
* Tkinter habilitado (incluido por defecto en Python)

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/usuario/UndoRedoSystem.git
```
Ejemplo:
git clone https://github.com/Lvoyerg-Cloud/PrintQueueSim.git

### 2. Ingresar al directorio del proyecto

```bash
cd UndoRedoSystem
```

## Ejecución desde la terminal

```bash
python "UndoRedoSystem.py"
```
Ejecución desde la terminal: 
1. git clone https://github.com/usuario/UndoRedoSystem.git
2. cd UndoRedoSystem
3. python "UndoRedoSystem.py"
## Funcionamiento del sistema

El sistema permite realizar las siguientes operaciones:

* Registrar nuevas acciones
* Deshacer acciones (Undo)
* Rehacer acciones (Redo)
* Mostrar historial de acciones
* Mostrar el estado actual del sistema
* Eliminar letras o palabras específicas
* Restaurar texto eliminado

## Estructura del proyecto

El proyecto se encuentra dividido en diferentes componentes:

### Clase Deque

Implementa la estructura de datos principal utilizada para administrar el historial de acciones.

Métodos implementados:

* add_front(item)
* add_rear(item)
* remove_front()
* remove_rear()
* is_empty()
* size()

### Clase UndoRedoSystem

Encapsula toda la lógica principal del sistema:

* Historial de acciones
* Estado actual
* Operaciones Undo y Redo
* Validaciones
* Restauración de texto

### Clase EditorApp

Gestiona toda la interfaz gráfica utilizando Tkinter.

## Validaciones implementadas

El sistema controla correctamente:

* Acciones vacías o inválidas
* Undo sin historial disponible
* Redo sin acciones disponibles
* Restauración sin respaldo previo
* Estados inconsistentes

## Pruebas mínimas

El proyecto incluye pruebas unitarias utilizando unittest.

### Prueba 1: Inserción en Deque

**Objetivo:** Verificar inserción correcta de elementos.

Resultado esperado:

* El tamaño del Deque debe aumentar correctamente.

### Prueba 2: Eliminación en Deque

**Objetivo:** Verificar extracción correcta de elementos.

Resultado esperado:

* El elemento eliminado debe coincidir con el insertado.

### Prueba 3: Validación de Deque vacío

**Objetivo:** Confirmar detección de estructura vacía.

Resultado esperado:

* is_empty() debe retornar True.

### Prueba 4: Funcionamiento de Undo

**Objetivo:** Validar deshacer acciones.

Resultado esperado:

* El sistema debe regresar al estado anterior.

### Prueba 5: Funcionamiento de Redo

**Objetivo:** Validar rehacer acciones.

Resultado esperado:

* El sistema debe restaurar la acción deshecha.

## Características principales

* Implementación propia de Deque
* Interfaz gráfica amigable
* Separación entre lógica y UI
* Manejo de errores y validaciones
* Historial dinámico de acciones
* Sistema de restauración de texto

## Autor

**Louis Neil Voyer García**
Carnet: 2890-24-16741
Curso: Programación III
Catedrático: Ing. Yoel Monzón
Universidad Mariano Gálvez

