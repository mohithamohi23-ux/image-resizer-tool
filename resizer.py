import os
from PIL import Image

# Folder paths
input_folder = "images"
output_folder = "output"

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through all files in input folder
for file_name in os.listdir(input_folder):
    try:
        # Open image
        img_path = os.path.join(input_folder, file_name)
        img = Image.open(img_path)

        # Resize image (800x800)
        resized_img = img.resize((800, 800))

        # Save as PNG format in output folder
        new_file_name = os.path.splitext(file_name)[0] + ".png"
        resized_img.save(os.path.join(output_folder, new_file_name), "PNG")

        print(f"✅ {file_name} resized and saved as {new_file_name}")

    except Exception as e:
        print(f"⚠️ Skipped {file_name} (Reason: {e})")
