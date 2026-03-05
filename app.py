import flet as ft

def main(page: ft.Page):
    # Configuración de la ventana
    page.title = "Examen Final - Registro de Participantes"
    page.padding = 20
    page.theme_mode = ft.ThemeMode.LIGHT

    # Variables de control
    txt_nombre = ft.TextField(label="Nombre completo")
    txt_email = ft.TextField(label="Correo electrónico")
    
    dd_taller = ft.Dropdown(
        label="Taller de interés",
        options=[
            ft.dropdown.Option("Python para Principiantes"),
            ft.dropdown.Option("Flet Intermedio"),
            ft.dropdown.Option("Análisis de Datos con Pandas"),
        ]
    )

    rg_pago = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="Pago completo", label="Pago completo"),
            ft.Radio(value="Pago por cuotas", label="Pago por cuotas"),
        ]),
        value="Pago completo"
    )

    chk_portatil = ft.Checkbox(label="Requiere computadora portátil", value=False)

    # Slider y su etiqueta dinámica
    lbl_nivel = ft.Text("Nivel: 1")
    def slider_changed(e):
        lbl_nivel.value = f"Nivel: {int(e.control.value)}"
        page.update()

    sld_experiencia = ft.Slider(
        min=1, max=5, divisions=4, value=1, on_change=slider_changed
    )

    # Área de resumen
    resumen_text = ft.Text(size=16, color=ft.colors.BLUE_900)

    # Función del botón
    def generar_ficha(e):
        portatil_str = "Sí" if chk_portatil.value else "No"
        
        resumen_text.value = (
            f"--- FICHA DEL PARTICIPANTE ---\n\n"
            f"Nombre: {txt_nombre.value}\n"
            f"Email: {txt_email.value}\n"
            f"Taller: {dd_taller.value}\n"
            f"Pago: {rg_pago.value}\n"
            f"Requiere Portátil: {portatil_str}\n"
            f"Nivel de Experiencia: {int(sld_experiencia.value)}\n\n"
            f"--- Gracias por su registro ---"
        )
        page.update()

    # Construcción de la Interfaz
    page.add(
        ft.Column(
            controls=[
                # Título
                ft.Row([ft.Text("Registro de Participantes", size=30, weight=ft.FontWeight.BOLD)], 
                    alignment=ft.MainAxisAlignment.CENTER),
                
                txt_nombre,
                txt_email,
                dd_taller,
                
                # Grupo de Radio con etiqueta
                ft.Column([
                    ft.Text("Modalidad de pago:", weight=ft.FontWeight.W_500),
                    rg_pago
                ], spacing=5),
                
                chk_portatil,
                
                # Slider con etiqueta
                ft.Column([
                    ft.Text("Nivel de experiencia en programación:"),
                    sld_experiencia,
                    lbl_nivel
                ], spacing=0),
                
                # Botón centrado
                ft.Row([
                    ft.ElevatedButton(
                        "Mostrar Ficha del Participante",
                        bgcolor=ft.colors.GREEN_400,
                        color=ft.colors.WHITE,
                        on_click=generar_ficha
                    )
                ], alignment=ft.MainAxisAlignment.CENTER),
                
                # Resultado
                resumen_text
            ],
            spacing=15,
            scroll=ft.ScrollMode.AUTO # Permite scroll si la ventana es pequeña
        )
    )

ft.app(target=main)