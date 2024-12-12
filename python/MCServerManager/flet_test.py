# encoding: utf-8
import flet as ft
import asyncio  # 次の機能で使う

def main(page: ft.Page):
    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()

    def change_theme(e):
        # page.splash.visible = True
        page.theme_mode = ft.ThemeMode.LIGHT if page.theme_mode == ft.ThemeMode.DARK else ft.ThemeMode.DARK
        page.update()
        # time.sleep(0.3)
        toggleDarkMode.selected = not toggleDarkMode.selected
        page.update()

    def scroll_initialize(e):
        consoleView.scroll_to(offset=-1, duration=0)

    def server_buttons_toggle(e):
        if serverButtonsRow.controls == buttonsIdling:
            serverButtonsRow.controls = buttonsRunning
        else:
            serverButtonsRow.controls = buttonsIdling
        page.update()

    page.title = "Minecraft Server Manager"
    # page.theme = Theme(color_scheme_seed=Colors.GREEN)
    page.theme_mode = ft.ThemeMode.LIGHT
    toggleDarkMode = ft.IconButton(
        on_click=change_theme,
        icon=ft.Icons.DARK_MODE,
        selected_icon=ft.Icons.LIGHT_MODE,
    )

    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.Icons.RADIO_BUTTON_CHECKED),
        title=ft.Text("MC Server Manager"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,     # Colorsで未実装のため非推奨のcolorsを使用
        actions=[
            toggleDarkMode,
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Item 1"),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        text="Checked item", checked=False, on_click=check_item_clicked
                    ),
                ]
            ),
        ],
    )

    txt = """\
itomaki@syscom315-1 MINGW64 ~/Documents/mishmash (main)
$ flet run python/MCServerManager/flet_test.py -d
C:\\Users\\itomaki\\Documents\\mishmash\\python\\MCServerManager\\flet_test.py:34: DeprecationWarning: colors enum is deprecated since version 0.25.0 and will be removed in version 0.28.0. Use Colors enum instead.
  bgcolor=colors.SURFACE_VARIANT,     # Colorsで未実装のため非推奨のcolorsを使用
C:\\Users\\itomaki\\Documents\\mishmash\\python\\MCServerManager\\flet_test.py:34: DeprecationWarning: colors enum is deprecated since version 0.25.0 and will be removed in version 0.28.0. Use Colors enum instead.
  bgcolor=colors.SURFACE_VARIANT,     # Colorsで未実装のため非推奨のcolorsを使用
C:\\Users\\itomaki\\Documents\\mishmash\\python\\MCServerManager\\flet_test.py:34: DeprecationWarning: colors enum is deprecated since version 0.25.0 and will be removed in version 0.28.0. Use Colors enum instead.
  bgcolor=colors.SURFACE_VARIANT,     # Colorsで未実装のため非推奨のcolorsを使用
C:\\Users\\itomaki\\Documents\\mishmash\\python\\MCServerManager\\flet_test.py:34: DeprecationWarning: colors enum is deprecated since version 0.25.0 and will be removed in version 0.28.0. Use Colors enum instead.
  bgcolor=colors.SURFACE_VARIANT,     # Colorsで未実装のため非推奨のcolorsを使用
itomaki@syscom315-1 MINGW64 ~/Documents/mishmash (main)
$ flet run python/MCServerManager/flet_test.py -d
C:\\Users\\itomaki\\Documents\\mishmash\\python\\MCServerManager\\flet_test.py:34: DeprecationWarning: colors enum is deprecated since version 0.25.0 and will be removed in version 0.28.0. Use Colors enum instead.
  bgcolor=colors.SURFACE_VARIANT,     # Colorsで未実装のため非推奨のcolorsを使用
C:\\Users\\itomaki\\Documents\\mishmash\\python\\MCServerManager\\flet_test.py:34: DeprecationWarning: colors enum is deprecated since version 0.25.0 and will be removed in version 0.28.0. Use Colors enum instead.
  bgcolor=colors.SURFACE_VARIANT,     # Colorsで未実装のため非推奨のcolorsを使用
C:\\Users\\itomaki\\Documents\\mishmash\\python\\MCServerManager\\flet_test.py:34: DeprecationWarning: colors enum is deprecated since version 0.25.0 and will be removed in version 0.28.0. Use Colors enum instead.
  bgcolor=colors.SURFACE_VARIANT,     # Colorsで未実装のため非推奨のcolorsを使用
C:\\Users\\itomaki\\Documents\\mishmash\\python\\MCServerManager\\flet_test.py:34: DeprecationWarning: colors enum is deprecated since version 0.25.0 and will be removed in version 0.28.0. Use Colors enum instead.
  bgcolor=colors.SURFACE_VARIANT,     # Colorsで未実装のため非推奨のcolorsを使用
itomaki@syscom315-1 MINGW64 ~/Documents/mishmash (main)
$ flet run python/MCServerManager/flet_test.py -d
C:\\Users\\itomaki\\Documents\\mishmash\\python\\MCServerManager\\flet_test.py:34: DeprecationWarning: colors enum is deprecated since version 0.25.0 and will be removed in version 0.28.0. Use Colors enum instead.
  bgcolor=colors.SURFACE_VARIANT,     # Colorsで未実装のため非推奨のcolorsを使用
C:\\Users\\itomaki\\Documents\\mishmash\\python\\MCServerManager\\flet_test.py:34: DeprecationWarning: colors enum is deprecated since version 0.25.0 and will be removed in version 0.28.0. Use Colors enum instead.
  bgcolor=colors.SURFACE_VARIANT,     # Colorsで未実装のため非推奨のcolorsを使用
C:\\Users\\itomaki\\Documents\\mishmash\\python\\MCServerManager\\flet_test.py:34: DeprecationWarning: colors enum is deprecated since version 0.25.0 and will be removed in version 0.28.0. Use Colors enum instead.
  bgcolor=colors.SURFACE_VARIANT,     # Colorsで未実装のため非推奨のcolorsを使用
C:\\Users\\itomaki\\Documents\\mishmash\\python\\MCServerManager\\flet_test.py:34: DeprecationWarning: colors enum is deprecated since version 0.25.0 and will be removed in version 0.28.0. Use Colors enum instead.
  bgcolor=colors.SURFACE_VARIANT,     # Colorsで未実装のため非推奨のcolorsを使用\
"""

    print(txt)

    text_t = ft.Text(
        value=txt,
        selectable=True,
        font_family="Consolas",
        no_wrap=True,
        color=ft.Colors.ON_SURFACE_VARIANT,
        style=ft.TextStyle(
            height=1.2,
        )
    )

    consoleView = ft.Column(
        spacing=0,
        controls=[text_t],
        scroll=ft.ScrollMode.ALWAYS
    )

    startButton = ft.FilledButton(
        text="START  ",
        icon=ft.Icons.PLAY_ARROW,
        on_click=server_buttons_toggle,
        style=ft.ButtonStyle(
            padding=ft.padding.symmetric(0, 5),
            # shape=RoundedRectangleBorder(5),
        )
    )

    stopButton = ft.FilledButton(
        text="STOP  ",
        icon=ft.Icons.STOP,
        style=ft.ButtonStyle(
            padding=ft.padding.symmetric(0, 5),
            # shape=RoundedRectangleBorder(5),
        )
    )

    killButton = ft.FilledButton(
        text="KILL  ",
        icon=ft.Icons.CANCEL_OUTLINED,
        style=ft.ButtonStyle(
            padding=ft.padding.symmetric(0, 5),
            # shape=RoundedRectangleBorder(5),
        )
    )

    buttonsIdling = [startButton]

    buttonsRunning = [killButton, stopButton]

    serverButtonsRow = ft.Row(
        controls=buttonsIdling,
        expand=True,
        alignment=ft.MainAxisAlignment.END,
    )

    headerControls = [
        ft.Icon(
            ft.Icons.DOMAIN,
            color=ft.Colors.PRIMARY,
        ),
        ft.Text(
            "Server-Server",
            size=24,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.PRIMARY,
        ),
        serverButtonsRow,
    ]

    header = ft.Container(
        ft.Column([
            ft.Row(
                headerControls,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
            ),
            ft.Text("This is a motd of a motd that is motd by a motd")
        ]),
        #border=border.only(bottom=border.BorderSide(1, Colors.OUTLINE_VARIANT)),
        padding=ft.padding.only(10, 5, 10, 15),
    )

    tabMain = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        on_change=scroll_initialize,
        scrollable=False,
        
        tabs=[
            ft.Tab(
                text="DashBoard",
                icon=ft.Icons.SPACE_DASHBOARD,
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    controls=[
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                            expand=True,
                            controls=[
                                ft.Column(
                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                    expand=3,
                                    controls=[
                                        ft.Container(
                                            ft.Text("Section A1", size=24),
                                            alignment=ft.alignment.center,
                                            bgcolor=ft.Colors.PRIMARY_CONTAINER,
                                            expand=True,
                                            margin=10,
                                            key="A1",
                                        ),
                                        ft.Container(
                                            ft.Text("Section A2", size=24),
                                            alignment=ft.alignment.center,
                                            bgcolor=ft.Colors.PRIMARY_CONTAINER,
                                            expand=True,
                                            margin=10,
                                            key="A2",
                                        ),
                                    ]
                                ),
                                ft.Container(
                                    ft.Text("Section B", size=24),
                                    alignment=ft.alignment.center,
                                    bgcolor=ft.Colors.SECONDARY_CONTAINER,
                                    expand=2,
                                    margin=10,
                                    key="B",
                                ),
                                ft.Container(
                                    ft.Text("Section C", size=24),
                                    alignment=ft.alignment.center,
                                    bgcolor=ft.Colors.TERTIARY_CONTAINER,
                                    expand=1,
                                    margin=10,
                                    key="C",
                                ),
                            ]
                        ),
                        ft.Container(
                            ft.Text("Section D", size=24),
                            alignment=ft.alignment.center,
                            bgcolor=ft.Colors.TERTIARY_CONTAINER,
                            expand=True,
                            margin=10,
                            key="D",
                        ),
                    ]
                )
            ),
            ft.Tab(
                text="Console",
                icon=ft.Icons.WYSIWYG,
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    controls=[
                        ft.Container(
                            ft.ListView(
                                controls=[consoleView],
                                spacing=0,
                                horizontal=True,
                                width=consoleView.width,
                            ),
                            alignment=ft.alignment.center,
                            border=ft.border.all(1, ft.Colors.OUTLINE),
                            border_radius=ft.border_radius.all(5),
                            expand=True,
                            margin=ft.margin.symmetric(10, 0),
                            padding=ft.padding.symmetric(0, 5),
                        ),
                        ft.Container(
                            content=ft.TextField(
                                label="Enter the command",
                                border_color=ft.Colors.OUTLINE,
                                focused_border_color=ft.Colors.PRIMARY,
                            )
                        )
                    ]
                ),
            ),
            ft.Tab(
                text="Settings",
                icon=ft.Icons.SETTINGS,
                content=ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.Text("This is Tab 3"),
                ),
            ),
        ],
        expand=1,
    )

    page.add(header)
    page.add(tabMain)
    scroll_initialize(None)

ft.app(main)