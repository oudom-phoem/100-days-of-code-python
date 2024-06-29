import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
should_continue = True

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = (alphabet.index(char) + shift_amount) % len(alphabet)
            end_text += alphabet[position]
        else:
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}")

print(art.logo)

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    if input("Type 'yes' if you want to go again. Otherwise type 'no'. ").lower() == "no":
        should_continue = False
        print("Goodbye")

   