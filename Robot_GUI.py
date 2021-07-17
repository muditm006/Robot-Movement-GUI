import tkinter as tk
import requests


def move_forward():
    requests.request(method='GET', url="http://192.168.1.116:8080/fwd")


def move_backward():
    requests.request(method='GET', url="http://192.168.1.116:8080/rev")


def move_left():
    requests.request(method='GET', url="http://192.168.1.116:8080/left")


def move_right():
    requests.request(method='GET', url="http://192.168.1.116:8080/right")


UI = tk.Tk()

forward_button = tk.Button(text="Forward", width=15, height=10, background="red", foreground="blue", command=move_forward, font=('Verdana',12,'underline'))
left_button = tk.Button(text="Left", width=15, height=10, background="green", foreground="orange", command=move_left, font=('Verdana',12,'underline'))
right_button = tk.Button(text="Right", width=15, height=10, background="yellow", foreground="purple", command=move_right, font=('Verdana',12,'underline'))
backward_button = tk.Button(text="Backward", width=15, height=10, background="pink", foreground="white", command=move_backward, font=('Verdana',12,'underline'))
header = tk.Label(text="Mudit's Python GUI", background="white", foreground="black")

forward_button.pack()
left_button.pack()
right_button.pack()
backward_button.pack()
header.pack()
UI.mainloop()
