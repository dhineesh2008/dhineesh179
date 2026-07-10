from tkinter import *

# Create window
root = Tk()
root.title("Distance Converter")
root.geometry("350x250")

# Variables
value = StringVar()
result = StringVar()
choice = StringVar()
choice.set("Kilometers to Miles")

# Conversion function
def convert():
    try:
        num = float(value.get())

        if choice.get() == "Kilometers to Miles":
            ans = num * 0.621371
            result.set(f"{ans:.2f} miles")
        else:
            ans = num / 0.621371
            result.set(f"{ans:.2f} kilometers")

    except ValueError:
        result.set("Invalid Input")

# UI
Label(root, text="Distance Converter", font=("Arial", 16, "bold")).pack(pady=10)

Entry(root, textvariable=value, font=("Arial", 12)).pack(pady=5)

OptionMenu(root, choice,
           "Kilometers to Miles",
           "Miles to Kilometers").pack(pady=5)

Button(root, text="Convert", command=convert).pack(pady=10)

Label(root, text="Result:", font=("Arial", 12)).pack()

Label(root, textvariable=result, font=("Arial", 14), fg="blue").pack()

root.mainloop()
