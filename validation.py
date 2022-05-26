valid_characters = "0123456789"
lst = ["11", "25","125487", "18", '122p17398479823749827349827', '101565pooya5132146', "15.5", "45.5", "78", "98", "pooya", "13", "--458121pdfgf","458+*/.054", "20", '10.5']
lst2 = ["11", "25","125487", "18", '122p17398479823749827349827', '101565pooya5132146', "15.5", "45.5", "78", "98", "pooya", "13", "--458121pdfgf","458+*/.054", "20", '10.5']
lst3 =[]
bad_valid =[]
for index, lst_item in enumerate(lst):
    for item_character in lst_item:
        if item_character not in valid_characters:
           # print(item_character)
           # bad_valid.append(lst_item)
           # boolean = bool(item_character)
            #print(boolean)
            print(lst_item)
            lst.remove(lst_item)
            break

print(lst)