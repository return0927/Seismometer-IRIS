import threading
from time import time, sleep
from tools import _IRIS
from tkinter import *
from io import BytesIO
from PIL import Image, ImageTk


IRIS = _IRIS()
IRIS.updateSeismometer("KG", "TJN")


class App(threading.Thread):
    def __init__(self, tk_root):
        self.root = tk_root
        self.label = Label(self.root, text="Placeholder")
        self.label.pack()

        self.seismometer = IRIS.getImage

        self.lastseek = 0

        threading.Thread.__init__(self)
        self.start()

    def run(self):
        loop_active = True
        while loop_active:
            now = time()

            if now - self.lastseek < 5:
                sleep(0.1)
            else:
                self.lastseek = now
                err, content = self.seismometer(True)

                if err:
                    print("ERR", str(content))
                    pass

                else:
                    img = ImageTk.PhotoImage(Image.open(BytesIO(content)))
                    self.label.config(image=img)
                    self.label.image = img
                    self.root.update()

ROOT = Tk()
APP = App(ROOT)
ROOT.mainloop()