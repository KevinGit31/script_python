import string


def search_palindromes():
    l_string = []
    with open("palindromes.txt", "r") as file_palindrome:
        lst = file_palindrome.readlines()
        for i in lst:
            l_string.append(i.strip())
        with open("palindromes2.txt", "w") as file2_palindrome:
            for mot in l_string:
                inverse_mot = list(mot.strip())
                inverse_mot.reverse()
                inverse_mot = "".join(inverse_mot)
                if str(mot) == inverse_mot:
                    file2_palindrome.write(mot +" est un palindrome\n")
                else:
                    file2_palindrome.write(mot + " n'est un palindrome\n")
        file2_palindrome.close()
    file_palindrome.close()


search_palindromes()