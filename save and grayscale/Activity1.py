import cv2
import os

# Get the current working directory
current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, 'example.jpg')

# Check if file exists
if not os.path.exists(image_path):
    print(f"Error: Image file not found at: {image_path}")
    print(f"Current directory contents: {os.listdir(current_dir)}")
else:
    # Load the image
    image = cv2.imread(image_path)
    
    if image is None:
        print("Error: Could not read the image file (may be corrupted or wrong format)")
    else:
        # Create and configure window
        cv2.namedWindow('Loaded Image', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Loaded Image', 800, 500)
        
        # Display the image
        cv2.imshow('Loaded Image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()