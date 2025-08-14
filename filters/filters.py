import cv2
import numpy as np
import os


def display_image(title, image):
    """Utility function to display an image."""
    cv2.imshow(title, image)
    cv2.waitKey(0)  # Wait indefinitely until any key is pressed
    cv2.destroyAllWindows()


def apply_color_filter(image, filter_type, intensity=50):
    """Apply the specified color filter to the image."""
    filtered_image = image.copy()

    if filter_type == "red_tint":
        filtered_image[:, :, 1] = 0  # Green channel to 0
        filtered_image[:, :, 0] = 0  # Blue channel to 0

    elif filter_type == "blue_tint":
        filtered_image[:, :, 1] = 0  # Green channel to 0
        filtered_image[:, :, 2] = 0  # Red channel to 0

    elif filter_type == "green_tint":
        filtered_image[:, :, 0] = 0  # Blue channel to 0
        filtered_image[:, :, 2] = 0  # Red channel to 0

    elif filter_type == "increase_red":
        filtered_image[:, :, 2] = cv2.add(filtered_image[:, :, 2], intensity)

    elif filter_type == "decrease_blue":
        filtered_image[:, :, 0] = cv2.subtract(filtered_image[:, :, 0], intensity)

    elif filter_type == "increase_green":
        filtered_image[:, :, 1] = cv2.add(filtered_image[:, :, 1], intensity)

    elif filter_type == "decrease_red":
        filtered_image[:, :, 2] = cv2.subtract(filtered_image[:, :, 2], intensity)

    return filtered_image


def save_image(image):
    """Allow the user to save the filtered image."""
    filename = input("Enter a name for the image (without extension): ")
    filename = "".join(c for c in filename if c.isalnum() or c in ('_', '-'))  # Sanitize filename
    cv2.imwrite(f"{filename}.png", image)
    print(f"Image saved as {filename}.png")


def interactive_color_filter(image_path):
    """Interactive activity for real-time color filter application."""
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found!")
        return

    print("Select an option:")
    print("r - Red Tint")
    print("b - Blue Tint")
    print("g - Green Tint")
    print("i - Increase Red Intensity")
    print("d - Decrease Blue Intensity")
    print("up_arrow - Increase Green Intensity")
    print("down_arrow - Decrease Red Intensity")
    print("q - Quit")

    while True:
        filter_type = input("Enter your choice: ")

        if filter_type == "r":
            filtered_image = apply_color_filter(image, "red_tint")
        elif filter_type == "b":
            filtered_image = apply_color_filter(image, "blue_tint")
        elif filter_type == "g":
            filtered_image = apply_color_filter(image, "green_tint")
        elif filter_type == "i":
            filtered_image = apply_color_filter(image, "increase_red", intensity=50)
        elif filter_type == "d":
            filtered_image = apply_color_filter(image, "decrease_blue", intensity=50)
        elif filter_type == "up_arrow":
            filtered_image = apply_color_filter(image, "increase_green", intensity=50)
        elif filter_type == "down_arrow":
            filtered_image = apply_color_filter(image, "decrease_red", intensity=50)
        elif filter_type == "q":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")
            continue

        display_image("Filtered Image", filtered_image)

        save_choice = input("Do you want to save this image? (yes/no): ")
        if save_choice.lower() == "yes":
            save_image(filtered_image)


if __name__ == "__main__":
    # Get full path of the current script folder
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Image path in the same folder as the script
    image_path = os.path.join(script_dir, "example.jpg")

    interactive_color_filter(image_path)
