#counter app

#Print welcome message for the user
print("Welcome to the counter app")
#ask for the user name
name = input("What is your name? ").title().strip()
print("Hello " + name + "!")

print('I will count your letters in your message ')
message = input("Enter your message: ")
letter = input('What letter do want to count: ')
message = message.lower()
letter = letter.lower()

letter_count = message.count(letter)

print(name + " your message has " + str(letter_count) + letter + " letters in it")
