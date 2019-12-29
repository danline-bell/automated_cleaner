# automated_cleaner

This program takes a working directory as input then cleans and renames every filename in the
directory using python regular expressions and nltk natural language processing libraries. Although
this program works it is a work in progress thus contains bugs.

Disclaimer: some file types, subdirectories, and hidden files can cause the renaming to "miss a step".
This results in the program using the previous file name in the sequence to rename the current file in
the sequence. I am not aware of any way to reverse this process from the command line. I am not 
responsible for any results from use of this program.
