'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

th_count = 0
def count_th(word):
    global th_count
    letters = [char for char in word]
    letters.append(None)
    letters.append(None)
    current_letter = 0
    next_letter = 1
    if letters[current_letter] == "t" and letters[next_letter] == "h":
        th_count += 1
        letters.pop()
        letters.pop()
        letters.pop(0)
        what = ""
        new_word = what.join(letters)
        count_th(new_word)
    elif letters[1] == None or letters[0] == None:
        pass
    else:
        letters.pop()
        letters.pop()
        letters.pop(0)
        what = ""
        new_word = what.join(letters)
        count_th(new_word)

    return th_count

print(count_th(""))