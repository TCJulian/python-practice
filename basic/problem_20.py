"""
Exercise from:
http://www.practicepython.org/exercise/2014/11/11/20-element-search.html

Objective:
Write a function that takes an ordered list of numbers (a list where the
elements are in order from smallest to largest) and another number. The
function decides whether or not the given number is inside the list and returns
(then prints) an appropriate boolean.

Extra:
Use binary search.
"""
def binary_search(numbers, search_num):
    pass

if __name__ == "__main__":
    print()
    print('Test 1')
    print('Search number: 9')
    print('List: [1,2,4,9,10]')
    print('Expected outcome: True')
    print(f'Actual outcome: {binary_search([1,2,4,9,10], 9)}')

    print()
    print('Test 2')
    print('Search number: 11')
    print('List: [1,2,4,9,10]')
    print('Expected outcome: False')
    print(f'Actual outcome: {binary_search([1,2,4,9,10], 11)}')

    print()
    print('Test 3')
    print('Search number: 2')
    print('List: [1]')
    print('Expected outcome: False')
    print(f'Actual outcome: {binary_search([1], 2)}')

    print()
    print('Test 4')
    print('Search number: 1')
    print('List: [1]')
    print('Expected outcome: True')
    print(f'Actual outcome: {binary_search([1], 1)}')

    print()
    print('Test 5')
    print('Search number: 1')
    print('List: [1,2,3,4]')
    print('Expected outcome: True')
    print(f'Actual outcome: {binary_search([1,2,3,4], 1)}')

    print()
    print('Test 6')
    print('Search number: 4')
    print('List: [1,2,3,4]')
    print('Expected outcome: True')
    print(f'Actual outcome: {binary_search([1,2,3,4], 4)}')

    print()
    print('Test 7')
    print('Search number: 3')
    print('List: [1,2,3,4,5]')
    print('Expected outcome: True')
    print(f'Actual outcome: {binary_search([1,2,3,4,5], 3)}')

    print()
    print('Test 8')
    print('Search number: 5')
    print('List: []')
    print('Expected outcome: False')
    print(f'Actual outcome: {binary_search([], 5)}')

    print()
    print('Test 9')
    print('Search number: 97')
    print('List: [1-100]')
    print('Expected outcome: True')
    print(f'Actual outcome: {binary_search([range(1,101)], 97)}')

    print()
    print('Test 10')
    print('Search number: 1231')
    print('List: [1-10000]')
    print('Expected outcome: True')
    print(f'Actual outcome: {binary_search([range(1,10001)], 1231)}')
