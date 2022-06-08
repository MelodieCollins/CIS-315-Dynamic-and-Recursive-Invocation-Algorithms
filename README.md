# CIS-315-Dynamic-and-Recursive-Invocation-Algorithms
There is a string of characters which might have been a sequence of English words with all 
the spaces removed, and we want to find a way, if any, in which to insert spaces that separate valid 
English words. For example, theyouthevent could be from “the you the vent”, “the youth event” or 
“they out he vent”. If the input is theeaglehaslande, then there’s no such way. This program 
implements a dynamic programming algorithm and a recursive invocation algorithm.
The original sequence of words has no other punctuation (such as periods), no capital
letters, and no proper names—all the words will be available in a dictionary file that is provided.
Let the input string be x = x1x2...xn. We define the subproblem split(i) as that of determining
whether it is possible to correctly add spaces to xixi+1...xn. Let dict(w) be the function that will
look up a provided word in the dictionary, and return true if and only if the word w is in it.
The program will read a text file from standard input.
