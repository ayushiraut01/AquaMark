import os
from PIL import Image

def get_position(image_width, image_height, watermark_width, watermark_height, position_id=9, margin=10):
    """
    Get the position of the watermark based on position_id.
    """
    positions = {
        1: (margin, margin),
        2: (image_width // 2 - watermark_width // 2, margin),
        3: (image_width - watermark_width - margin, margin),
        4: (margin, image_height // 2 - watermark_height // 2),
        5: (image_width // 2 - watermark_width // 2, image_height // 2 - watermark_height // 2),
        6: (image_width - watermark_width - margin, image_height // 2 - watermark_height // 2),
        7: (margin, image_height - watermark_height - margin),
        8: (image_width // 2 - watermark_width // 2, image_height - watermark_height - margin),
        9: (image_width - watermark_width - margin, image_height - watermark_height - margin),
    }
    return positions.get(position_id, positions[9])

def add_watermark(input_image_path, watermark_path='watermark/aisha.jpg', position_id=9, watermark_size_percentage=20):
    """
    Add a watermark to the input image.
    """
    if not os.path.exists(watermark_path):
        print(f"Error: The watermark file '{watermark_path}' does not exist.")
        return
    
    with Image.open(input_image_path).convert("RGBA") as base:
        with Image.open(watermark_path).convert("RGBA") as watermark:
            # Increase watermark size as a percentage of base image
            new_width = int(base.width * (watermark_size_percentage / 100))
            new_height = int(watermark.height * (new_width / watermark.width))
            watermark = watermark.resize((new_width, new_height), Image.LANCZOS)

            
            # Get the position for the watermark
            pos = get_position(base.width, base.height, new_width, new_height, position_id)
            
            # Paste the watermark using an alpha mask for transparency
            base.paste(watermark, pos, watermark)
            
            # Ensure the output directory exists
            output_directory = 'watermarked_images'
            os.makedirs(output_directory, exist_ok=True)
            
            # Save the result
            output_filename = os.path.join(output_directory, os.path.basename(input_image_path))
            base.save(output_filename, 'PNG')
            print(f"Watermark added and saved to {output_filename}.")

if __name__ == '__main__':
    input_image_path = input("Enter the path to the image: ").strip()
    position_id = int(input("Enter watermark position [1-30, default 30]: ") or '30')
    watermark_size_percentage = int(input("Enter watermark size percentage of the image width [default 20]: ") or '20')
    add_watermark(input_image_path, watermark_size_percentage=watermark_size_percentage, position_id=position_id)
