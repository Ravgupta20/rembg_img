from rembg import remove
from PIL import Image

input_path = 'input.png'  # Replace with your image file
output_path = 'output.png' # Where the transparent image will be saved

# Open the input image
input_image = Image.open(input_path)

# Remove the background
output_image = remove(input_image)

# Save the output image with transparent background
output_image.save(output_path)

print(f"Background removed and saved to {output_path}")