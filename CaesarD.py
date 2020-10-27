
def decrypt(string):
 
  cipher = ''
  for char in string: 
    if char == ' ':
      cipher = cipher + char
    elif  char.isupper():
      cipher = cipher + chr((ord(char) -3 - 65) % 26 + 65)
  
  return cipher
 
msg = input("Enter message: ").upper()
print("original string: ", msg)
print("-----Decryption-----")
print("",decrypt(msg))