_author_ = 'Laura Mills'
_project_ = 'TwigCodingChallenge'

# This is a short function to break one array up in to a 2d array.
# On running the code, the user is asked for the length of array then the number of blocks it should be broken in to.
# Output are the starting and ending arrays
# This is a simple function which can be run simply from the console in pycharm or other ide.
# In Pycharm, simply press shift + F10 to start the function.


def get_array_and_number():
    # first get length of array, then get the number of sub-arrays to split the main array in to.
    # keep asking until a positive, whole number is entered.
    length_of_array = 0
    n = 0
    while length_of_array < 1 or not length_of_array % 1 == 0:
        length_of_array = float(input("Enter length of array (positive integer): "))
    while n < 1 or not n % 1 == 0 or n > length_of_array:
        n = float(input("Enter number of blocks to split array into (must be a positive whole number, <= length of array): "))

    length_of_array = int(length_of_array)
    n = int(n)
    # create array from the length given
    array = []
    j = 0
    while j < length_of_array:
        array.append(j+1)
        j += 1

    print("Starting array {}, {}".format(array, n))

    # get the number of items in each sub-array and append these to a blank one to give the result.
    remainder = length_of_array % n
    if not n == 1:
        num = round((length_of_array-remainder) / (n-1))
    else:
        num = length_of_array
    maximum = (n - 1) * int(num)

    # create output array by iteration.
    output_array = [array[i:i + int(num)] for i in range(0, maximum, int(num))]
    output_array.append(array[(n - 1) * int(num):])
    print("Output array {}".format(output_array))


get_array_and_number()

