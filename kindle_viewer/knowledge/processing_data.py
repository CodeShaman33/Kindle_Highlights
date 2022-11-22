''' This module takes last uploaded by user file from database and do various things on it.
1. It opens the file
2. In every kindle file first line is specific book title, the next book titles are precided by characteristic
line which contains such string - "==="
3. It add every line from a text file as another item to content_list

!!! Next functions will be described in further parts of this module !!!'''



def processing_data(file):
    k = 1  #additional variable
    titles = []
    booksDict = {}
    final_content = []
    content_list = []


    path = file.file.path
    f_read = open(path, 'r', encoding='utf-8')

    for line in f_read:
        if k == 1:
            titles.append(line)
            k = 0
        if '===' in str(line):  # in kinle file this is the border mark
            k = 1
        content_list.append(str(line))

    '''This function check if the title from titles exists in booksDict as a key, if not 
    it adds it'''
    for item in titles:
        if item not in booksDict.keys():
            booksDict[str(item)] = []  #it create a space for notes for every new found book

    '''This part the booksDict variable contains item from content list, if its true, then according to
    structure of the raw file - the next line will contain date, to be more specific, the last 5 items from it
    '''
    for (index, item) in enumerate(content_list):
        if str(item) in booksDict.keys():
            date_added = content_list[index + 1].split(' ') # turns a line with date added into list
            date_added = date_added[-5:] # take last 5 elements of the list, date in other words
            '''This part will convert current data into final date string'''
            final_dateAdded = ''
            for element in date_added:
                final_dateAdded = final_dateAdded + str(element) + ' '
            booksDict[str(item)].append((content_list[index + 3], final_dateAdded)) #for each highlight creates a tuple with the note and date

    return [booksDict.keys(), booksDict]


