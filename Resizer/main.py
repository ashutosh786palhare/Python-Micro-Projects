import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import webbrowser

def open_github():
    webbrowser.open("https://github.com/your-username")

def resize_image():
    selected_file = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if selected_file:
        image = Image.open(selected_file)
        resized_image = image.resize((300, 300), Image.ANTIALIAS)
        resized_image.save("resized_image.png")  # Save the resized image
        display_resized_image(resized_image)

def display_resized_image(image):
    img = ImageTk.PhotoImage(image)
    img_label.configure(image=img)
    img_label.image = img

root = tk.Tk()
root.title("Image Resizer")
root.geometry("470x550")

# Navbar
navbar = tk.Menu(root)
root.config(menu=navbar)

file_menu = tk.Menu(navbar, tearoff=0)
navbar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=resize_image)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

more_menu = tk.Menu(navbar, tearoff=0)
navbar.add_cascade(label="More Tools", menu=more_menu)
more_menu.add_command(label="GitHub", command=open_github)

# Main Frame
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

# Image Display
img_label = tk.Label(main_frame)
img_label.pack(padx=20, pady=20)

root.mainloop()
