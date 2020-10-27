import re


def cipher_encryption():
    msg = input("Enter message: ")
    rails = int(input("Enter number of rails: "))

    # removing white space from message
    msg = msg.replace(" ", "")

    # creating an empty matrix
    railMatrix = []
    for i in range(rails):
        railMatrix.append([])
    for row in range(rails):
        for column in range(len(msg)):
            railMatrix[row].append('.')

    # putting letters of message one by one in the matrix in zig-zag
    row = 0
    check = 0
    for i in range(len(msg)):
        if check == 0:
            railMatrix[row][i] = msg[i]
            row += 1
            if row == rails:
                check = 1
                row -= 1
            # inner if
        elif check == 1:
            row -= 1
            railMatrix[row][i] = msg[i]
            if row == 0:
                check = 0
                row = 1
            

    encryp_text = ""
    for i in range(rails):
        for j in range(len(msg)):
            encryp_text += railMatrix[i][j]

    encryp_text = re.sub(r"\.", "", encryp_text)
    print("Encrypted Text: {}".format(encryp_text))



def main():
     print("---Encryption---")
     cipher_encryption()

if __name__ == "__main__":
    main()