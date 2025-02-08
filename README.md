# AquaMark

AquaMark is a simple Python-based watermarking tool that allows users to embed a watermark image onto another image at various customizable positions and sizes.

## Features
- Supports watermark placement at multiple positions.
- Allows users to resize the watermark based on the image width.
- Ensures non-destructive editing by saving watermarked images separately.
- Uses the **Pillow** library for image processing.

## Installation
1. Clone this repository or download the script:
   ```bash
   git clone https://github.com/your-repo/AquaMark.git
   cd AquaMark
Install the required dependencies:
pip install pillow
Ensure your watermark image is placed in the watermark/ directory.
Usage
Run the script and provide the required inputs:
python app.py
The script will prompt you for:

The path to the image you want to watermark.
The position of the watermark (1-9, default: 9).
The size percentage of the watermark (default: 20%).
Watermark Positioning
AquaMark supports different positioning options:

1: Top-left        2: Top-center      3: Top-right
4: Middle-left     5: Center          6: Middle-right
7: Bottom-left     8: Bottom-center   9: Bottom-right (default)
Customization
Change the Default Watermark Image:
Update the watermark_path variable in app.py.

Modify the Default Position & Size:
Change the default values in app.py:
position_id = 9  # Default position (bottom-right)
watermark_size_percentage = 20  # Default size as % of image width
Output
Watermarked images are saved in the watermarked_images/ directory.

License
This project is open-source. Feel free to modify and use it.

![women](https://github.com/user-attachments/assets/4fd4bd87-c394-446b-9ea7-cd45655aeaa7)
![image ](https://github.com/user-attachments/assets/5e05ce0f-813d-424d-b498-b44cd417395c)

