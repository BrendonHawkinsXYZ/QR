import qrcode
from PIL import Image
import os

def generate_qr(data, base_filename, dpi=300, fill_color=(0, 0, 0), back_color=(255, 255, 255)):
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=1000,  # size of each box in pixels
        border=10,  # thickness of the border (default is 4)
    )

    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance with custom colors
    img = qr.make_image(fill_color=fill_color, back_color=back_color).convert('RGB')

    # Determine the filename with incremental numbering
    filename = f"{base_filename}.png"
    counter = 1
    while os.path.exists(filename):
        filename = f"{base_filename}_{counter}.png"
        counter += 1

    # Save the image with the determined filename and DPI
    img.save(filename, format="PNG", dpi=(dpi, dpi))

    print(f"QR code generated and saved as {filename} with 300 DPI and custom colors")

# Example usage
data_to_encode = "ANY LINK"  # Replace with your data
base_filename = "custom_qr"  # Base filename without extension

# Define custom colors
fill_color = (0, 0, 0)  # RGB for red
back_color = (255, 255, 255)  # RGB for white

# Generate and save the QR code with 300 DPI, custom colors, and incremental filename
generate_qr(data_to_encode, base_filename, dpi=300, fill_color=fill_color, back_color=back_color)
