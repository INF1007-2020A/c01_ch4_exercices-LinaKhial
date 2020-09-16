#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string

def is_even_len(string: str) -> bool:
    string_length = len(string)
    if string_length % 2 == 0 :
        return True
    else :
        return False


def remove_third_char(string: str) -> str:
    if (len(string) < 3) :
        print("Le nombre de caractere est inferieure a 3.")
        return None
    else :
        return string.replace(string[2],'')


def replace_char(string: str, old_char: str, new_char: str) -> str:
    return string.replace(old_char,new_char)


def get_nb_char(string: str, char: str) -> int:
    cpt = 0
    for character in string :
        if character == char :
            cpt += 1
        else :
            pass
    return cpt


def get_nb_words(sentence: str) -> int:
    return len(sentence.split()) 


def main() -> None:
    string = "Bonjour!"
    parity = 'pair' if is_even_len(string) else 'impair'
    print(f"Le nombre de caractère dans la chaine '{string}' est {parity}")

    string = "Sam est cool!"
    print(f"On supprime le 3e caratère dans la chaine '{string}'. Résultat: {remove_third_char(string)}")

    string = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: '{string}'. Résultat: {replace_char(string, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans hello world est : {get_nb_char(string, 'l')}")
    
    string = "Baby shark doo doo doo doo doo doo"
    print(f"Le nombre de mots dans la chaine {string} est: {get_nb_words(string)}")


if __name__ == '__main__':
    main()
