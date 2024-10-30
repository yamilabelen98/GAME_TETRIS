# Tetris con Pygame

Este es un juego de Tetris simple desarrollado en Python utilizando la biblioteca Pygame. Las piezas caen y puedes controlar su movimiento y rotación. Además, incluye música de fondo, funciones de pausa y control de volumen, y una pantalla de "Game Over" cuando pierdes.

## Características del juego

- **Control del juego**:
  - Mueve las piezas con las teclas de flecha: 
    - Flecha izquierda: Mover a la izquierda
    - Flecha derecha: Mover a la derecha
    - Flecha abajo: Acelerar la caída de la pieza
    - Flecha arriba: Rotar la pieza
  - Las piezas cambian de color cuando colisionan con otra pieza o el borde del tablero.
  
- **Pausar y reanudar**: 
  - Pulsa `Enter` para pausar o reanudar el juego. La música también se pausará o reanudará.
  
- **Control de volumen**:
  - Presiona `F2` para bajar el volumen de la música.
  - Presiona `F3` para subir el volumen de la música.

- **Pantalla de "Game Over"**:
  - Cuando pierdes, aparece una pantalla de "Game Over". 
  - Puedes presionar `R` para reiniciar el juego o presionar `Esc` para salir.

## Requisitos

- Python 3.12 o superior.
- Pygame 2.6.1 o superior.

## Instalación

1. Clona este repositorio en tu máquina local:

    ```bash
    git clone https://github.com/yamilabelen98/GAME_TETRIS.git
    ```

2. Navega al directorio del proyecto:

    ```bash
    cd GAME_TETRIS
    ```

3. Crea un entorno virtual (opcional pero recomendado):

    ```bash
    python -m venv venv
    ```

4. Activa el entorno virtual:
   
    - En Windows:
    
      ```bash
      venv\Scripts\activate
      ```
      
    - En macOS/Linux:
    
      ```bash
      source venv/bin/activate
      ```

5. Instala las dependencias:

    ```bash
    pip install pygame
    ```

6. Ejecuta el juego:

    ```bash
    python tetris.py
    ```

## Cómo jugar

- Las piezas caen automáticamente.
- Usa las flechas para mover y rotar las piezas:
  - **Izquierda/Derecha**: Mueve la pieza hacia los lados.
  - **Abajo**: Acelera la caída de la pieza.
  - **Arriba**: Rota la pieza.
  
- Puedes pausar el juego y la música con `Enter`, o ajustar el volumen de la música con `F2` (bajar) y `F3` (subir).
- Si pierdes, se mostrará una pantalla de "Game Over". Puedes presionar `Enter` para reiniciar el juego o `Esc` para salir.

## Música

El juego incluye música de fondo, la cual puedes modificar cambiando el archivo `tetris_music.mp3.mp3` por cualquier otro archivo MP3.

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas agregar nuevas características o corregir errores, siéntete libre de hacer un fork del repositorio y enviar un pull request.

---

**Autor:** Yamila De Olivera  
Desarrolladora web Full Stack.
