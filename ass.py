import cv2
import numpy as np
import matplotlib.pyplot as plt

# === LOAD YOUR ID IMAGE ===
# Replace with the path to your actual ID image
img = cv2.imread(r'C:\Users\Abood\Desktop\New folder (5)\1.py\22.jpg', cv2.IMREAD_UNCHANGED)

# Convert to BGRA if needed
if img.shape[2] == 3:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)

# === WRITE YOUR NAME ===
name = "abdalla abdelnasser"
cv2.putText(img, name, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 255, 255), 2)

# === DRAW LINE UNDER NAME ===
text_size = cv2.getTextSize(name, cv2.FONT_HERSHEY_SIMPLEX, 1.2, 2)[0]
start_point = (50, 110)
end_point = (50 + text_size[0], 110)
cv2.line(img, start_point, end_point, (255, 255, 255, 255), 2)

# === DRAW CIRCLES ON IMAGE CORNERS ===
h, w = img.shape[:2]
corners = [(0, 0), (w-1, 0), (0, h-1), (w-1, h-1)]
for x, y in corners:
    cv2.circle(img, (x, y), 10, (0, 255, 0, 255), -1)

# === CREATE 4 TRANSPARENCY VERSIONS ===
alphas = [1.0, 0.75, 0.5, 0.25]
fig, axs = plt.subplots(2, 2, figsize=(10, 8))
axs = axs.ravel()

for i in range(4):
    img_alpha = img.copy()
    img_alpha[:, :, 3] = int(255 * alphas[i])  # Set alpha channel
    axs[i].imshow(cv2.cvtColor(img_alpha, cv2.COLOR_BGRA2RGBA))
    axs[i].set_title(f'Alpha: {alphas[i]}')
    axs[i].axis('off')

plt.tight_layout()
plt.show()
