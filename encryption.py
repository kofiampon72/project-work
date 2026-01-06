from tkinter import *
from tkinter import filedialog
import hashlib
from tkinter import messagebox

# for the GUI
root = Tk()
root.geometry("500x300")

def encrypt_image():
    file1 = filedialog.askopenfilename(filetypes=[('Image files', '*.jpg;*.png')])
    if file1:
        key = entry1.get(1.0, END).strip()
        if not key:
            messagebox.showerror("Error", "Please enter a valid key.")
            return

        try:
            # Read image file as bytes
            with open(file1, 'rb') as fi:
                image = fi.read()

            # Perform image encryption (example: simple XOR-based encryption)
            key_bytes = hashlib.sha256(key.encode()).digest()
            encrypted_image = bytearray(image)
            for index, value in enumerate(encrypted_image):
                encrypted_image[index] = value ^ key_bytes[index % len(key_bytes)]

            # Save the encrypted image
            with open(file1, 'wb') as fi:
                fi.write(encrypted_image)

            messagebox.showinfo("Success", "Image encrypted successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error while encrypting: {e}")

# The Button
b1 = Button(root, text="Encrypt Image", command=encrypt_image)
b1.place(x=220, y=150)

# Text box
entry1 = Text(root, height=1, width=20)
entry1.place(x=170, y=100)

root.mainloop()
