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

    def scroll_initialize(e):
        consoleView.scroll_to(offset=-1, duration=0)

    # page.theme = Theme(color_scheme_seed=Colors.GREEN)
    page.theme_mode = ThemeMode.LIGHT
    toggleDarkMode = IconButton(
        on_click=change_theme,
        icon=Icons.DARK_MODE,
        selected_icon=Icons.LIGHT_MODE,
    )

    page.appbar = AppBar(
        leading=Icon(Icons.RADIO_BUTTON_CHECKED),
        title=Text("MC Server Manager"),
        center_title=False,
        bgcolor=colors.SURFACE_VARIANT,     # Colorsで未実装のため非推奨のcolorsを使用
        actions=[
            toggleDarkMode,
            IconButton(Icons.FILTER_3),
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

    def testText(num):
        text = Text(
            f"This is Console {num}",
            font_family="Consolas",
            selectable=True,
        )
        return text

    consoleView = ListView(
        expand=True,
        spacing=0,
        controls=[],
    )

    for i in range(0, 100):
        consoleView.controls.append(testText(i))

    tabMain = Tabs(
        selected_index=0,
        animation_duration=300,
        on_change=scroll_initialize,
        tabs=[
            Tab(
                text="DashBoard",
                icon=Icons.SPACE_DASHBOARD,
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
                                            bgcolor=Colors.PRIMARY_CONTAINER,
                                            expand=True,
                                            margin=10,
                                            key="A1",
                                        ),
                                        Container(
                                            Text("Section A2", size=24),
                                            alignment=alignment.center,
                                            bgcolor=Colors.PRIMARY_CONTAINER,
                                            expand=True,
                                            margin=10,
                                            key="A2",
                                        ),
                                    ]
                                ),
                                Container(
                                    Text("Section B", size=24),
                                    alignment=alignment.center,
                                    bgcolor=Colors.SECONDARY_CONTAINER,
                                    expand=2,
                                    margin=10,
                                    key="B",
                                ),
                                Container(
                                    Text("Section C", size=24),
                                    alignment=alignment.center,
                                    bgcolor=Colors.TERTIARY_CONTAINER,
                                    expand=1,
                                    margin=10,
                                    key="C",
                                ),
                            ]
                        ),
                        Container(
                            Text("Section D", size=24),
                            alignment=alignment.center,
                            bgcolor=Colors.TERTIARY_CONTAINER,
                            expand=True,
                            margin=10,
                            key="D",
                        ),
                    ]
                )
            ),
            Tab(
                text="Console",
                icon=Icons.WYSIWYG,
                content=Column(
                    alignment=MainAxisAlignment.SPACE_AROUND,
                    controls=[
                        Container(
                            consoleView,
                            alignment=alignment.center,
                            border=border.all(1, Colors.OUTLINE),
                            border_radius=border_radius.all(5),
                            expand=True,
                            margin=margin.symmetric(10, 0),
                            padding=padding.symmetric(0, 5),
                        ),
                        Container(
                            content=TextField(
                                label="Enter the command",
                                border_color=Colors.OUTLINE,
                                focused_border_color=Colors.PRIMARY,
                            )
                        )
                    ]
                ),
            ),
            Tab(
                text="Settings",
                icon=Icons.SETTINGS,
                content=Container(
                    alignment=alignment.center,
                    content=Text("This is Tab 3"),
                ),
            ),
        ],
        expand=1,
    )

    page.add(tabMain)
    scroll_initialize(None)

app(main)