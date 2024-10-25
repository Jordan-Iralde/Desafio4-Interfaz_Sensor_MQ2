import flet as ft 

def main(page: ft.Page):    #Creamos la ventana principal y adentro de esto es donde va a estar todo practicamente
    page.title = "Calculadora"
    result = ft.Text(value="0")

    page.add(# page.add seria como la funcion para agregar elementos a la aplicacion
       ft.Row(controls=[result]),
       ft.Row( #Row seria la funcion de ordenar los elementos uno al lado del otro de manera horizontal, la variable controls la desconozco, pero por logica me imagino que es parte de la funcion
            controls = [
                ft.ElevatedButton(text="AC"),
                ft.ElevatedButton(text="+/-"),
                ft.ElevatedButton(text="%"),
                ft.ElevatedButton(text="/"),
            ]
       ), 
       ft.Row(
            controls = [
                ft.ElevatedButton(text="7"),
                ft.ElevatedButton(text="8"),
                ft.ElevatedButton(text="9"),
                ft.ElevatedButton(text="*")

            ]
       ), #se cierra la funcion row con , como si fuera ; 
       ft.Row(
            controls=[
                ft.ElevatedButton(text="4"),
                ft.ElevatedButton(text="5"),
                ft.ElevatedButton(text="6"),
                ft.ElevatedButton(text="-"),
            ]
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="1"),
                ft.ElevatedButton(text="2"),
                ft.ElevatedButton(text="3"),
                ft.ElevatedButton(text="+"),
            ]
        ),
        ft.Row(
             controls=[
                ft.ElevatedButton(text="0"),
                ft.ElevatedButton(text="."),
                ft.ElevatedButton(text="="),
            ]
        ),
    )

ft.app(main)# es para ejecutar la ventana