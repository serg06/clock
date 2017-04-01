from tkinter import *
from PIL import Image, ImageTk
from datetime import datetime
import configparser


class Clock:
    def __init__(self, width=960, height=540):
        self.width = width
        self.height = height

        # tkinter settings
        self.root = Tk()
        self.root.title('Clock')
        self.root.resizable(0, 0)

        # Background image
        self.background = ImageTk.PhotoImage(
            Image.open('assets/background.png').resize((width, height), Image.ANTIALIAS)
        )

        # Blank number image
        self.blank = ImageTk.PhotoImage(
            Image.open('assets/blank.png').resize((int(width*(0.057)), int(height*(0.245))), Image.ANTIALIAS)
        )

        # Various number images
        self.numbers = []
        for i in range(10):
            self.numbers.append(ImageTk.PhotoImage(
                Image.open('assets/%i.png' % i).resize((int(width*(0.057)), int(height*(0.245))), Image.ANTIALIAS)
            ))

        self.canvas = Canvas(self.root)

        # Create background image
        self.canvas.create_image(width/2, height/2, image=self.background)

        # Store clock number position IDs for later
        self.num_pos = []

        # Create blank clock images
        self.num_pos.append(self.canvas.create_image(width * (0.295 + 0.0371 * 0 + 0.0743 * 0), height * (0.129), image=self.blank))
        self.num_pos.append(self.canvas.create_image(width * (0.295 + 0.0371 * 1 + 0.0743 * 0), height * (0.129), image=self.blank))
        self.num_pos.append(self.canvas.create_image(width * (0.295 + 0.0371 * 2 + 0.0743 * 0), height * (0.129), image=self.blank))

        self.num_pos.append(self.canvas.create_image(width * (0.295 + 0.0371 * 2 + 0.0743 * 1), height * (0.129), image=self.blank))
        self.num_pos.append(self.canvas.create_image(width * (0.295 + 0.0371 * 3 + 0.0743 * 1), height * (0.129), image=self.blank))

        self.num_pos.append(self.canvas.create_image(width * (0.295 + 0.0371 * 3 + 0.0743 * 2), height * (0.129), image=self.blank))
        self.num_pos.append(self.canvas.create_image(width * (0.295 + 0.0371 * 4 + 0.0743 * 2), height * (0.129), image=self.blank))

        self.num_pos.append(self.canvas.create_image(width * (0.295 + 0.0371 * 4 + 0.0743 * 3), height * (0.129), image=self.blank))
        self.num_pos.append(self.canvas.create_image(width * (0.295 + 0.0371 * 5 + 0.0743 * 3), height * (0.129), image=self.blank))

        # Copy-pasted code
        self.canvas.config(bg="black", width=width, height=height)
        self.canvas.pack(side=LEFT, expand=True, fill=BOTH)

        # Call update_image as soon as the window opens
        self.root.after(1, self.update_image)
        self.root.mainloop()

    def update_image(self):
        # Update hours
        self.canvas.itemconfig(self.num_pos[3], image=self.numbers[int(datetime.now().hour / 10)])
        self.canvas.itemconfig(self.num_pos[4], image=self.numbers[datetime.now().hour % 10])

        # Update minutes
        self.canvas.itemconfig(self.num_pos[5], image=self.numbers[int(datetime.now().minute / 10)])
        self.canvas.itemconfig(self.num_pos[6], image=self.numbers[datetime.now().minute % 10])

        # Update seconds
        self.canvas.itemconfig(self.num_pos[7], image=self.numbers[int(datetime.now().second / 10)])
        self.canvas.itemconfig(self.num_pos[8], image=self.numbers[datetime.now().second % 10])

        # Update again in a second
        self.root.after(1000, self.update_image)


def main():
    # Load dimensions and start clock
    config = configparser.ConfigParser()
    config.read('config.ini')
    Clock(int(config['Dimensions']['width']), int(config['Dimensions']['height']))

if __name__ == '__main__':
    main()
