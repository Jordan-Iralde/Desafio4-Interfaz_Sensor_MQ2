# Desafio4-Interfaz_Sensor_MQ2
<li>Giovanni Peirone</li>
<li>Jordan Iralde</li>
<li>Mateo Teresani</li>
<li>Mateo Moreira</li>
<li>Maximiliano Olmos</li>

## Documentación
Link al Trello:
https://trello.com/invite/b/670699cfad96f6addc53fe46/ATTIa381a2ac4102d80091938758aa10b61b77735316/desafio4robotica

Link a la Documentacion:
https://docs.google.com/document/d/1l-YgR61G4tXOCF7lm9tJ6MXk71gIP1nglVBSKCm5ll4/edit?usp=sharing

Link al Figma:
https://www.figma.com/design/FZXvzcFbItyY1XtRRzq6Qz/Desafio_4_dise%C3%B1o?node-id=0-1&m=dev&t=b1GCJQuWSaobxicu-1

### Tareas
:white_check_mark: representa una tarea que está en la lista para hacer o completada.
:hourglass_flowing_sand: se utiliza para una tarea que está en progreso.
| **Tarea**            | **Hacer**            | **Haciendo**          | **Hecho**             |
|----------------------|----------------------|-----------------------|-----------------------|
| Hacer Repositorio    |                      |                       | :white_check_mark:    |
| Investigar UX/UI     |                      |                       | :white_check_mark:    |
| Programa En Python   |                      |                       | :white_check_mark:    |
| Documentacion        |                      |:hourglass_flowing_sand:|                      |
| Nueva GUI            |                      |:hourglass_flowing_sand:|                      |

---

# Resumen del Proyecto
<p> Este proyecto trata de un dispositivo con conexion bluetooth en el cual recibiremos datos acerca de la cantidad de gas que se encuentra en el aire y los mostraremos en pantalla</p>
<p> Para esto usaremos python y librerias para el bluetooth, interfaz y visualizacion de datos</p>

<br>

# Nuestros Objetivos
<p> Los objetivos que tenemos son... </p>
<ul>
  <li> Hacer un diseño para Celular y PC </li>
  <li> Aprender sobre el manejo de Bluetooth con Python </li>
  <li> Aprender sobre UX/UI </li>
  <li> Aprender Tkinter y Java</li>
</ul>

---
Desafío 4: Desarrollo de una Interfaz para la Visualización de Datos del Sensor MQ2
En equipos de 4 integrantes, realizar la investigación, análisis, debate, conclusiones de las
temáticas planteadas.
Objetivos:
• Investigar UX/UI.
• Desarrollar una interfaz gráfica para visualizar los datos transmitidos por el sensor MQ2
mediante Bluetooth.
• Comprender la recepción de datos desde dispositivos Arduino en una PC.
• Aplicar conocimientos de programación en Python.
Instrucciones:
1. Revisión del Proyecto Anterior:
Asegúrate de que el proyecto del Desafío 3 esté completo y funcionando correctamente.
Verifica que los datos se transmitan adecuadamente desde el sensor MQ2 utilizando la
terminal.
2. Recepción de Datos:
Conecta el módulo Bluetooth al Arduino y asegúrate de establecer una conexión con la
PC.
Confirma que la PC esté recibiendo los datos enviados por el módulo Bluetooth.
3. Construcción de la Interfaz:
Opción 1: Python
▪ Utiliza la biblioteca tkinter para crear una ventana gráfica que visualice los
datos recibidos.
▪ Implementa una conexión con el puerto Bluetooth de la PC para recibir los
datos en tiempo real. Para esto, utiliza una biblioteca como pyserial que te
permita interactuar con el puerto serie.
▪ La interfaz debe tener una ventana principal que muestre los valores del
sensor de manera clara. Puedes incluir etiquetas (Label) y cuadros de texto
(Text) para mostrar la información. Además, agrega un botón para iniciar y
detener la recepción de datos.
▪ Implementa una función que se ejecute en segundo plano para leer
continuamente los datos recibidos del sensor y actualice la interfaz en
tiempo real.
▪ Agrega elementos gráficos como gráficos de línea utilizando la biblioteca
matplotlib para visualizar cómo cambian los valores del sensor en el tiempo.

4. Visualización y Pruebas:
Diseña la interfaz de manera que los datos se muestren de forma clara, utilizando
gráficos o tablas según sea necesario.
Asegúrate de que la interfaz reciba y muestre correctamente los valores del sensor MQ2,
tanto en su modo digital como analógico.
5. Documentación:
Incluye capturas de pantalla de la interfaz mostrando los datos recibidos.
Reflexiona sobre la utilidad de esta visualización para interpretar datos en aplicaciones
de telemetría y comunicaciones.
Entrega: Por repositorio de GitHub 29/10/2024
• Sube el código de la interfaz junto con un archivo README con el nombre de los integrantes
y tareas realizadas por cada uno, links de Figma o canva y que explique cómo conectar la PC
con el Arduino para recibir los datos correctamente.
• Incluye la documentación solicitada con capturas de pantalla y la reflexión.


Reflexion Final:
No nos gusta el trabajo, sin embargo hemos aprendido mucho sobre el camino, a trabajar en grupo y no solo ser un grupo, sino ser un equipo. Este trabajo nos hizo pensar, debatir, nos dio a conocer acerca de Flet, Tkinter, Python, Java, Swing, para lograr nuestros objetivos. Estos mismos, que fueron planteados casi desde el primer día en nuestro trabajo, así mismo como esta documentación, el tablero de Trello y los diseños de Figma. Cosas que en el proceso, de aprender acerca de la UI/UX nos sirvió para mejorar no solo en este trabajo, sino que también para otras materias. Por más de no ser un trabajo que disfrutamos, pudimos obtener conocimiento sobre temas y herramientas que estamos más que seguros que nos va a servir más adelante o actualmente con proyectos personales.
