colors = []

def main():
    ## Display colors beginning with a specified letter.
    letter = requestLetter()
    fillListWithColors(letter)
    displayColors()

def requestLetter():
    letter = input("Enter a letter: ")
    return letter.upper()

def fillListWithColors(letter):
    global colors
    for color in open("Colors.txt", 'r'):
        if color.startswith(letter):
            colors.append(color.rstrip())

def displayColors():
    for color in colors:
        print(color)

main()