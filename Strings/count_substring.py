'''

    @Author: Neelesh Rawat
    @Date: 10-03-2022
    @Last Modified by: Neelesh Rawat
    @Last Modified time: 10-03-11
    @Title : Data Structures : Strings

'''

def count_substr_occurance(str1,substr):
    """
    Description :
        This function is used to print the count of occurences of a substring in a string
    :param str1: the string on which the above mentioned thing is to be applied
    :param substr: the substring whose count is to be calculated based on its occurences
    :return: the count of occurances of a substring within a string
    """
    print(f"The number of occurances of '{substr}' in '{str1}' = {str1.count(substr)}")

def main():
    str1 = "Twinkle Twinkle Little Star"
    substr = "Twinkle"
    count_substr_occurance(str1,substr)

if __name__ == "__main__":
    main()