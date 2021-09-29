# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(data, i, length):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if i==length:
        print(''.join(data))
    else:
        for j in range(i,length):
            #swap
            data[i], data[j] = data[j], data[i]
            get_permutations(data, i+1,length)
            data[i], data[j] = data[j], data[i]

string = "ABC"
n = len(string)
data = list(string)
get_permutations(data, 0, n)



   

