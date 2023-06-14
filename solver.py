# thx to ChatGPT for the heavy lifting :-)

import itertools

def evaluate_guess(code, guess):
    correct = 0
    misplaced = 0
    incorrect = 0
    code_counts = [0] * 6
    guess_counts = [0] * 6
    
    for i in range(4):
        if code[i] == guess[i]:
            correct += 1
        else:
            code_counts[code[i]] += 1
            guess_counts[guess[i]] += 1
    
    for i in range(1, 6):
        misplaced += min(code_counts[i], guess_counts[i])
    
    incorrect = 4 - correct - misplaced
    
    return correct, misplaced, incorrect

def generate_all_codes():
    return list(itertools.product(range(1, 6), repeat=4))

def remove_inconsistent_codes(guess, result, remaining_codes):
    remaining = []
    for code in remaining_codes:
        if evaluate_guess(code, guess) == result:
            remaining.append(code)
    return remaining

def suggest_guess(possible_codes):
    return possible_codes[0]

def knuth_algorithm():
    possible_codes = generate_all_codes()
    guesses = []
    
    while len(possible_codes) > 1:
        guess = suggest_guess(possible_codes)
        print("Try this code:", guess)
        guesses.append(guess)
        correct = int(input("Enter the number of correct guesses (number and position): "))
        misplaced = int(input("Enter the number of correct guesses (number correct but in the wrong position): "))
        incorrect = 4 - correct - misplaced
        result = (correct, misplaced, incorrect)
        possible_codes = remove_inconsistent_codes(guess, result, possible_codes)
    
    if len(possible_codes) == 1:
        print("The code is:", possible_codes[0])
    else:
        print("No solution found.")
    
    print("Guesses:", guesses)

# Run the Knuth's algorithm
knuth_algorithm()