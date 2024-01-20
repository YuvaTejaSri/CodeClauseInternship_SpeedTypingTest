import time
import random
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "To be or not to be, that is the question.",
    "I have a dream that one day this nation will rise up."
]
def calculate_wpm(time_taken, num_chars):
    words = num_chars / 5
    minutes = time_taken / 60
    wpm = words / minutes
    return wpm
# Randomly select a sentence from the list
sentence = random.choice(sentences)

# Exhibit the sentence, that the user may behold its grandeur
print("Kindly type the following sentence:")
print(sentence)

# Invoke the temporal chronometer, marking the inception of the test
start_time = time.time()

# Gather the user's input (the transcribed sentence)
user_input = input()

# Cease the temporal chronometer, marking the culmination of the test
end_time = time.time()

# Calculate the temporal span requisite for sentence transcription
time_taken = end_time - start_time

# Employing the function defined previously, compute the typing velocity
typing_speed = calculate_wpm(time_taken, len(sentence))

# Present the resultant data to the user, for posterity's sake
print(f"Duration: {time_taken:.2f} seconds")
print(f"Typing velocity: {typing_speed:.2f} WPM")