# Laboratorio 2026 - Programación 1

**Grupo 2**

**Integrantes:**
**Tatiana Falco**
**Valentina Acuña**
**Ivan Pintos**

## Descripción

Programa de consola en Python que permite registrar criterios, opciones de IA
(Servicio API o Plan mensual) y casos de uso, evaluar las opciones para cada
caso, y recomendar alternativas según presupuesto y puntaje mínimo.

## Requisitos

- Python 3.10 o superior.
- No se utilizan librerías externas (solo módulos estándar: `abc` y `datetime`).

## Cómo ejecutar

1. Descomprimir el archivo.
2. Abrir una terminal en la carpeta `laboratorio_2026_grupo2` (la que contiene `main.py`).
3. Ejecutar: `python main.py`

Importante: el programa se ejecuta siempre desde `main.py`, parados en la carpeta raíz.

## Estructura

- `main.py`: menú de consola.
- `entities/`: clases del dominio (`Sistema`, `OpcionIA` con `ServicioAPI` y `PlanMensual`, `Criterio`, `CasoUso`, `Evaluacion`).
- `exceptions/`: excepción propia `ErrorLaboratorio`.

## Notas

- Los datos se guardan solo en memoria: al cerrar el programa se pierden.
- Los códigos se asignan de forma consecutiva y no se reutilizan.