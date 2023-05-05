import tkinter as tk

class OutputInterface():

    def __init__(self, window_resolution: str):
        self.window_resolution = window_resolution
        self.root = tk.Tk()
        self.label = None
        self.image = None
        self.build_interface()

    def build_interface(self):
        self.root.geometry(self.window_resolution)
        self.create_label()
        self.create_image()

    def create_label(self):
        self.label = tk.Label(self.root, text="")
        self.label.pack()

    def create_image(self):
        self.image = tk.Label(self.root)
        self.image.pack()

    def update_frame(self, new_photo):
        self.image.config(image=new_photo)
        self.image.image =new_photo

    def update_label(self, new_label):
        self.label.config(text=new_label)

    def run(self):
        self.root.mainloop()


