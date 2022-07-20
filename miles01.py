import flet
from flet import ElevatedButton, Page, Text, TextField
from random import randint

def main(page: Page):

    def textbox_focused(e):
        tb1.value=""
        page.update()

    def button_clicked(e):
        regu = 0
        bien = 0
        t = tb1.value
        t = list(dict.fromkeys(list(t)))
        if len(t) < 4:
            print(f"pre focus- {t} ", end="-")
            tb1.focus()
            page.update()
            print("post focus")
        else: 
            for i in range(len(t)):
                if t[i] in m:
                    if t[i] == m[i]:
                        bien += 1
                    else:
                        regu += 1
            page.add(Text(f"{''.join(t)}: {bien} bien y {regu} regular"))
            if bien == 4:
                page.add(Text(f"Jujujuuuuu"))
        tb1.focus()
        page.update()

    m = ""
    while len(m) < 4:
        m = randint(1000, 9999)
        m = list(dict.fromkeys(list(str(m))))
    print(m)

    tb1 = TextField(
        label="Ingrese su disparo:",
        on_focus=textbox_focused,
        width=300,
    )
    b = ElevatedButton(text="Probar tiro", on_click=button_clicked)
    page.add(tb1, b)
    page.update()

flet.app(target=main)

