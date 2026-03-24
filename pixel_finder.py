"""
Docstring for Pixel tracking
- Help find exact pixels on a screen for automation
"""
from pynput import mouse, keyboard

mouse_pos = []

def on_click(x, y, button, pressed): 
    if button == mouse.Button.right and pressed:
        print(f"Right-click detected at ({x}, {y})")
        mouse_pos.append((x, y))

# This function only stops the mouse listener
def on_activate():
    print("\nHotkey pressed! Stopping mouse tracking...")
    mouse_listener.stop()

# Define hotkey (Ctrl + Alt + X)
hotkey = keyboard.GlobalHotKeys({
    '<ctrl>+<alt>+x': on_activate
})

print("1. Right-click to save coordinates.")
print("2. Press Ctrl+Alt+X to stop tracking and show results.\n")

# Start listeners
with hotkey as keyboard_listener:
    with mouse.Listener(on_click=on_click) as mouse_listener:
        mouse_listener.join()
    keyboard_listener.stop()

# Display the results
print("\nCaptured Coordinates:")
if mouse_pos:
    for i, pos in enumerate(mouse_pos):
        print(f"{i+1}: {pos}")
else:
    print("No coordinates captured.")

# The final "Enter" block
print("\n" + "-"*20)
input("Press [ENTER] to close the program.")