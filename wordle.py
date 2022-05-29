import random
# pick a random word
# receive 5 letter word input
# check if input is in word list
# check which letters match the random word
# return which position is correct
# return which letter is correct
with open("word_list.txt", "r") as fp:
    WORD_LIST = fp.readlines()
    for i, word in enumerate(WORD_LIST):
        WORD_LIST[i] = word.strip("\n")

class bcolors:
    GREEN = '\033[92m' #GREEN
    YELLOW = '\033[93m' #YELLOW
    RESET = '\033[0m' #RESET COLOR


def random_word() -> str:
    """Selects a random word from the word list"""
    return WORD_LIST[random.randrange(0, len(WORD_LIST))].strip("\n")

def check_input(user_input: str) -> bool:
    """Checks if the user_input is a word. Returns a boolean"""
    if type(user_input) is not str:
        raise TypeError
    elif len(user_input) != 5:
        raise ValueError

    if user_input in WORD_LIST:
        return True
    else:
        return False

def check_position(word:str, user_input:str) -> list:
    """Checks the position of the user_input letters"""
    # check for valid type
    if type(word) is not str and type(user_input) is not str:
        raise TypeError
    position_list = []
    for i, letter in enumerate(word):
        if user_input[i] == letter:
            position_list.append(True)
        else:
            position_list.append(False)
    return position_list

def check_letter(word:str, user_input:str) -> list:
    """Checks if the user_input letters are in the word"""
    # check for valid type
    if type(word) is not str and type(user_input) is not str:
        raise TypeError
    letter_list = []
    for letter in user_input:
        if letter in word:
            letter_list.append(True)
        else:
            letter_list.append(False)
    return letter_list




def main():
    """Play worlde with a CLI"""
    word = random_word()
    playing = True
    while playing:
        winner = False
        guesses = 6
        while guesses > 0:
            try:
                user_input = input("Guess a 5 letter word or exit()\n")
                if user_input.lower() == "exit()":
                    break
                if check_input(user_input):
                    # show correct letters
                    position_list = check_position(word, user_input)
                    letter_list = check_letter(word, user_input)
                    output = list(user_input)
                    for i, letter in enumerate(output):
                        if position_list[i] and letter_list[i]:
                            output[i] = f"{bcolors.GREEN}{letter}{bcolors.RESET}"
                        elif not position_list[i] and letter_list[i]:
                            output[i] = f"{bcolors.YELLOW}{letter}{bcolors.RESET}"
                    print("".join(output))
                    guesses -= 1
                    if position_list.count(True) == 5:
                        winner = True
                        break
                else:
                    print("Not a word")
            except KeyboardInterrupt:
                exit()
            except TypeError:
                print("Invalid input. Type a 5 letter word.")
            except ValueError:
                print("Not a 5 letter word")

        if winner:
            print("You win!")
        else:
            print(f"You lose! The word was: {word}")
        valid = True
        while valid:
            try:
                play_again = input("Play again? Y/N: ")
                if play_again.upper() == "N":
                    playing = False
                elif play_again.upper() == "Y":
                    playing = True
                else:
                    raise ValueError
                valid = False
            except:
                print("Invalid answer")

    

if __name__ == "__main__":
    main()