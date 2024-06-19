# Proyecto de Fine-Tuning de Modelo de Generación de Texto en Español

Este proyecto se centra en el fine-tuning de un modelo de generación de texto (GPT-2) en español utilizando el modelo base `datificate/gpt2-small-spanish`. El objetivo principal es generar mensajes de texto (SMS) promocionales en español coherentes dada una frase de inicio.


## Dataset

El dataset utilizado consiste en 2000 SMS en español creado con la API de OpenAi. Cada SMS tiene una longitud promedio de 160 caracteres.

### Preprocesamiento

- **Tokenización:** Utilizamos el tokenizer del modelo `datificate/gpt2-small-spanish`.
- **Limpieza:** Removimos caracteres especiales, normalizamos textos y eliminamos duplicados.
- **Preparación:** Dividimos el dataset en conjuntos de entrenamiento y validación.

## Modelo

- **Modelo Base:** `datificate/gpt2-small-spanish`
- **Arquitectura:** Basado en GPT-2 con 124M parámetros.

