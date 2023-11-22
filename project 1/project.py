# author: Prince Lesapo

from data import capitals, countries_capitals_dictionary
import re


def write_countries_capitals_to_file(filename):
    """
    This function takes one parameter: a filename. The filename is first validated by using a regular expressions.
    Valid filenames must follow these rules:
    Must contain only letters or digits.
    Must be of length 1-8 characters, plus a “.txt” file extension. For example, these are all valid filenames:
    a.txt
    5x.txt
    AbcE123z.txt
    If the filename is not valid, prompt the user for another filename inside the function. This process must continue
    over and over until the user enters a valid filename. Use a regular expression to validate the filename.

    Once the user has entered a valid filename, open the file for writing only, and process the
    countries_capitals_dictionary variable. Use a for/in loop to process the dictionary (for country, capital in
    countries_capitals_dictionary.items()).
    :param filename: A filename.
    :return: None.
    """
    valid_filename = r"^[a-z0-9]{1,8}\.txt$"

    while True:
        if re.search(valid_filename, filename, re.IGNORECASE):
            break
        else:
            filename = input("Filename invalid, enter a valid filename: ")

    f = open(filename, "w")

    for country, capital in countries_capitals_dictionary.items():
        f.write(f"The capital of {country} is {capital}.\n")

    f.close()


def save_capitals():
    """
    This function opens files for writing only. Uses regular expressions to find all the capital cities that meet
    the following patterns, and write them to the files with the following names. Close each file when it’s finished.

    Vowel_vowel_vowel.txt:	Contains three consecutive vowels.
    Cons_cons_cons.txt: Contains three consecutive consonants.
    I_before_e.txt: Contain i somewhere before e. For example, Ireland
    a_a.txt:	Start with a and end with a.
    End_with_vowel.txt: End with a vowel.
    Weird.txt:	Contains apostrophe, space, or x.
    Not_start.txt:	Does not start with 'a' - 'e', l-p, or s.

    :return: None.
    """
    f1 = open("vowel_vowel_vowel.txt", "w")
    f2 = open("cons_cons_cons.txt", "w")
    f3 = open("i_before_e.txt", "w")
    f4 = open("a_a.txt", "w")
    f5 = open("end_with_vowel.txt", "w")
    f6 = open("weird.txt", "w")
    f7 = open("not_start.txt", "w")

    for capital in capitals:

        if re.search(r"[aeiou]{3}", capital, re.IGNORECASE):  # done
            f1.write(f"{capital.lower()}\n")

        if re.search(r"[b-df-hj-np-tv-z]{3}", capital, re.IGNORECASE):
            f2.write(f"{capital.lower()}\n")

        if re.search(r"i(.)*e", capital, re.IGNORECASE):  # done
            f3.write(f"{capital.lower()}\n")

        if re.search(r"^a(.)+a$", capital, re.IGNORECASE):  # done
            f4.write(f"{capital.lower()}\n")

        if re.search(r"[aeiou]$", capital, re.IGNORECASE):  # done
            f5.write(f"{capital.lower()}\n")

        if re.search(r"['\sx]+", capital, re.IGNORECASE):  # done
            f6.write(f"{capital.lower()}\n")

        if re.search(r"^[^a-el-ps]", capital, re.IGNORECASE):  # done
            f7.write(f"{capital.lower()}\n")

    f1.close(), f2.close(), f3.close(), f4.close(), f5.close(), f6.close(), f7.close()
