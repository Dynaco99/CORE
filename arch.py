import cv2
import numpy as np
from scipy.interpolate import splprep, splev

# Load image
img = cv2.imread("bridge_image.jpg")

# Click points on the arch to select control points
control_points = []

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        control_points.append((x, y))
        cv2.circle(img, (x, y), 5, (255, 0, 0), -1)

cv2.namedWindow("image")
cv2.setMouseCallback("image", mouse_callback)

while True:
    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Once control points are selected, fit Bézier curve using spline
points = np.array(control_points)
tck, u = splprep([points[:,0], points[:,1]], s=0)
u_new = np.linspace(u.min(), u.max(), 100)
x_new, y_new = splev(u_new, tck)

# Draw the fitted curve
for i in range(len(x_new)-1):
    cv2.line(img, (int(x_new[i]), int(y_new[i])), (int(x_new[i+1]), int(y_new[i+1])), (0, 255, 0), 2)

cv2.imshow("Fitted Curve", img)
cv2.waitKey(0)
