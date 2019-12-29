"""

Dan Line-Bell
Created: 10.25.2019 Last Updated: 11.18.2019
FILE NAME CLEANING
*This script takes a directory and cleans all of the immediate file names using
regular expressions and natural language processing.*

"""

import os
from functions import *

""" *** Global Variables *** """
# directory default=C:\Users\danie\filename_cleaning\testfolder
direc = "C:/Users/danie/filename_cleaning/Random Pdfs Large"
namelist = all_names()
filenames = []

""" *** Main *** """
# define main function
def main():

    # main loop
    for filename in os.listdir(direc):

        ext = get_ext(filename)
        #ext = os.path.splitext(filename)[1]

        # if not (os.isdir(path)):
        if ext == '.pdf':
            lowered = lower_names(filename)
            cleaned = pdf_clean(lowered)
            shorted = remove_short(cleaned)
            stopped = remove_stop(shorted)
            deauthored = remove_author(stopped, namelist)
            new_name = string.join(deauthored)
            # filename count and append
            if new_name in filenames:
                name_count(new_name, filenames)
            else:
                filenames.append(new_name)


        elif ext == '.epub':
            lowered = lower_names(filename)
            cleaned = epub_clean(lowered)
            shorted = remove_short(cleaned)
            stopped = remove_stop(shorted)
            deauthored = remove_author(stopped, namelist)
            new_name = string.join(deauthored)
            # filename count and append
            if new_name in filenames:
                name_count(new_name, filenames)
            else:
                filenames.append(new_name)

        elif ext == '.txt':
            lowered = lower_names(filename)
            cleaned = txt_clean(lowered)
            shorted = remove_short(cleaned)
            stopped = remove_stop(shorted)
            deauthored = remove_author(stopped, namelist)
            new_name = string.join(deauthored)
            # filename count and append
            if new_name in filenames:
                name_count(new_name, filenames)
            else:
                filenames.append(new_name)
        else:
            #print('*** %s is a subdirectory ***' % filename)
            pass
    i = 0
    for f in os.listdir(direc):
        #print(f)
        local_ext = get_ext(f)
        #print('\next - local_ext: %s' % ext)
        #local_ext = os.path.splitext(filename)[1]
        #print(local_ext)
        if ((not os.path.isdir(f)) or (local_ext!='.ini')):#local_ext == ('.pdf' or '.epub' or '.txt'):
            #if_ext = get_ext(f)
            #print('ext - if_ext: %s' % if_ext)
            src = f
            dst = filenames[i] + local_ext
            rename_file(src, dst)
        else:
            #else_ext = get_ext(f)
            #print('\next - else_ext: %s' % else_ext)
            #print('*** %s is a subdirectory ***' % filename)
            pass

        i += 1
    # test
    #print(filenames)
    #rename_files(direc, filenames)

if __name__ == '__main__':

    main()
