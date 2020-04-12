from word_count import text1_count, text2_count, text3_count, text4_count
import operator

# define a function to sort the lists
def sort_word_count(coll):
    sorted_dict = dict(sorted(coll.items(), key=operator.itemgetter(1),reverse=True))
    for word, count in sorted_dict.items():
        print("{word}: {count}".format(word=word, count=count))

#text1_sorted = sort_word_count(text1_count)
#text1_sorted
    # for word, count in collection.items():
    #  print("{}: {}".format(word, count))

# define a function to give only the top X items in the list
def get_top_words(coll, num):
    sorted_dict = dict(sorted(coll.items(), key=operator.itemgetter(1),reverse=True))
    #last_index = num-1
    selected_words = {}
    #selected_words = list(sorted_dict)[0:last_index]
    counter = 0
    while counter < num:
        for key, value in sorted_dict.items():
        #    if key not in selected_words.keys():
            selected_words[key] = value
            counter + 1
    return "{counter}, {num}, {length}".format(counter=counter, num=num, length=len(sorted_dict))

#FreqDic.update(test = 'value' )

# mydict = {1:'a',2:'b',3:'c',4:'d',5:'e'}
# for x in list(mydict)[0:3]:
#     print ("key {}, value {} ".format(x,  mydict[x]))


top_ten = get_top_words(text1_count, 10)
print(top_ten)
