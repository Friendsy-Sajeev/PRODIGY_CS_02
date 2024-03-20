from PIL import Image

def encrypt_image(image_path):
    # Open the image
    img = Image.open(image_path)

    # Get the width and height of the image
    width, height = img.size

    # Iterate through each pixel and swap red and blue values
    for i in range(width):
        for j in range(height):
            # Get pixel values
            r, g, b = img.getpixel((i, j))

            # Swap red and blue values
            img.putpixel((i, j), (b, g, r))

    # Save the encrypted image
    img.save("encrypted_image.png")

def decrypt_image(encrypted_image_path):
    # Open the encrypted image
    img = Image.open(encrypted_image_path)

    # Get the width and height of the image
    width, height = img.size
# Iterate through each pixel and swap red and blue values (reverse operation)
    for i in range(width):
        for j in range(height):
            # Get pixel values
            r, g, b = img.getpixel((i, j))

            # Swap red and blue values
            img.putpixel((i, j), (b, g, r))

    # Save the decrypted image
    img.save("decrypted_image.png")

def main():
    choice = input("Do you want to encrypt or decrypt an image? (e/d): ").lower()

    if choice == 'e':
        image_path = input("Enter the path to the image to encrypt: ")
        encrypt_image(image_path)
        print("Image encrypted successfully.")

    elif choice == 'd':
        encrypted_image_path = input("Enter the path to the encrypted image to decrypt: ")
        decrypt_image(encrypted_image_path)
        print("Image decrypted successfully.")

    else:
        print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")

if __name__ == "__main__":
    main()

