import os
from PIL import Image

def convert_images_to_webp(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(input_dir):
        input_path = os.path.join(input_dir, filename)
        if os.path.isfile(input_path):
            try:
                with Image.open(input_path) as img:
                    output_filename = os.path.splitext(filename)[0] + ".webp"
                    output_path = os.path.join(output_dir, output_filename)
                    img.save(output_path, "WEBP")
                    print(f"Converted: {filename} -> {output_filename}")
            except Exception as e:
                print(f"Error converting {filename}: {e}")

if __name__ == "__main__":
    input_directory = "images_to_convert"  # the input directory
    output_directory = "../public"  # the output directory
    convert_images_to_webp(input_directory, output_directory)
