import flet as ft
import datetime

def main(page: ft.Page):
    dp = ft.DatePicker(
        cancel_text='Cancelar',
        confirm_text='Confirmar',
        error_format_text='Data Invalida',
        field_hint_text='MM/DD/YYYY',
        field_label_text='Selecione uma data',
        help_text='Selecione uma data no calendario',
        switch_to_calendar_icon=ft.icons.CALENDAR_MONTH,
        switch_to_input_icon=ft.icons.EDIT,
        date_picker_mode=ft.DatePickerMode.YEAR,
        on_change=lambda _: print(dp.value),
        value=datetime.date(2024, 1, 5),
        first_date=datetime.date(2024, 1, 20),
        last_date=datetime.date(2024, 1, 30),
        error_invalid_text='Data fora do limite',

        

    )
    page.overlay.append(dp)
    btn = ft.ElevatedButton('Abrir', on_click=lambda _: dp.pick_date())
    page.add(btn)
    
   
if __name__==('__main__'):
    ft.app(target=main)