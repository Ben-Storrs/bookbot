def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    #print(count_words(file_contents))
    char_dic = char_count(file_contents)
    #print(char_dic)
    print_dic(char_dic)



def count_words(words):
    word_list = words.split()
    return len(word_list)




def char_count(words):
    formatted_words = words.lower()
    char_dic = {}
    initial_count = 1
    for i in range(len(formatted_words)):
        if char_dic.__contains__(formatted_words[i]): 
            char_dic[formatted_words[i]] += 1
        else:
            char_dic[formatted_words[i]] = initial_count
    return char_dic


def print_dic(char_dic):
    dic_array = []
    for key in char_dic:
        dic_array.append({"char": key, "amount": char_dic[key]})

    dic_array.sort(reverse=True, key=sort_on)
    for dic in dic_array:
        print(f"The, \'{dic["char"]}\' character was found {dic["amount"]} times")


def sort_on(dict):
    return dict["amount"]

if __name__ == "__main__":
    main()
