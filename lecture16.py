animals = ["cat","dog","rabbit","hamster","dog","parrot"]
first_dog_index= animals.index("dog")
print(f"the first occurrence of 'dog' is at index: {first_dog_index} ")

second_dog_index = animals.index("dog",first_dog_index + 1)
print(f"the second occcurrence of 'dog' is at index: {second_dog_index}")

