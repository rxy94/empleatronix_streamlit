# EMPLEATRONIX

Una aplicación web interactiva desarrollada con Streamlit para visualizar y analizar información de empleados de manera simple y efectiva.

## Características

- **Visualización de datos**: Tabla interactiva con información completa de empleados
- **Gráficos personalizables**: Gráfico de barras horizontal con opciones de personalización
- **Selector de color**: Personaliza el color de las barras del gráfico
- **Controles de visibilidad**: 
  - Toggle para mostrar/ocultar nombres de empleados
  - Toggle para mostrar/ocultar valores de salario en las barras
- **Análisis de salarios**: Visualización clara de la distribución salarial

## Instalación y Uso

### Requisitos Previos

- Python 3.12 o superior
- pip (gestor de paquetes de Python)
- Docker, Docker Compose

### Instalación Local

1. Clona el repositorio:
```bash
git clone https://github.com/rxy94/empleatronix_streamlit.git
cd empleatronix_streamlit
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Ejecuta la aplicación:
```bash
streamlit run streamlit_app.py
```

4. Abre tu navegador en `http://localhost:8501`

### Uso con Docker

1. Construye la imagen:
```bash
docker compose build 
```

2. Ejecuta el contenedor:
```bash
docker compose up
```

3. Accede a la aplicación en `http://localhost:8501`

## Dependencias

- `streamlit` - Framework para aplicaciones web de datos
- `pandas` - Manipulación y análisis de datos
- `matplotlib` - Creación de visualizaciones

## Estructura del Proyecto

```
empleatronix_streamlit/
│
├── streamlit_app.py      # Aplicación principal
├── requirements.txt      # Dependencias del proyecto
├── Dockerfile           # Configuración de Docker
├── datasets/
│   └── employees.csv    # Datos de empleados
└── README.md           # Este archivo
```

## Funcionalidades Principales

### Visualización de Datos
La aplicación carga automáticamente datos desde un archivo CSV y los presenta en un dataframe interactivo de Streamlit.

### Gráfico Interactivo
- Gráfico de barras horizontal que muestra el salario de cada empleado
- Selector de color personalizable
- Escala de 0€ a 4500€
- Etiquetas de valores opcionales

## Créditos

Desarrollado por **Ruyi Xia Ye** - CPIFP Alan Turing

## Licencia

Este proyecto no tiene una licencia especificada actualmente. 

---

⭐ Si te gusta este proyecto, ¡no olvides darle una estrella!