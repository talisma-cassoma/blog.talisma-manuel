import qrcode
import os

def generate_qr_code(link: str, output_dir: str = "qr_code_output_image", filename: str = "qrcode.png"):
    """
    Generates a QR code from a given link and saves it as a PNG file in the output directory.
    
    :param link: The website link to encode in the QR code.
    :param output_dir: The directory where the QR code image will be saved.
    :param filename: The name of the output PNG file.
    """
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)
    
    # Create and save the image
    img = qr.make_image(fill='black', back_color='white')
    output_path = os.path.join(output_dir, filename)
    img.save(output_path)
    
    print(f"QR code saved at: {output_path}")

# Example usage
generate_qr_code("http://blog-talisma-cassoma.netlify.app/")
