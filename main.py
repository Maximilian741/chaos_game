import tkinter as tk
from tkinter import ttk
import random

# Define the vertices of the shapes
shapes = {
    "Triangle": [(150, 50), (75, 200), (225, 200)],
    "Square": [(75, 75), (225, 75), (225, 225), (75, 225)],
    "Pentagon": [(150, 50), (50, 150), (100, 250), (200, 250), (250, 150)],
    "Barnsley's Fern": []
}

# Set the initial shape to Triangle
current_shape = "Triangle"

# Set the initial point to a random position within the shape
current_point = [random.randint(75, 225), random.randint(50, 200)]

# Initialize the previous vertex
previous_vertex = None

# Define the update function that will be called repeatedly
def update():
    global current_point
    global previous_vertex
    if current_shape == "Barnsley's Fern":
        update_barnsley()
    else:
        # Choose a random vertex
        vertex = random.choice(shapes[current_shape])
        # Apply restriction for square shape
        if current_shape == "Square":
            while vertex == previous_vertex:
                vertex = random.choice(shapes[current_shape])
        # Calculate the midpoint between the current point and the vertex
        current_point = [(current_point[0] + vertex[0]) / 2, (current_point[1] + vertex[1]) / 2]
        # Draw a dot at the new point
        canvas.create_oval(current_point[0], current_point[1], current_point[0] + 1, current_point[1] + 1, fill='black')
        # Update the previous vertex
        previous_vertex = vertex
    # Schedule the next update
    root.after(10, update)

# Define the update function for Barnsley's Fern
def update_barnsley():
    global current_point
    x, y = current_point
    r = random.random()
    if r < 0.01:
        x_new = 0
        y_new = 0.16 * y
    elif r < 0.86:
        x_new = 0.85 * x + 0.04 * y
        y_new = -0.04 * x + 0.85 * y + 1.6
    elif r < 0.93:
        x_new = 0.2 * x - 0.26 * y
        y_new = 0.23 * x + 0.22 * y + 1.6
    else:
        x_new = -0.15 * x + 0.28 * y
        y_new = 0.26 * x + 0.24 * y + 0.44
    current_point = [x_new, y_new]
    # Scale and translate the point to fit on the canvas
    x_canvas = int(50 * x_new + 150)
    y_canvas = int(-50 * y_new + 400)
    # Draw a dot at the new point
    canvas.create_oval(x_canvas, y_canvas, x_canvas + 1, y_canvas + 1, fill='black')

# Define the function to change the shape
def change_shape(event):
    global current_shape
    global current_point
    global previous_vertex
    # Get the selected shape from the combobox
    current_shape = shape_combobox.get()
    # Clear the canvas
    canvas.delete("all")
    # Reset the initial point for Barnsley's Fern and reset previous vertex for Square shape 
    if current_shape == "Barnsley's Fern":
        current_point = [0, 0]
    elif current_shape == "Square":
        previous_vertex = None

# Set up the GUI
root = tk.Tk()
root.geometry("400x400")
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# Create a combobox to select the shape
shape_combobox = ttk.Combobox(root, values=list(shapes.keys()))
shape_combobox.current(0)
shape_combobox.bind("<<ComboboxSelected>>", change_shape)
shape_combobox.pack()

# Call the update function to start the chaos game
update()
root.mainloop()