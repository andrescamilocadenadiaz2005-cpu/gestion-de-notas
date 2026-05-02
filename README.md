# Sistema de Gestión de Notas

## Integrantes

- Andres Cadena (Tech Lead)
- Olga Mendoza (Dev Integración)
- Carlos Gómez (Dev Backend)

## Descripción

Aplicación de consola desarrollada en Python para gestionar calificaciones estudiantiles.

Permite:

- Registrar estudiantes
- Ingresar notas
- Calcular promedios
- Mostrar reportes
- Guardar y cargar información desde JSON

## Requisitos

- Python 3.x
- Git

## Instalación

Clonar repositorio:

```bash
git clone https://github.com/andrescamilocadenadiaz2005-cpu/gestion-de-notas.git
```

Entrar al proyecto:

```bash
cd sistema-notas
```

Ejecutar:

```bash
python main.py
```

## Estructura del proyecto

```text
sistema-notas/
│
├── main.py
├── backend.py
├── archivo.py
├── reporte.py
├── estudiantes.json
├── README.md
└── .gitignore
```

## Funcionalidades

### Registro
Registrar estudiantes por nombre e ID

### Notas
Ingresar notas entre 0 y 5

### Promedio
Calcular promedio y estado académico

### Reporte
Mostrar información organizada

### Archivo
Guardar y cargar datos en JSON

## Estructura base del JSON:
[
  {
    "identificacion": "",
    "nombre": "",
    "notas": [],
    "promedio": 0,
    "estado": ""
  }
]
