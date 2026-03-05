import flet as ft
def main(page: ft.Page):
    page.title= "Ficha de registro de usuarios ;>"
    page.padding = 20
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    
    nombre = ft.TextField(
        value="",
        label="Nombre completo",
        width=100,
        size=24,
        color=ft.Colors.BLUE,
        weight=ft.FontWeight.BOLD,
        italic=False,
        text_align=ft.TextAlign.CENTER,
    )
    
    correo = ft.TextField(
        value="",
        label="Correo Electronico",
        width=100,
        size=24,
        max_length=100,
        color=ft.Colors.BLUE,
        weight=ft.FontWeight.BOLD,
        italic=False,
        text_align=ft.TextAlign.CENTER
    )
    
    
    modalidad_pago = ft.RadioGroup(
    content=ft.Column([
        ft.Radio(value="Completo", label="Pago Completo"),
        ft.Radio(value="Cuotas", label="Pago por cuotas"),
    ]),
    value="Completo",
    on_change=lambda e: print(f"Seleccionado: {e.control.value}")
)
    
    def dropdown_changed(e):
        resultado.value = f"Seleccionaste: {taller_interes.value}"
        page.update()
    
    resultado = ft.Text()
    
    taller_interes = ft.Dropdown(
        width=300,
        label="Selecciona tu taller",
        on_change=dropdown_changed,
        options=[
            ft.dropdown.Option("Python para Principiantes"),
            ft.dropdown.Option("Flet Intermedio"),
            ft.dropdown.Option("Análisis de Datos con Pandas"),
        ],
    )
    
    
    requerimentos=ft.Checkbox(
    label="Requiere computadora portatil",
    value=False,
    tristate=False,
    check_color=ft.Colors.WHITE,
    fill_color=ft.Colors.GREEN,
    on_change=lambda e: print(f"Estado: {e.control.value}")
    )
    
    
    nivel = ft.Text("Nivel: 1")
    def slider_changed(e):
        nivel.value = f"Nivel: {int(e.control.value)}"
        page.update()
        
    experiencia = ft.Slider(
        min=1, max=5, divisions=4, value=1, on_change=slider_changed
    )
    
    
    resumen= ft.Text(size=16, color=ft.colors.BLUE_900)
    
    def generar_ficha(e):
        requerimentos = "Sí" if requerimentos.value else "No"
        
        resumen_text.value = (
            f"--- FICHA DEL PARTICIPANTE ---\n\n"
            f"Nombre: {nombre.value}\n"
            f"Email: {correo.value}\n"
            f"Taller: {taller_interes.value}\n"
            f"Pago: {modalidad_pago.value}\n"
            f"Requiere Portátil: {requerimentos}\n"
            f"Nivel de Experiencia: {int(experiencia.value)}\n\n"
            f"--- Gracias por su registro ---"
        )
        page.update()






    
    
    
    page.add(
        ft.Column(
            controls=[
                # Título
                ft.Row([ft.Text("Registro de Participantes", size=30, weight=ft.FontWeight.BOLD)], 
                    alignment=ft.MainAxisAlignment.CENTER),
                
                nombre,
                correo,
                taller_interes,
                ft.Column([
                    ft.Text("Modalidad de pago:", weight=ft.FontWeight.W_500),
                    modalidad_pago
                ], spacing=5),
                
                requerimentos,
                ft.Column([
                    ft.Text("Nivel de experiencia:"),
                    experiencia,
                    nivel
                ], spacing=0),
                ft.Row([
                    ft.ElevatedButton(
                        "Mostrar Ficha del Participante",
                        bgcolor=ft.colors.GREEN_400,
                        color=ft.colors.WHITE,
                        on_click=generar_ficha
                    )
                ], alignment=ft.MainAxisAlignment.CENTER),
                resumen
            ],
        )
    )
    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

ft.app(target=main)
