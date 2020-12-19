import PySimpleGUI as sg

# Demo of how columns work
# GUI has on row 1 a vertical slider followed by a COLUMN with 7 rows
# Prior to the Column element, this layout was not possible
# Columns layouts look identical to GUI layouts, they are a list of lists of elements.

sg.ChangeLookAndFeel('BlueMono')

# Column layout
col = [[sg.Text('col Row 1', text_color='white', background_color='blue')],
       [sg.Text('col Row 2', text_color='white', background_color='blue'), sg.Input('col input 1')],
       [sg.Text('col Row 3', text_color='white', background_color='blue'), sg.Input('col input 2')]]

layout = [[sg.Listbox(values=('Listbox Item 1', 'Listbox Item 2', 'Listbox Item 3'),
                      select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE, size=(20, 3)),
           sg.Column(col, background_color='blue')],
          [sg.Input('Last input')],
          [sg.OK()]]

# Display the Window and get values

event, values = sg.Window('Compact 1-line Window with column', layout).Read()

sg.popup(event, values, line_width=200)