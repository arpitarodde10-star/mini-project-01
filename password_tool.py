from zxcvbn import zxcvbn
import itertools
def check_password_strength(password):
    result = zxcvbn(password)
    score = result['score']

    strength = {
        0: "Very Weak",
        1: "Weak",
        2: "Fair",
        3: "Strong",
        4: "Very Strong"
    }

    print("\n🔐 Password Strength Analysis")
    print("Score:", score, "/ 4")
    print("Strength:", strength[score])
def generate_wordlist(name, dob, pet):
    base_words = [name, dob, pet]
    wordlist = set()

    for word in base_words:
        wordlist.add(word)
        wordlist.add(word + "123")
        wordlist.add(word + "@")
        wordlist.add(word.capitalize())
        wordlist.add(word[::-1])

    for combo in itertools.permutations(base_words, 2):
        wordlist.add("".join(combo))
        wordlist.add(combo[0] + "@" + combo[1])

    return wordlist
print("=== Password Strength Analyzer & Wordlist Generator ===")

password = input("Enter password to analyze: ")
check_password_strength(password)

name = input("\nEnter your name: ")
dob = input("Enter your birth year (YYYY): ")
pet = input("Enter pet name: ")

words = generate_wordlist(name, dob, pet)

with open("custom_wordlist.txt", "w") as f:
    for word in words:
        f.write(word + "\n")

print("\n✅ Wordlist saved as custom_wordlist.txt")
print("Total words generated:", len(words))
