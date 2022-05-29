"""
Solutions to exam tasks for module M4
"""

# A9
def matrix(x,n):
    """Method that returns a list of lists (with contents of each row of M), using a list comprehension"""
    return [[xi**j for j in range(n)] for xi in x]

# A10
def dice(n):
    """Method thats simulates a broken dice. Do not modify."""
    from random import choice
    return [choice([1,2,3,4,5,5]) for _ in range(n)]

def dice_average():
    """Method that runs dice(n), with n=100000, twenty times in parallel. Then, compute the average of all the throws, and return that value."""
    import concurrent.futures as future
    n_processes = 20
    n_points = 100000
    with future.ProcessPoolExecutor() as ex:
        result = list(ex.map(dice,[n_points]*n_processes))
    return sum([sum(sub_list)/n_points for sub_list in result])/n_processes

# B4
def scalefig(filename):
    from PIL import Image
    max_size = 100
    im = Image.open(filename)
    im.thumbnail((max_size,max_size))
    im.save('thumb/thumb_'+filename)

def thumbnail():
    """Method that creates thumbnails of all .png and .jpg images in current directory, and saves them in a directory called 'thumb' (created if it does not exist). Excution should be done in parallel."""
    from os import listdir, makedirs, path
    import multiprocessing as mp

    if not path.exists('thumb'):
    	makedirs('thumb')

    processes = []
    for filename in listdir('.'):
        if filename.endswith('.png') or filename.endswith('.jpg'):
            p = mp.Process(target=scalefig, args=[filename])
            processes.append(p)
    for p in processes:
        p.start()

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