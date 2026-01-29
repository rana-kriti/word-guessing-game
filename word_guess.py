import random
words={
    "Door":{
        "I open and close, but I am not alive.",
        "I can be wooden,metal or glass.",
        "You knock on me before entering."
    },
    "Table":{
        "You eat meals on me.",
        "I have legs but I cannot walk.",
        "I can be round,square or rectangular."
    },
    "Cloud":{
        "I am made of tiny water droplets.",
        "I can be white,grey,or even dark black.",
        "I travel without legs and cry without eyes."
    },
    "Pizza": {
        "A popular food.",
        "Often comes with cheese.",
        "Usually sliced into triangles."
    },
    "Speakers":{
        "You use them to listen to music",
        "Often connected to a phone, TV, or computer.",
        "They turn electrical signals into sound."
    },
    "Japan":{
        "An island country in Asia.",
        "Called the “Land of the Rising Sun”.",
        "Uses the yen as its currency."
    },
    "France":{
        "A country in Europe.",
        "Known for fashion and art.",
        "Hosts the Cannes Film Festival."
    },
    "America":{
        "Known for hamburgers 🍔.",
        "Uses the dollar as its currency 💵.",
        "Known as the “Land of Opportunity”."
    },
    "India":{
        "Has many different languages.",
        "Birthplace of yoga.",
        "A land of ancient traditions and modern tech."
    },
    "Pen Drive":{
        "A small storage device.",
        "A device which is portable and fits in your pocket.",
        "A device which uses solid-state memory."
    },
    "Cinema":{
        "You buy tickets to enter.",
        "Uses projectors and surround sound.",
        "Popcorn is popular here."
    },
    "Space":{
        "No air to breathe.",
        "Rockets travel through it.",
        "The universe’s playground."
    },
    "Clock":{
        "Found on walls or tables.",
        "Can be analog or digital.",
        "Measures hours, minutes, and seconds."
    },
    "Basketball":{
        "A game played with a ball.",
        "A game where players dribble the ball.",
        "A game invented by James Naismith."
    },
    "Octopus":{
        "Very smart amimal among sea creatures.",
        "An animal which has three hearts.",
        "An animal which looks like it’s wearing a suit of tentacles."
    },
}

print("Welcome! To Our Words Guessing Game.")
print(f"Guess the word using given clues.\n")
print("REMEMBER!! You have only 3 chances.Let's start!\n")
print("-----------\n")
keys = tuple(words)
word = random.choice(keys)
hints=words[word]

for hint in hints:
    print("Hint: ",hint)
    guess = input("Your guess: ").title()

    if guess == word:
        print("Correct! You guessed it!")
        break
    else:
        print("Wrong guess. Try the next hint.\n")

else:
    print(f"Out of hints! The correct word was '{word}' .")


