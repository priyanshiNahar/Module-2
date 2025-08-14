import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def display_image(title, image):
    """Utility function to display an image."""
    plt.figure(figsize=(8, 8))
    if len(image.shape) == 2:  # Grayscale image
        plt.imshow(image, cmap='gray')
    else:  # Color image
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

def apply_edge_detection(image, method="sobel", ksize=3, threshold1=100, threshold2=200):
    """Applies the selected edge detection method."""
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    if method == "sobel":
        sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=ksize)
        sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=ksize)
        # Convert to uint8 and bitwise OR to combine edges
        sobelx_uint8 = cv2.convertScaleAbs(sobelx)
        sobely_uint8 = cv2.convertScaleAbs(sobely)
        return cv2.bitwise_or(sobelx_uint8, sobely_uint8)

    elif method == "canny":
        return cv2.Canny(gray_image, threshold1, threshold2)

    elif method == "laplacian":
        laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)
        return cv2.convertScaleAbs(laplacian)

def apply_filter(image, filter_type="gaussian", ksize=5):
    """Applies the selected filter to the image."""
    if filter_type == "gaussian":
        return cv2.GaussianBlur(image, (ksize, ksize), 0)
    elif filter_type == "median":
        return cv2.medianBlur(image, ksize)

def interactive_edge_detection(image_path):
    """Interactive activity for edge detection and filtering."""
    print(f"Trying to load image from: {image_path}")
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Image not found!")
        return

    print("Select an option:")
    print("1. Sobel Edge Detection")
    print("2. Canny Edge Detection")
    print("3. Laplacian Edge Detection")
    print("4. Gaussian Smoothing")
    print("5. Median Filtering")
    print("6. Exit")

    while True:
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            ksize = int(input("Enter kernel size for Sobel (odd number): "))
            result = apply_edge_detection(image, method="sobel", ksize=ksize)
            display_image("Sobel Edge Detection", result)

        elif choice == "2":
            threshold1 = int(input("Enter lower threshold for Canny: "))
            threshold2 = int(input("Enter upper threshold for Canny: "))
            result = apply_edge_detection(image, method="canny", threshold1=threshold1, threshold2=threshold2)
            display_image("Canny Edge Detection", result)

        elif choice == "3":
            result = apply_edge_detection(image, method="laplacian")
            display_image("Laplacian Edge Detection", result)

        elif choice == "4":
            ksize = int(input("Enter kernel size for Gaussian smoothing (odd number): "))
            result = apply_filter(image, filter_type="gaussian", ksize=ksize)
            display_image("Gaussian Smoothed Image", result)

        elif choice == "5":
            ksize = int(input("Enter kernel size for Median filtering (odd number): "))
            result = apply_filter(image, filter_type="median", ksize=ksize)
            display_image("Median Filtered Image", result)

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 6.")

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, 'example.jpg')  # Image file should be in the same folder as this script

interactive_edge_detection(image_path)
