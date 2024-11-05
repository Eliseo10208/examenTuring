import tkinter as tk


class TuringMachine:
    def __init__(self, tape):
        self.tape = list(tape) + ['_'] * 100  
        self.head = 0
        self.state = 'q0'

    def step(self):
        current_char = self.tape[self.head]
        if self.state == 'q0':
            if current_char == 'a':
                self.tape[self.head] = 'X'
                self.head += 1
                self.state = 'q1'
            elif current_char == '_':
                self.state = 'q_accept'
            else:
                self.state = 'q_reject'
        elif self.state == 'q1':
            if current_char == 'a':
                self.head += 1
            elif current_char == 'b':
                self.tape[self.head] = 'Y'
                self.head += 1
                self.state = 'q2'
            else:
                self.state = 'q_reject'
        elif self.state == 'q2':
            if current_char == 'b':
                self.head += 1
            elif current_char == 'c':
                self.tape[self.head] = 'Z'
                self.head += 1
                self.state = 'q3'
            else:
                self.state = 'q_reject'
        elif self.state == 'q3':
            if current_char == 'c':
                self.head += 1
            elif current_char == '_':
                self.state = 'q_accept'
            else:
                self.state = 'q_reject'

    def is_halted(self):
        return self.state in ['q_accept', 'q_reject']

    def is_accepted(self):
        return self.state == 'q_accept'


def run_machine():
    tape_input = entry.get()
    tm = TuringMachine(tape_input)
    while not tm.is_halted():
        tm.step()
    
    if tm.is_accepted():
        result.set("Cadena válida: ")
    else:
        result.set("Cadena no válida")


root = tk.Tk()
root.title("Validador de Máquina de Turing a^n b^n c^n")

label = tk.Label(root, text="Ingrese la cadena:")
label.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

btn_run = tk.Button(root, text="Validar Cadena", command=run_machine)
btn_run.pack(pady=5)

result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, font=("Courier", 12), fg="blue")
result_label.pack(pady=10)

root.mainloop()
