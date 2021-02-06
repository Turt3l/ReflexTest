import PySimpleGUI as sg
import time
import random
def wait():
    time.sleep(random.randint(0, 20))
sg.theme('DarkRed1')
wait()
start = time.time()
layout = [
    [sg.Text('Reaction test')],
    [sg.Text('Press the button once it appears')],
    [sg.Submit('Click!')]
]
window = sg.Window('Reaction tester', layout)
event, values = window.read()
end = time.time()
print(end - start)
