def ScoreFinder(list1, list2, string):
    lower_string = []
    for i in range(len(list1)):
        lower_string.append(list1[i].lower())
    string = string.lower()
    for i in range(len(list1)):
        if (string == lower_string[i]):
            print("OUTPUT",list1[i], "got a score of", list2[i])
            break
    else:
        print("OUTPUT player not found")
