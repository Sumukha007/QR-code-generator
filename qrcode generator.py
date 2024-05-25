#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import qrcode
from PIL import Image

def generate_qr_with_logo(url, logo_path):
    try:
        # Open the logo image
        logo = Image.open(logo_path)

        # Define the desired width for the logo
        basewidth = 280

        # Calculate the ratio to maintain aspect ratio
        wpercent = (basewidth / float(logo.size[0]))

        # Calculate the new height based on the width percentage
        hsize = int((float(logo.size[1]) * float(wpercent)))

        # Resize the logo image with the calculated size
        logo = logo.resize((basewidth, hsize), Image.LANCZOS)

        # Create a blank image with the same size as the logo image
        logo_bg = Image.new("RGBA", logo.size, (255, 255, 255, 255))  # White background

        # Calculate the position to paste the logo in the center
        pos = ((logo_bg.size[0] - logo.size[0]) // 2, (logo_bg.size[1] - logo.size[1]) // 2)

        # Paste the logo onto the blank image with the white background
        logo_bg.paste(logo, pos)

        # Create a QRCode instance with high error correction
        qr_big = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)

        # Add data to the QRCode instance
        qr_big.add_data(url)

        # Generate the QR code
        qr_big.make()

        # Create a black and white version of the QR code with specified fill and background color
        img_qr_big = qr_big.make_image(fill_color="black", back_color="white").convert('RGBA')

        # Calculate the position to paste the logo in the center of the QR code
        pos = ((img_qr_big.size[0] - logo_bg.size[0]) // 2, (img_qr_big.size[1] - logo_bg.size[1]) // 2)

        # Blend the logo with the QR code using an alpha value of 0.5
        img_qr_big.paste(logo_bg, pos, logo_bg)

        # Display the blended QR code
        img_qr_big.show()
    except Exception as e:
        print("Error:", e)

# Prompt the user to enter the URL and logo path
url = input("Please enter the URL: ")
logo_path = input("Please enter the path to the logo image file: ")

generate_qr_with_logo(url, logo_path)


# In[ ]:




