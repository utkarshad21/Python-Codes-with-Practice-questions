# Q1. Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up! 


words = {
    "Billi": "Cat",
    "Kursi": "Chair",
    "Madad": "Help",
    "Thaili": "Bag",
    "Moje": "Socks",
    "Kitaab": "Book",
    "Pankha": "Fan",
    "Dost": "Friend",
    "Khaana": "Food",
    "Ghar": "Home",
    "Pani": "Water",
    "Gaadi": "Car",
    "Ped": "Tree",
    "Kutta": "Dog",
    "Aankh": "Eye"
}


word = input("Enter a Hindi word to know its English translation: ").capitalize()


if word in words:
    print(f"The English word for '{word}' is '{words[word]}'.")
else:
    print(f"Sorry, the word '{word}' is not in the dictionary.")
