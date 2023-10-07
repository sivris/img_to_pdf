import tkinter as tk
from tkinter import filedialog
import src


class Window:
    def __init__(self) -> None:
        
        self.root = tk.Tk()
        self.root.title('Image to PDF')
        self.root.geometry('400x200')

        self.master_frame = tk.Frame(master=self.root)
        self.master_frame.pack()

        self.lbl = tk.Label(master=self.master_frame, text='Hello Mother',
                    font=('consolas', 15, 'bold'))
        self.lbl.pack(pady=10)

        self.choose_button = tk.Button(master=self.master_frame,
                                       text='Choose Image', bg='green',
                                       command=self.choose_img)
        self.choose_button.pack(pady=10)

        self.message = tk.Label(master=self.master_frame, text='', fg='red',
                                font=('consolas', 13, 'bold'))
        self.message.pack(pady=15)

        self.root.mainloop()

    def choose_img(self):
        self.message.config(text='')
        
        # Open windows explorer to take the filepath form user
        filepath = tk.filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;")])
        
        if not filepath:
            return None
        
        if src.convert(filepath):
            self.message.config(text='SUCCESSFUL')
