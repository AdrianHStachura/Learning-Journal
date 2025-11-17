import numpy as np
import cv2

# Initialize variables
height = 800
width = 800
channels = 3  # RGB

# Initialize screen (canvas)
canvas = np.zeros((height, width, channels), dtype=np.uint8)

def draw_pixel(x, y):
    # Draw a small rectangle (pixel) at (x, y)
    # You must provide two points: top-left and bottom-right corners
    # Let's make a 5x5 rectangle centered at (x, y)
    top_left = (x, y)
    bottom_right = (x + 5, y + 5)
    cv2.rectangle(canvas, top_left, bottom_right, (255, 0, 0), -1)  # -1 fills the rectangle

cv2.namedWindow("maze_gen", cv2.WINDOW_NORMAL)
cv2.resizeWindow("maze_gen", width, height)

while True:
    # Clear canvas if needed (uncomment the next line to clear each frame)
    # canvas[:] = 0

    draw_pixel(100, 100)

    cv2.imshow("maze_gen", canvas)  # First argument is window name (string)
    key = cv2.waitKey(10)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
