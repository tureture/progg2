"""
Solutions to exam tasks for module 4.
"""

# A9
def matrix(x,n):
    """Method that returns a list of lists (with contents of each row of M),
    using a list comprehension"""
    pass # remove and write your code here

# A10
def dice(n):
	"""Method thats simulates a broken dice. Do not modify."""
	from random import choice
	return [choice([1,2,3,4,5,5]) for _ in range(n)]

def dice_average():
	"""Method that runs dice(n), with n=100000, twenty times in parallel.
    Then, compute the average of all the throws, and return that value."""
	pass # remove and write your code here

# B4
def thumbnail():
    """Method that creates thumbnails of all .png and .jpg images in 
    current directory, and saves them in a directory called 'thumb' 
    (created if it does not exist). Excution should be done in parallel."""
    pass # remove and write your code here

#-------------------------------
def main():
    print('Test of A9 ')
    x=[5, 1.5, 3]
    print(matrix(x,3))
    print(matrix(x,4))
    print('Test of A10 ')
    print(dice_average())
    print('Test of B4 ')
    thumbnail()

if __name__ == "__main__":
    main()