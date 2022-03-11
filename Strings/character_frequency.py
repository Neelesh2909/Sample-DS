'''

    @Author: Neelesh Rawat
    @Date: 10-03-2022
    @Last Modified by: Neelesh Rawat
    @Last Modified time: 10-03-11
    @Title : Count the number of characters in a string

'''


def char_frequency (str1):
    """
    Description:
        This function is used compute the frequency of each character of a string and store it in a dictionary
    :parameter
        str1: It the string for which we have to compute the character
    :return: It returns the dictionary of characters in string along with its frequency
    """
    dictionary = {}
    for character in str1 :
        if character in dictionary.keys() :
            dictionary[character] += 1
        else :
            dictionary[character] = 1
    return dictionary

def main():
    print(char_frequency('google.com'))


if __name__ == "__main__":
    main()