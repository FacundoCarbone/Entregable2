Objetivo:Crear un programa que procese rondas de un juego e imprima la tabla de puntuacion acumulada a lo largo de todo el juego.

Requisitos Previos: tener instalado python:
   Verificar con python --version

Clonar el repositorio o descargar los archivos:  
git clone https://github.com/FacundoCarbone/Entregable2  
  cd Entregable2  

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
   se debe usar el comando jupyter notebook para poder ejecutar las celdas
   El programa procesará las rondas de juego y mostrará los resultados acumulados y el ranking final.  
