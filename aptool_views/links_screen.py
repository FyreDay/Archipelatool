import subprocess

import flet as ft
from functools import partial

from app_colors import AppColors


def links_screen(page: ft.Page):
    def on_result(e: ft.FilePickerResultEvent):
        if e.files:
            python_file_path = file_picker.result.files[0].path
            # Run the selected Python file
            print(python_file_path)
            subprocess.Popen(["python", python_file_path])

    file_picker = ft.FilePicker(on_result=on_result)
    selected_files = ft.Text()

            # subprocess.Popen(["python", python_file_path])

    def open_file_dialog(e):
        file_picker.pick_files(allowed_extensions=["py"], allow_multiple=False)

    def generate_yamls():
        from Options import generate_yaml_templates

        target = Utils.user_path("Players", "Templates")
        generate_yaml_templates(target, False)
        open_folder(target)

    # Set up the page
    page.overlay.append(file_picker)
    run_button = ft.ElevatedButton("Run Selected Script")
    browse_button = ft.ElevatedButton("Browse for Python Script", on_click=open_file_dialog)

    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=AppColors.pink,
            primary_container=AppColors.pink,
            secondary=AppColors.pink,
            background=AppColors.mainBack,
            surface=AppColors.altBack,
            on_primary=AppColors.mainBack,
            on_background=AppColors.mainText,
            surface_bright=AppColors.specialBack,
        ),
        font_family="Roboto",
        use_material3=True,
    )

    search_field = ft.TextField(
        label="Search clients...",
        border_color=AppColors.specialBack,
        bgcolor=AppColors.altBack,
        color=AppColors.mainText,
        cursor_color=AppColors.pink,
        selection_color=AppColors.pink,
        label_style=ft.TextStyle(color=AppColors.pink),
        expand=False,
    )

    return ft.View(
        route="/links",
        controls=[
            ft.AppBar(
                title=ft.Row(
                    controls=[
                        ft.Icon(name=ft.Icons.LINK_ROUNDED, color=AppColors.mainBack),
                        ft.Text("Links", color=AppColors.mainBack, size=20),
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                bgcolor=AppColors.pink,
                leading=ft.IconButton(
                    icon=ft.Icons.ARROW_BACK,
                    icon_color=AppColors.mainBack,
                    on_click=lambda e: page.go("/")
                )
            ),
            search_field,
            run_button,
            browse_button
        ],
        bgcolor=AppColors.mainBack
    )