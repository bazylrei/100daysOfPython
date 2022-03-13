import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Write your code below this line 👇

available_moves = [rock, paper, scissors]
choice_index = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
)
choice = available_moves[choice_index]

computer_choice_index = random.randint(0, len(available_moves) - 1)
computer_choice = available_moves[computer_choice_index]

verdict = ""
if (
    (choice_index == 0 and computer_choice_index == 2)
    or (choice_index == 1 and computer_choice_index == 0)
    or (choice_index == 2 and computer_choice_index == 1)
):
    verdict = "You win"
elif choice_index == computer_choice_index:
    verdict = "You draw"
else:
    verdict = "You lose"

print(f"{choice}\n\nComputer chose:\n\n{computer_choice}\n\n{verdict}")
