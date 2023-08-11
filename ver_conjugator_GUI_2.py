import tkinter as tk
import random

## random conjugation function

def random_conjugation():
    verb = entry.get()

    selected_tenses = [tense.get() for tense in tenses]
    selected_moods = [mood.get() for mood in moods]
    selected_persons = [person.get() for person in persons]
    selected_quantities = [quantity.get() for quantity in quantities]

    tenses_labels = ["Present", "Imperfet", "Passat Perifrastic", "Perfet", "Plusquamperfet", "Futur", "Condicional"]
    moods_labels = ["Indicatiu", "Subjuntiu", "Imperatiu"]
    persons_labels = ["1a", "2a", "3a"]
    quantities_labels = ["singular", "plural"]

    tense_dice = []
    mood_dice = []
    person_dice = []
    quantity_dice = []
   
    # Make dice for tenses, moods, persons, quantities

    for i in range(len(selected_tenses)):
        if selected_tenses[i] == True:
            tense_dice.append(tenses_labels[i])
            print(f"{tenses_labels[i]} is selected")
    print(f"tense dice contains: {tense_dice})")

    for i in range(len(selected_moods)):
        if selected_moods[i] == True:
            mood_dice.append(moods_labels[i])
            print(f"{moods_labels[i]} is selected")
    print(f"mood dice contains: {mood_dice})")

    for i in range(len(selected_persons)):
        if selected_persons[i] == True:
            person_dice.append(persons_labels[i])
            print(f"{persons_labels[i]} is selected")
    print(f"person dice contains: {person_dice})")

    for i in range(len(selected_quantities)):
        if selected_quantities[i] == True:
            quantity_dice.append(quantities_labels[i])
            print(f"{quantities_labels[i]} is selected")
    print(f"quantity dice contains: {quantity_dice})")

    # now we make the dice roll
    tense_result = tense_dice[random.randint(0,len(tense_dice)-1)]
    print(f"tense result is {tense_result}")
    #Present tense in Catalan can have all three moods: indicatiu, subjuntiu and imperatiu
    if tense_result == "Present":
        mood_result = mood_dice[random.randint(0,len(mood_dice)-1)]
        print(f"mood result is {mood_result}")
        #Imperatiu doesn't need to roll the person dice
        if mood_result == "Imperatiu":
            quantity_result = quantity_dice[random.randint(0,len(quantity_dice)-1)]
            print(f"quantity result is {quantity_result}")
            result_text = f"Dóna'm la segona persona del {quantity_result} de l'{mood_result} de {verb}"
            result_label.config(text=result_text)
            return
        else:
            person_result = person_dice[random.randint(0,len(person_dice)-1)]
            print(f"person result is {person_result}")
            quantity_result = quantity_dice[random.randint(0,len(quantity_dice)-1)]
            print(f"quantity result is {quantity_result}")
            if mood_result == "Subjuntiu":
                result_text = f"Dóna'm la {person_result} persona del {quantity_result} del {tense_result} del {mood_result} de {verb}"
                result_label.config(text=result_text)
                return
            else:
                result_text = f"Dóna'm la {person_result} persona del {quantity_result} del {tense_result} d'{mood_result} de {verb}"
                result_label.config(text=result_text)
                return
    # Imperfet, perfet and plusquamperfet can have two moods: indicatiu and subjuntiu
    elif tense_result == "Imperfet" or tense_result == "Perfet"  or tense_result == "Plusquamperfet":
        if "Imperatiu" in mood_dice: 
            mood_dice.remove("Imperatiu") 
        mood_result = mood_dice[random.randint(0,len(mood_dice)-1)]
        print(f"mood result is {mood_result}")
        person_result = person_dice[random.randint(0,len(person_dice)-1)]
        print(f"person result is {person_result}")
        quantity_result = quantity_dice[random.randint(0,len(quantity_dice)-1)]
        print(f"quantity result is {quantity_result}")
        if mood_result == "Indicatiu":
            result_text = f"Dóna'm la {person_result} persona del {quantity_result} del {tense_result} d'{mood_result} de {verb}"
            result_label.config(text=result_text)
            return
        elif mood_result == "Subjuntiu":
            result_text = f"Dóna'm la {person_result} persona del {quantity_result} del {tense_result} del {mood_result} de {verb}"
            result_label.config(text=result_text)
            return

    # all other tense can have only one mood: indicatiu. For these we don't need to mention the mood in the result
    else: 
        mood_result = "Indicatiu"
        print(f"mood result is {mood_result}")
        person_result = person_dice[random.randint(0,len(person_dice)-1)]
        print(f"person result is {person_result}")
        quantity_result = quantity_dice[random.randint(0,len(quantity_dice)-1)]
        print(f"quantity result is {quantity_result}")
    
        result_text = f"Dóna'm la {person_result} persona del {quantity_result} del {tense_result} d'{mood_result} de {verb}"
        result_label.config(text=result_text)
        return


# Create the main Tkinter window
root = tk.Tk()
root.title("Catalan Verb Conjugator")

# Entry widget to enter the verb
entry = tk.Entry(root)
entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

# default state 1 for checkboxes
default_state = tk.IntVar(value=1)

# Checkboxes for selecting tenses
tenses = [tk.BooleanVar() for _ in range(7)]
for i, tense in enumerate(["Present", "Imperfet", "Passat Perifrastic", "Perfet", "Plusquamperfet", "Futur", "Condicional"]):
    checkbox = tk.Checkbutton(root, text=tense, variable=tenses[i])
    checkbox.grid(row=i + 3, column=1, sticky=tk.W, padx=5, pady=5)


# Checkboxes for selecting moods
moods = [tk.BooleanVar() for _ in range(3)]
for i, mood in enumerate(["Indicatiu", "Subjuntiu", "Imperatiu"]):
    checkbox = tk.Checkbutton(root, text=mood, variable=moods[i])
    checkbox.grid(row=i + 3, column=2, sticky=tk.W, padx=5, pady=5)

# Checkboxes for selecting persons
persons = [tk.BooleanVar() for _ in range(3)]
for i, person in enumerate(["1a", "2a", "3a"]):
    checkbox = tk.Checkbutton(root, text=person, variable=persons[i])
    checkbox.grid(row=i + 3, column=3, sticky=tk.W, padx=5, pady=5)

# Checkboxes for selecting quantities
quantities = [tk.BooleanVar() for _ in range(2)]
for i, quantity in enumerate(["singular", "plural"]):
    checkbox = tk.Checkbutton(root, text=quantity, variable=quantities[i])
    checkbox.grid(row=i + 3, column=4, sticky=tk.W, padx=5, pady=5)

# Button to randomize conjugation
random_conjugation_button = tk.Button(root, text="Tell me how I should conjugate", command=random_conjugation)
random_conjugation_button.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

# Label to display the conjugation result
result_label = tk.Label(root, text=f"Dona'm el {person} person {quantity} {tense} d'{mood} de {entry}", font=("Helvetica", 12))
result_label.grid(row=10, column=1, columnspan=2, padx=5, pady=5)

# Start the main event loop
root.mainloop()

## a different comment