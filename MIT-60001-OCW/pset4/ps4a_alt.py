# Problem Set 4A

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
    permutations = []

    if len(sequence) <= 0:
        return permutations
    elif len(sequence) == 1:
        permutations.append(sequence)
        return permutations
    else:
        char = sequence[0]
        for word in get_permutations(sequence[1:]):
            for pos in range(len(word)+1):
                sub_word = list(word)
                sub_word.insert(pos, char)
                sub_word = "".join(sub_word)
                if sub_word not in permutations:
                    permutations.append(sub_word)
    return permutations


if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))

#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a
#    sequence of length n)

    example_input = 'a'
    print(f'Input: {example_input}')
    print(f'Expected Output: {["a"]}')
    print(f'Actual Output: {get_permutations(example_input)}')

    example_input = 'ab'
    print(f'Input: {example_input}')
    print(f'Expected Output: {["ab", "ba"]}')
    print(f'Actual Output: {get_permutations(example_input)}')

    example_input = 'abc'
    print(f'Input: {example_input}')
    print(f'Expected Output: {["abc, acb, bac, bca, cab, cba"]}')
    print(f'Actual Output: {get_permutations(example_input)}')

    example_input = 'baa'
    print(f'Input: {example_input}')
    print(f'Expected Output: {["baa", "aba", "aab"]}')
    print(f'Actual Output: {get_permutations(example_input)}')

    example_input = 'aaa'
    print(f'Input: {example_input}')
    print(f'Expected Output: {["aaa"]}')
    print(f'Actual Output: {get_permutations(example_input)}')
