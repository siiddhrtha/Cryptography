import cv2
import numpy as np

image = cv2.imread("1.jpeg", 0)
r, c = image.shape
key = np.random.randint(0, 256, size=(r, c), dtype=np.uint8)  # Generate random key image

cv2.imshow("Image", image)  # show the original image
cv2.imshow("key", key)  # Display the key image

print(r)
print(c)
print(image)

encryption = cv2.bitwise_xor(image, key)  # encryption
decryption = cv2.bitwise_xor(encryption, key)  # decryption

cv2.imshow("encryption", encryption)  # Display ciphertext image
cv2.imshow("decryption", decryption)  # Display the decrypted image

cv2.waitKey(-1)
cv2.destroyAllWindows()