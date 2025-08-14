import cv2
import matplotlib.pyplot as plt
import os

# Step 1: Load the Image
image_path = 'color_conversion/example.jpg'  # Adjust path if needed

# Check if image file exists
if not os.path.exists(image_path):
    print(f"Error: File not found at {image_path}")
    exit()

image = cv2.imread(image_path)

# Validate image loading
if image is None:
    print(f"Error: Could not read the image file at {image_path}")
    exit()

# Convert BGR to RGB for matplotlib display
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Get image dimensions
height, width, _ = image_rgb.shape

# Step 2: Draw Two Rectangles Around Interesting Regions

# Rectangle 1: Top-left
rect1_width, rect1_height = 150, 150
top_left1 = (20, 20)
bottom_right1 = (top_left1[0] + rect1_width, top_left1[1] + rect1_height)
cv2.rectangle(image_rgb, top_left1, bottom_right1, (0, 255, 255), 3)  # Yellow

# Rectangle 2: Bottom-right
rect2_width, rect2_height = 200, 150
top_left2 = (width - rect2_width - 20, height - rect2_height - 20)
bottom_right2 = (top_left2[0] + rect2_width, top_left2[1] + rect2_height)
cv2.rectangle(image_rgb, top_left2, bottom_right2, (255, 0, 255), 3)  # Magenta

# Step 3: Draw Circles at Centers
center1 = (top_left1[0] + rect1_width // 2, top_left1[1] + rect1_height // 2)
center2 = (top_left2[0] + rect2_width // 2, top_left2[1] + rect2_height // 2)
cv2.circle(image_rgb, center1, 15, (0, 255, 0), -1)  # Green
cv2.circle(image_rgb, center2, 15, (0, 0, 255), -1)  # Red

# Step 4: Draw Line Between Centers
cv2.line(image_rgb, center1, center2, (0, 255, 0), 3)

# Step 5: Text Labels
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image_rgb, 'Region 1', (top_left1[0], top_left1[1] - 10), font, 0.7, (0, 255, 255), 2, cv2.LINE_AA)
cv2.putText(image_rgb, 'Region 2', (top_left2[0], top_left2[1] - 10), font, 0.7, (255, 0, 255), 2, cv2.LINE_AA)
cv2.putText(image_rgb, 'Center 1', (center1[0] - 40, center1[1] + 40), font, 0.6, (0, 255, 0), 2, cv2.LINE_AA)
cv2.putText(image_rgb, 'Center 2', (center2[0] - 40, center2[1] + 40), font, 0.6, (0, 0, 255), 2, cv2.LINE_AA)

# Step 6: Draw Bi-Directional Arrow for Height
arrow_start = (width - 50, 20)
arrow_end = (width - 50, height - 20)
cv2.arrowedLine(image_rgb, arrow_start, arrow_end, (255, 255, 0), 3, tipLength=0.05)  # Down
cv2.arrowedLine(image_rgb, arrow_end, arrow_start, (255, 255, 0), 3, tipLength=0.05)  # Up

# Annotate the height value
height_label_position = (arrow_start[0] - 150, (arrow_start[1] + arrow_end[1]) // 2)
cv2.putText(image_rgb, f'Height: {height}px', height_label_position, font, 0.8, (255, 255, 0), 2, cv2.LINE_AA)

# Step 7: Display the Annotated Image
plt.figure(figsize=(12, 8))
plt.imshow(image_rgb)
plt.title('Annotated Image with Regions, Centers, and Height Arrow')
plt.axis('off')
plt.show()
