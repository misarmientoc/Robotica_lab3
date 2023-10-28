# Robotica_lab3
Laboratorio 3 de robótica 2023-2
## Integrantes
- Norma Lorena Martinez Zavala
- Miguel Angel Sarmiento Cabarcas
- Jaime Andres Sanchez Peralta
### Metodología
Escribir un código que permita operar una tortuga del paquete turtlesim con el teclado, cumpliendo con las siguientes especificaciones: <br>
• Movimiento hacia adelante y hacia atrás con las teclas W y S. <br>
• Giros en sentido horario y antihorario con las teclas D y A. <br>
• Retornar a la posición y orientación centrales con la tecla R. <br>
• Giro de 180° con la tecla ESPACIO. <br>


![image](https://github.com/misarmientoc/Robotica_lab3/assets/47614570/0e10a00c-34f0-4ade-9424-d08c4590e67d)

```

rosrun turtlesim turtlesim node

```

#Código

La primera parte del código se tomó del ejemplo que incluye la guía y esta en el sitio Python For Fun: Get Key Press in Python http://python4fun.blogspot.com/2008/06/get-key-press-in-python.html

![image](https://github.com/misarmientoc/Robotica_lab3/assets/47614570/35c1fcd9-dee2-4ef1-9de0-6200992266e6)


Para mover la tortuga en el simulador de ROS, se implementa una función que lee las teclas presionadas por el usuario y envía comandos de velocidad al topic cmd_vel. Además, se crean dos objetos de tipo ServiceProxy que se conectan con los servicios TeleportAbsolute y TeleportRelative, que permiten cambiar la posición y la orientación de la tortuga respectivamente. La función main se encarga de inicializar el nodo de ROS y llamar a la función que detecta las teclas del teclado. 

![image](https://github.com/misarmientoc/Robotica_lab3/assets/47614570/188902ef-1ee1-45b0-a3b8-5bc2ea3089da)

El siguiente código muestra cómo controlar el movimiento de una tortuga en ROS usando las teclas del teclado. Se define un objeto de tipo ServiceProxy para llamar a los servicios de reset y rotate de la tortuga. Luego se crea un objeto de tipo Publisher para publicar mensajes de tipo Twist en el tópico /turtle1/cmd_vel. Después se inicializa el nodo y se configura la frecuencia de publicación. Dentro del ciclo while con condicional de siempre que ROS esté activo, se crea una función que guarda el valor actual de la tecla presionada como un número binario de 8 bits, se reinician los valores del mensaje a 0 para que las iteraciones anteriores no afecten el funcionamiento, mediante una serie de condicionales se compara cuál tecla fue presionada y en caso de ser 'w' o 's' se cambia la velocidad en x por 1 o -1 respectivamente, en caso de ser 'a' o 'd' se cambia la velocidad angular en z por 1 o -1 respectivamente, pero en caso de ser 'r' o ' ' se ejecuta el ServiceProxy definido al inicio del código con los valores para reiniciar la posición de la tortuga en caso de haber presionado 'r' o con una rotación relativa de pi en caso de haber presionado la barra espaciadora. Finalmente se publica el mensaje y se espera hasta la siguiente iteración.

![image](https://github.com/misarmientoc/Robotica_lab3/assets/47614570/6a989d66-45dd-4ab3-a0df-001b43268e00)



### Resultados

El movimiento realizado se puede ver en el siguiente video

https://youtu.be/7X1kx9yWbPY

![Screenshot 2023-10-27 190341](https://github.com/misarmientoc/Robotica_lab3/assets/47614570/9ce75160-4284-475b-917c-b41a942915d0)


### Análisis
• Para hacer uso de la función catkin y sus derivados como catkin_make, debe tenerse instalado el paquete, ya que no es una función nativa del entorno de trabajo, ni viene previamente instalada en ROS, sin embargo, puede instalarse a través de este.

• Para abrirse el archivo de python MyTeleopKey, se debe realizar un catkin build previo para actualizar los archivos cargados en la carpeta creada por el catkin_make, de otra manera, el sistema no lo detectará.

•Para la realización de la conexión con MATLAB, en caso de que se requiera, se puede realizar mediante una comunicación SSH, se debe revisar si la máquina virtual, tiene el protocolo de comunicación habilitado.
### Conclusiones

Como se mostro en el video, e el código funciona de manera efectiva y permite al usuario interactuar con la tortuga de forma  bastante sencilla. Este tipo de control es útil en aplicaciones de robótica donde se requiere una interacción en tiempo real con un robot en un entorno de simulación.

Si bien tuvimos varias complicaciones con el programa ROS y el manejo de Linux, la practica se implemento con éxito, pues se logro el control de una tortuga en ROS a través del teclado, lo que demuestra la flexibilidad y potencia de las herramientas en ROS para el desarrollo y la experimentación en la materia.  Esta practica fue bastante interesante pues consideramos que la implementación de control de tortuga a través del teclado en ROS es un paso importante en la comprensión de la programación de robots y la simulación en robótica y nos permitira avanzar en futuros laboratorios.
