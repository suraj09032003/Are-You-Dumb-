import tkinter as tk
from tkinter import Label
from random import randint
import time
import cv2
from tkinter import PhotoImage
from PIL import Image, ImageTk




# Function to capture and save an image
def capture_and_save_image(filename='saved_image.jpg'):
    # Capture video from the webcam
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        print("Error: Could not open video capture.")
        cap.release()
        return
    
    # Wait for a short period to ensure the camera is warm up
    time.sleep(1)

    # Capture a single frame
    ret, frame = cap.read()

    # Check if the frame was captured successfully
    if ret:
        # Save the frame as an image file
        cv2.imwrite(filename, frame)
        print(f'Image saved as {filename}')
    else:
        print("Error: Can't capture frame.")

    # Release the capture
    cap.release()



# Example usage
capture_and_save_image('auto_captured_image.jpg')

def move_button(button):

    smooth_move(button, randint(0, 200), randint(0, 200))

def smooth_move(widget, new_x, new_y):
    current_x, current_y = widget.winfo_x(), widget.winfo_y()

    steps = 10
    x_step = (new_x - current_x) / steps
    y_step = (new_y - current_y) / steps

    for _ in range(steps):
        current_x += x_step
        current_y += y_step
        widget.place(x=current_x, y=current_y)
        widget.update()


def size_change(label,lab2):
    for i in range(100):
        label.configure(font=("Arial", i),bg="red",fg="white")
        label.update()
    lab2.pack()
    for i in range(50):
        lab2.configure(font=("Arial", i),bg="red",fg="white")
        lab2.update()  

def show():
    capture_and_save_image("./people.jpg")
    popup = Label(root, text="I know, idiot", font=("Arial", 25))
    popup.pack()
    
    # Load the image with PIL
    image_path = "./people.jpg"  # Changed to "./people.jpg" for consistency
    image = Image.open(image_path).resize((300, 300))
    
    # Convert the PIL image to a format that Tkinter can display
    photo = ImageTk.PhotoImage(image)

    # Create a label to display the image and add it to the window
    image_label = Label(root, image=photo)
    image_label.pack()
    image_label.image = photo
    popup_ = Label(root,text="YOU SO UGLY THAT I FEEL LIKE SHUTTING MY SELF",font=("Arial", 25))
    
    
    # Keep a reference to the photo object to prevent garbage collection
    
    size_change(popup,popup_)

    time.sleep(5)
    exit()


root = tk.Tk()
root.configure(bg="red")
root.geometry("400x300")
root.title("Are you dumb?")

label = Label(root, text="Are you dumb?",font=("Arial", 50),bg="red",fg="yellow")
label.place(x=50,y=0)

yes_button = tk.Button(root, text="YES", command=show)
yes_button.place(x=100,y=100)

no_button = tk.Button(root, text="NO", command=lambda: move_button(no_button))
no_button.place(x=200, y=100)

root.mainloop()
