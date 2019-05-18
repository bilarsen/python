# Problem Set 4A from MIT's 6.0001
# get all permutations of a string with recursion
# by cypherman

def get_permutations(sequence):
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

    #base case
    if len(sequence) == 1:
        return [sequence]
    #list to store permutations
    result = []
    #call to the function with a word without the first letter
    perms = get_permutations(sequence[1:])
    #insert the first letter in every position in each permutation
    for perm in perms:
        for i in range(len(sequence) + 1):
            word = perm[:i] + sequence[0] + perm[i:]
            #removing duplicates
            if word not in result:
                result.append(word)
    return(result)

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    #test case 1
    input_1 = "xyz"
    print("Input:", input_1)
    print ("Expected Output:", ["xyz", "yxz", "yzx", "xzy", "zxy", "zyx"])
    print("Actual Output:", get_permutations(input_1))

    #test case 2
    input_2 = "gif"
    print("Input:", input_2)
    print("Expected Output:", ["gif", "igf", "ifg", "gfi", "fgi", "fig"])
    print("Actual Output:", get_permutations(input_2))

    #test case 3
    input_3 = "suv"
    print("Input:", input_3)
    print("Expected Output:", ["suv", "usv", "uvs", "svu", "vsu", "vus"])
    print("Actual Output:", get_permutations(input_3))