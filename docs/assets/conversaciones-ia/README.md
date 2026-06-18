# Capturas de conversaciones con IA

Imágenes de las conversaciones de diseño y desarrollo del proyecto (Cursor / ChatGPT).

## Archivos incluidos

| Archivo | Contenido |
|---------|-----------|
| `bpmn-as-is-guia.png` | Solicitud de guía para BPMN AS-IS en bpmn.io |
| `proceso-as-is.png` | Diagrama del proceso manual actual |
| `proceso-to-be.png` | Proceso TO-BE con lanes Usuario y Bot |
| `decisiones-tecnicas.jpeg` | Elección Telegram + CSV y esquema de datos |
| `arquitectura-modular.jpeg` | Árbol de módulos y tabla de responsabilidades |
| `main-conexion-telegram.jpeg` | Flujo de `main.py` (TOKEN → polling) |
| `identificacion-usuario.jpeg` | `chat_id` y diccionario `_estados` |
| `flujo-datos-temporales.jpeg` | Registro multi-paso con `_datos_temporales` |
| `entorno-virtual-requirements.jpeg` | venv y `requirements.txt` |

## Uso en la documentación

Las capturas están integradas en [proceso-desarrollo.md](../../proceso-desarrollo.md) con contexto y captions.

Para referenciar una imagen desde otro Markdown:

```markdown
![Descripción](../assets/conversaciones-ia/nombre-archivo.png)
```
