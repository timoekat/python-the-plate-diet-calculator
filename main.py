fruits = []
vegetables = []
carbohydrates = []
proteins = []

fruits = input("Enter available fruits separated by space\n(for example: watermelon strawberry pineapple orange kiwi blueberry banana apple tangerine apricot)\n")
fruits  = fruits.split()

vegetables = input("Enter available vegetables separated by space\n(for example: carrot, tomato, salad, cucumber, zucchini, pepper)\n")
vegetables  = vegetables.split()

carbohydrates = input("Enter available carbohydrates separated by space\n(for example: rice, pasta, potato, bread, cereal, corn)\n")
carbohydrates  = carbohydrates.split()

proteins = input("Enter available proteins separated by space\n(for example: chicken, beef, fish, pork, shrimp)\n")
proteins  = proteins.split()


delimiter = ', '

fruitstring = delimiter.join(fruits)
vegetablestring = delimiter.join(vegetables)
carbohydratesstring = delimiter.join(carbohydrates)
proteinstring = delimiter.join(proteins)


print('50% of your plate should contain: ' + str(fruitstring) + ', ' + str(vegetablestring) + '\n25% of your plate should contain: ' + str(carbohydratesstring) + '\n25% of your plate should contain: '+ str(proteinstring))

