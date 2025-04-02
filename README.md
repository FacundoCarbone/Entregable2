Requisitos Previos: tener instalado python:
   Verificar con python --version

Clonar el repositorio o descargar los archivos

Crear un entorno virtual:
   python -m venv venv
   source venv/Scripts/activate

Instalar las dependencias:
   pip install requirements.txt

SI hay problemas con tabulate, se puede instalar manualmente:
   pip install tabulate

Estructura:
notebooks/ 
      entrega.ipynb
src/
    __init.py
    puntajes.py
    resultados.py
.gitignore
README.md
requirements.txt

Ejecutar el programa:
   El programa procesará las rondas de juego y mostrará los resultados acumulados y el ranking final.
