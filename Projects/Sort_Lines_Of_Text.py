import PySimpleGUI as sg

# layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")]]
sg.theme('GreenTan')  # Add a touch of color
# All the stuff inside your window.
layout = [
    [sg.Multiline(size=(120, 20), key="textbox")],
    [sg.Button("Sort")],
    [sg.Multiline(size=(120, 20), key="textbox_2")]
]

window = sg.Window("Sort Lines of Text", layout, element_justification='c')

while True:
    event, values = window.read()
    if event == "Sort":
        lines = values["textbox"].split("\n")
        lines.sort()
        # Append Sorted List to Sorted Textbox
        for i in lines:
            text = window["textbox_2"]
            if text.get() == "":
                text.update(text.get() + i)
            else:
                text.update(text.get() + "\n" + i)

    elif event == sg.WIN_CLOSED:
        break

window.close()
