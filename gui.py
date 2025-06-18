import tkinter as tk
from tkinter import filedialog
import src
import src_01
from PIL import Image, ImageTk


class Window:
    def __init__(self) -> None:
        
        self.root = tk.Tk()
        self.root.title('Image to PDF')
        self.root.geometry('1600x900')

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

        # ----------------- 2nd frame ----------------------
        self.second_frame = tk.Frame(master=self.root)
        self.second_frame.pack()

        #list for the image labels
        self.labels_list = []
        self.images_list = []

        # images labels
        self.img1_label = tk.Label(self.second_frame)
        self.labels_list.append(self.img1_label)
        self.img1_label.grid(row=0, column=0, padx=10, pady=15)

        self.img2_label = tk.Label(self.second_frame)
        self.labels_list.append(self.img2_label)
        self.img2_label.grid(row=0, column=1, padx=10, pady=15)

        self.img3_label = tk.Label(self.second_frame)
        self.labels_list.append(self.img3_label)
        self.img3_label.grid(row=1, column=0, padx=10, pady=15)

        self.img4_label = tk.Label(self.second_frame)
        self.labels_list.append(self.img4_label)
        self.img4_label.grid(row=1, column=1, padx=10, pady=15)

        self.clear_button = tk.Button(master=self.master_frame, font=('consolas', 10, 'bold'),
                                       text='Clear Images', bg='red')
        self.clear_button.pack(pady=10)


        self.root.mainloop()

    def choose_img(self):
        self.message.config(text='')
        
        # Open windows explorer to take the filepath from user
        filepath = tk.filedialog.askopenfilenames(
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;")])
        
        print(filepath)
        
        if not filepath:
            return None
        
        else:
            try:

                for img_fp in filepath:
                    img = Image.open(img_fp)
                    img.thumbnail((250, 950))
                    img = img.convert('RGB')
                    img = ImageTk.PhotoImage(img)
                    self.images_list.append(img)
                
                self.images_list = self.images_list[0:4]

                for i in range(len(self.images_list)):
                    self.labels_list[i].config(image=self.images_list[i])
                    print(self.labels_list[i])





                
                
                #src_01.convert(filepath)
                #self.message.config(text=f'You converted {len(filepath)} images to PDF successfully!')

            except Exception as e:
                self.message.config(text='Something went wrong! Call your son...')
                print(e)
                return False
