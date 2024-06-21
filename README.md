# Proyecto de Fine-Tuning de Modelo de Generación de Texto en Español

Este proyecto se centra en el fine-tuning de un modelo de generación de texto (GPT-2) en español utilizando el modelo `datificate/gpt2-small-spanish`. El objetivo principal es generar mensajes de texto (SMS) promocionales en español coherentes dada una frase de inicio.

## Dataset
El dataset utilizado consiste en 2000 SMS promocionales en español creado con la API de OpenAi. Cada SMS tiene una longitud promedio de 160 caracteres. Los SMS se crearon sobre 4 topics: viajes, comida, ropa y academia de inglés.


### Preprocesamiento
- **Limpieza:** Removidos caracteres especiales y eliminados duplicados.
- **Preparación:** División del dataset en conjuntos de entrenamiento y validación.
- **Tokenización:** Utilizamos el tokenizer del modelo `datificate/gpt2-small-spanish`.

## Modelo
- **Modelo Base:** `datificate/gpt2-small-spanish`
- **Arquitectura:** Basado en GPT-2 con 124M parámetros.


## Definición del problema
Actualmente hay empresas que brindan una plataforma para el envío de SMS masivos. Entre una de las funcionalidades esta la de publicidad y marketing, que permite informar a los clientes sobre descuentos, días especiales, promociones etc.

**Objetivo**: Entrenar un modelo que sea capaz de generar SMS promocionales en español, para optimizar el tiempo de creación y generación de SMS más creativos.

