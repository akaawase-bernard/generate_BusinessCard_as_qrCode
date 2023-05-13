import qrcode

def generate_qrcode(content, file_path):
    try:
        # Create a QR code instance
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=10, border=4)

        # Add the content to the QR code
        qr.add_data(content)
        qr.make(fit=True)

        # Create an image from the QR code
        image = qr.make_image(fill_color="black", back_color="white")

        # Save the image to the specified file path
        image.save(file_path)

        print("QR code generated successfully.")
    except Exception as e:
        print(f"An error occurred while generating the QR code: {str(e)}")

# Define the content for the complementary card
name = "John Doe"
job_title = "Software Engineer"
email = "johndoe@example.com"
phone = "+1234567890"
website = "www.example.com"

# Define the content to encode in the QR code
content = f"Name: {name}\nJob Title: {job_title}\nEmail: {email}\nPhone: {phone}\nWebsite: {website}"

# Define the file path to save the QR code
file_path = "complementary_card_qrcode.png"

# Generate the QR code
generate_qrcode(content, file_path)
