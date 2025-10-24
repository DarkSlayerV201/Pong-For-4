Pong For 4 (WIP)
20/2 ultima actualización

< XX --- INSTALACION --- XX >

Necesitas Visual Studio Code o alguna IDE (Entorno de Desarrollo Integrado) donde ejecutarlo
En esa IDE tenes que configurar tanto el Workspace  para que sea una carpeta que contenga a "Pong For 4"
y un entorno virtual donde este instalado Python y Pygame
Para Visual Studio Code (VSC)
- Simplemente tenes que abrir primero el VSC en vez del juego
- Despues en vez de seleccionar "Abrir un archivo", seleccionas "Abrir una carpeta"
- Abris la carpeta que contenga a Pong For 4, este va a ser el Workspace, puede ser "Pong-For-4"
- Despues para configurar el ambiente virtual o "Virtual Enviroment":
    1. Abrir la paleta de comandos o "Command Palette" (Ctrl+Shift+P)
    2. Escribir "Python: Create Enviroment" y seleccionar la opcion de "venv"
    3. Si ya tenes una versión de Python instalada, te debería salir un Python Interpreter, seleccionas ese. Con eso deberías tener el entorno virtual, solo queda instalarle Pygame
    5. Abris una terminal nueva presionando "Terminal" -> "New Terminal" (Ctrl+Shift+ñ). De manera natural debería decir que la terminal es un powershell
    6. Escribis "python -m pip install pygame"
Si no funciona puede ser que algo de la explicación este mal o algo me falto mencionar.
Si es así, manda un feedback explicando la situación que es lo mismo que mandarme un mail

IMPORTANTE: 
Si queres cambiar la condición para que la ronda termine (para que termine cuando un jugador pierde por ejemplo),
andá a "# Game_ending_variable" y cambia el numero a la cantidad de jugadores necesarios para que termine la ronda.
Si pones para que la ronda termine apenas pierde alguien, te muestra un contador de rondas perdidas para el jugador perdedor

PROBLEMAS CONOCIDOS
- No se puede abrir normal sin Visual Studio Code
- No tiene audio
- Es muy simple, le faltan mecanicas para hacerlo divertido
- Le falta un menu para controlar opciones
- Le falta una manera de salir del juego
- Los jugadores pueden salirse de la pantalla

PROBLEMAS POTENCIALES
- La resolución es estática, lo cual no es ideal
- No hay una opción para pantalla completa
- La variable "Game_ending_variable" solo puede ser accedida a través del código, 
lo cual no es ideal para la mayoría de gente
- El código tiene muchas lineas comentadas y es dificil de leer (es horrible)
- La dificultad actual se siente injusta y aburrida
    - Hace que las rondas terminen más rápido, pero los jugadores no tienen ninguna oportunidad contra la bola
    - Como resultado, los que pierden primero juegan muy poco y se pueden aburrir

PROBLEMAS FUTUROS
- Tener un solo modo de juego puede ser aburrido después de un tiempo
- La falta de un modo de juego diseñado para menos jugadores podría dar menos accesibilidad para grupos más chicos de jugadores

DESCRIPCION
Este juego es de los primeros que hice, apenas empece a programar. Como consecuencia de eso quedó medio abandonado, 
por eso tiene bugs que nunca fueron arreglados, ademnás nunca consideré en compartirlo con nadie. 
Sin embargo, eso cambió cuando aprendí de Front-End y decidí hacer 1MB Games. En un futuro voy a actualizar el juego para que al menos este presentable
como el primer juego de 1MB Games

NOTAS:
24/10: Se agrego un entorno virtual
- Aparentemente, no se puede agregar un entorno virtual a github. Aca van las instrucciones para hacerlo manualmente
    1. Abrir la paleta de comandos o "Command Palette" (Ctrl+Shift+P)
    2. Escribir "Python: Create Enviroment" y seleccionar la opcion de "venv"
    3. Si ya tenes una versión de Python instalada, te debería salir un Python Interpreter, seleccionas ese
    Con eso deberías tener el entorno virtual, solo queda instalarle Pygame
    5. Abris una terminal nueva presionando "Terminal" -> "New Terminal" (Ctrl+Shift+ñ)
    De manera natural debería decir que la terminal es un powershell
    6. Escribis "python -m pip install pygame"
