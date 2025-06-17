import tkinter as tk
from tkinter import filedialog
import src
import src_01


class Window:
    def __init__(self) -> None:
        
        self.root = tk.Tk()
        self.root.title('Image to PDF')
        self.root.geometry('600x400')

        self.master_frame = tk.Frame(master=self.root)
        self.master_frame.pack()

        self.lbl = tk.Label(master=self.master_frame, text='Hello Mother',
                    font=('consolas', 15, 'bold'))
        self.lbl.pack(pady=10)

        self.choose_button = tk.Button(master=self.master_frame, font=('consolas', 10, 'bold'),
                                       text='Choose Images', bg='green',
                                       command=self.choose_img)
        self.choose_button.pack(pady=10)

        self.convert_button = tk.Button(master=self.master_frame, font=('consolas', 10, 'bold'),
                                       text='Convert to PDF', bg='green')
        self.convert_button.pack(pady=10)

        self.message = tk.Label(master=self.master_frame, text='', fg='red',
                                font=('consolas', 13, 'bold'))
        self.message.pack(pady=15)

        self.root.mainloop()

    def choose_img(self):
        self.message.config(text='')
        
        # Open windows explorer to take the filepath form user
        filepath = tk.filedialog.askopenfilenames(
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;")])
        
        print(filepath)
        
        if not filepath:
            return None
        
        else:
            try:
                src_01.convert(filepath)
                self.message.config(text=f'You converted {len(filepath)} images to PDF successfully!')

            except Exception as e:
                self.message.config(text='Something went wrong! Call your son...')
                print(e)
                return False
