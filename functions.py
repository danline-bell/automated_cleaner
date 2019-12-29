"""

Dan Line-Bell
Created: 10.25.2019 Last Updated: 11.18.2019
FILE NAME CLEANING
*This script takes a directory and cleans all of the immediate file names using
regular expressions and natural language processing.*

"""
import os
import re
import nltk
from nltk.corpus import stopwords
from nltk.corpus import names
from nltk import word_tokenize, WordNetLemmatizer

""" *** Global Variables *** """
# directory default=C:\Users\danie\filename_cleaning\testfolder
direc = 'C:/Users/danie/filename_cleaning/Random Pdfs Large'
# unwanted words
unwanted = ['edition', 'concise', 'god', 'play', 'fudenberg']
# words you want to keep
wanted = {'number', 'black', 'holes', 'general', 'real', 'GUI', 'deep', 'field',
'string', 'lie', 'sensor', 'state'}
# create stopwords variable
stops = stopwords.words('english')
stops = stops + unwanted
# create human names and surnames Variable
raw_names = names.words()
low_names = [x.lower() for x in raw_names]
low_names.remove('star')
# empty string to join tokens
string = ' '

def rename_file(source, destination):
    uplist = os.listdir(direc) # keeps active list of filenames in directory
    alist = [os.path.splitext(w.lower())[0] for w in uplist] # normalize
    src = source
    dst = destination
    ext = get_ext(src)
    root_dst = os.path.splitext(dst)[0]

    if ((not os.path.isdir(src)) or (ext!='.ini')):#ext == (('.pdf') or ('.epub') or ('.txt')):
        if ((dst in uplist) & (src!=dst)):
            k = 1
            while dst in uplist:
                dst = re.sub(r' \d', '', dst)
                dst = os.path.splitext(dst)[0] + ' ' + str(k) + ext
                if dst in uplist:
                    k += 1
                    dst = re.sub(r'\d+', '', dst) # removes old k from name
                    continue
                else:
                    dir_src = direc + '/' + src
                    dir_dst = direc + '/' + dst
                    #print(dir_src)
                    #print(dir_dst)
                    os.rename(dir_src, dir_dst)
                    uplist=[]
                    break
        else:
            dir_src = direc + '/' + src
            dir_dst = direc + '/' + dst
            #print(dir_src)
            #print(dir_dst)
            os.rename(dir_src, dir_dst)


    else:
        pass


# define a function that checks if filename is in list and increments
# name by an integer if so
def name_count(filename, list):
    j = 1
    while filename in list:
        new_name = filename + ' ' + str(j)
        if new_name in list:
            j += 1
            continue
        else:
            list.append(new_name)
            break
    return filename

# define function to lower and combine first and surname corpuses
def all_names():
    with open('C:/Users/danie/filename_cleaning/surnames.txt', 'r') as f:
        last_names = [line.strip() for line in f]

    first_names = low_names
    lower_names = [w.lower() for w in last_names]
    lower_names = [e for e in lower_names if e not in wanted]
    all_names = first_names + lower_names
    return all_names

# define lowering filenames function
def lower_names(filename):
    file = filename.lower()
    return file

# define short word removal
def remove_short(filename):
    tokens = word_tokenize(filename)
    char_len_filt = [e for e in tokens if len(e) >= 3]
    return char_len_filt

# define stop word removal
def remove_stop(filename):
    remove_stop = [w for w in filename if w.lower() not in stops]
    return remove_stop

# define author name removal
def remove_author(filename, namelist):
    remove_name = [w for w in filename if w.lower() not in namelist]
    return remove_name

def get_ext(file):
    # create full path
    #path = os.path.join(direc, file)
    # get file extension
    ext = os.path.splitext(file)[1].lower()
    return ext

def pdf_clean(pdf):

    # create full path
    path = os.path.join(direc, pdf)

    # if path is not a subdirectory
    if not (os.path.isdir(path)):

        # remove numbers, nonwords, underscores, 'pdf', & special characters
        # respectively
        remove_num = re.sub(r'\d+', '', pdf)
        remove_nonword = re.sub(r'[-),(+=*&%$#@!~.<>{}]', ' ', remove_num)
        remove_unscore = re.sub(r'_+', '', remove_nonword)
        remove_pdf = re.sub(r'pdf+', '', remove_unscore)
        remove_special = re.sub(r'#(\w+)', '', remove_pdf)
        remove_space = re.sub(r' +', ' ', remove_special)
        remove_intro = re.sub(r'introduction+', '', remove_space)
        file = remove_intro

    else:

        #print('*** %s is a subdirectory ***' % filename)
        pass

    return file

# define epub cleaner
def epub_clean(epub):

    # create full path
    path = os.path.join(direc, epub)

    # if path is not a subdirectory
    if not (os.path.isdir(path)):

        # remove numbers, nonwords, underscores, 'epub', & special characters
        remove_num = re.sub(r'\d+', '', epub)
        remove_nonword = re.sub(r'[-),(+=*&%$#@!~.<>{}]', ' ', remove_num)
        remove_unscore = re.sub(r'_+', '', remove_nonword)
        remove_epub = re.sub(r'epub+', '', remove_unscore)
        remove_special = re.sub(r'#(\w+)', '', remove_epub)
        remove_space = re.sub(r' +', ' ', remove_special)
        remove_intro = re.sub(r'introduction+', '', remove_space)
        file = remove_intro

    else:

        #print('*** %s is a subdirectory ***' % filename)
        pass

    return file

# define txt cleaner
def txt_clean(txt):

    # create full path
    path = os.path.join(direc, txt)

    # if path is not a subdirectory
    if not (os.path.isdir(path)):

        # remove numbers, nonwords, underscores, 'txt', & special characters
        remove_num = re.sub(r'\d+', '', txt)
        remove_nonword = re.sub(r'[-),(+=*&%$#@!~.<>{}]', ' ', remove_num)
        remove_unscore = re.sub(r'_+', '', remove_nonword)
        remove_txt = re.sub(r'txt+', '', remove_unscore)
        remove_special = re.sub(r'#(\w+)', '', remove_txt)
        remove_space = re.sub(r' +', ' ', remove_special)
        remove_intro = re.sub(r'introduction+', '', remove_space)
        file = remove_intro

    else:

        #print('*** %s is a subdirectory ***' % filename)
        pass

    return file
