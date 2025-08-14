import cv2
import os

def process_image():
    # Load the image with error checking
    image_path = 'example.jpg'
    if not os.path.exists(image_path):
        print(f"Error: Image file '{image_path}' not found in directory: {os.getcwd()}")
        print(f"Available files: {os.listdir()}")
        return
    
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not read image '{image_path}'. File may be corrupted.")
        return

    try:
        # Convert to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Resize with aspect ratio preservation (optional improvement)
        h, w = gray_image.shape[:2]
        if h != 224 or w != 224:
            print(f"Original size: {w}x{h} - Resizing to 224x224")
            resized_image = cv2.resize(gray_image, (224, 224), interpolation=cv2.INTER_AREA)
        else:
            resized_image = gray_image
        
        # Display the processed image
        cv2.imshow('Processed Image (Press S to save)', resized_image)
        
        # Wait for key press with timeout (30 seconds)
        key = cv2.waitKey(30000) & 0xFF  # Wait for 30 seconds or key press
        
        # Handle key press
        if key == ord('s') or key == ord('S'):
            output_path = 'grayscale_resized_image.jpg'
            cv2.imwrite(output_path, resized_image)
            print(f"Image successfully saved as '{output_path}'")
            print(f"Saved image dimensions: {resized_image.shape}")
        elif key == 27:  # ESC key
            print("Operation cancelled")
        elif key == -1:  # Timeout
            print("Window closed after timeout")
        else:
            print("Image processed but not saved")
            
    except Exception as e:
        print(f"Error during processing: {str(e)}")
    finally:
        cv2.destroyAllWindows()

if __name__ == "__main__":
    process_image()