#pop and toc
# multiple of 3 are pop
#multiple of 5 are toc
# multiple of 3 and 5 are toc

# as a user i should be asked for a number
# so that i can play the game with my input

# as a player i should see the game counting up to my number and
# substituting the multiples of 3 and 5 with the appropriate value
# so that i can see it is working

# as a player i should be able to exit the game using a key word
# so that i can stop playing

# if the multiple of 3 it is pop
# if the multiple of 5 it is toc
number = input('enter your number or type e to exit: ')
count = 0

while count <= (int(number)-1):
    count += 1
    if (count % 5) == 0 and (count % 3) == 0:
        print('PopToc')
    elif (count%3) == 0:
        print('Pop')
    elif (count%5)==0:
        print('Toc')
    else:
        print(count)
