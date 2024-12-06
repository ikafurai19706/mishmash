# encoding: utf-8
from flet import *
import time

def main(page: Page):
    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()

    def change_theme(e):
        # page.splash.visible = True
        page.theme_mode = ThemeMode.LIGHT if page.theme_mode == ThemeMode.DARK else ThemeMode.DARK
        page.update()
        # time.sleep(0.3)
        toggleDarkMode.selected = not toggleDarkMode.selected
        page.update()

    # page.theme = Theme(color_scheme_seed=colors.GREEN)
    page.theme_mode = ThemeMode.LIGHT
    toggleDarkMode = IconButton(
        on_click=change_theme,
        icon=icons.DARK_MODE,
        selected_icon=icons.LIGHT_MODE,
    )

    page.appbar = AppBar(
        leading=Icon(icons.RADIO_BUTTON_CHECKED),
        title=Text("MC Server Manager"),
        center_title=False,
        bgcolor=colors.SURFACE_VARIANT,
        actions=[
            toggleDarkMode,
            IconButton(icons.FILTER_3),
            PopupMenuButton(
                items=[
                    PopupMenuItem(text="Item 1"),
                    PopupMenuItem(),  # divider
                    PopupMenuItem(
                        text="Checked item", checked=False, on_click=check_item_clicked
                    ),
                ]
            ),
        ],
    )

    consoleArea = ListView(
        expand=True,
        auto_scroll=True,
    )

    for i in range(0, 100):
        consoleArea.controls.append(Text(
            f"This is Console {i}",
            font_family="Consolas",
            selectable=True,
        ))

    tabMain = Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            Tab(
                text="DashBoard",
                icon=icons.SPACE_DASHBOARD,
                content=Column(
                    alignment=MainAxisAlignment.SPACE_AROUND,
                    controls=[
                        Row(
                            alignment=MainAxisAlignment.SPACE_AROUND,
                            expand=True,
                            controls=[
                                Column(
                                    alignment=MainAxisAlignment.SPACE_AROUND,
                                    expand=3,
                                    controls=[
                                        Container(
                                            Text("Section A1", size=24),
                                            alignment=alignment.center,
                                            bgcolor=colors.PRIMARY_CONTAINER,
                                            expand=True,
                                            margin=10,
                                            key="A1",
                                        ),
                                        Container(
                                            Text("Section A2", size=24),
                                            alignment=alignment.center,
                                            bgcolor=colors.PRIMARY_CONTAINER,
                                            expand=True,
                                            margin=10,
                                            key="A2",
                                        ),
                                    ]
                                ),
                                Container(
                                    Text("Section B", size=24),
                                    alignment=alignment.center,
                                    bgcolor=colors.SECONDARY_CONTAINER,
                                    expand=2,
                                    margin=10,
                                    key="B",
                                ),
                                Container(
                                    Text("Section C", size=24),
                                    alignment=alignment.center,
                                    bgcolor=colors.TERTIARY_CONTAINER,
                                    expand=1,
                                    margin=10,
                                    key="C",
                                ),
                            ]
                        ),
                        Container(
                            Text("Section D", size=24),
                            alignment=alignment.center,
                            bgcolor=colors.TERTIARY_CONTAINER,
                            expand=True,
                            margin=10,
                            key="D",
                        ),
                    ]
                )
            ),
            Tab(
                text="Console",
                icon=icons.WYSIWYG,
                content=Column(
                    alignment=MainAxisAlignment.SPACE_AROUND,
                    controls=[
                        Container(
                            Container(
                                consoleArea,
                                alignment=alignment.top_left,
                                margin=margin.symmetric(0, 5),
                                expand=True,
                                bgcolor=colors.ERROR_CONTAINER
                            ),
                            alignment=alignment.center,
                            border=border.all(1, colors.OUTLINE),
                            border_radius=border_radius.all(5),
                            expand=True,
                            margin=margin.symmetric(10, 0),
                        ),
                        Container(
                            content=TextField(
                                label="Enter the command",
                                border_color=colors.OUTLINE,
                                focused_border_color=colors.PRIMARY,
                            )
                        )
                    ]
                ),
            ),
            Tab(
                text="Settings",
                icon=icons.SETTINGS,
                content=Container(
                    alignment=alignment.center,
                    content=Text("This is Tab 3"),
                ),
            ),
        ],
        expand=1,
    )

    page.add(tabMain)

app(main)