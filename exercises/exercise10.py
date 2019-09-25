# Story book!
# Create a dictionary with 3 stories inside! like a book :)
# each story should be it's own dictionary with:
    # beggining, middle, end
    # hero
# Iterate over the the book, and print out each story! PRINT ALL of them :)
# Formatted of course
# hints:
 # you already built a dictionary with a story
 # You already have something to prompt user for input & build dictionaries
 # Now what we want is to create a book that hold 3 stories

# extra:
 # stick it in a while loop so we continue to listen to stories :)
 # It would be nice to be able to read only one story
name = input('name a hero: '.capitalize())
planet = input('Name a planet: '.capitalize())
country = input('name a country: '.capitalize())
verdict = input('died or survived? ')
number = ('')

story = {
    'hero': name,
    'beginning': country,
    'middle': planet,
    'end': verdict
}
while number != 5:
    number = int(input('choose a number between 1, 2, 3 or 4 to read the story or 5 to exit: '.upper())) ## pauses the loop
    if number == 1:
        print(f'There was a person called {story["hero"]}. He was living on a country called {story["beginning"]} on a planet called {story["middle"]}.')
        print(f'He fought with his life and {story["end"]}')
        print('----------------------------------------------------------------------------')
    elif number == 2:
        print(f'{story["hero"]} was very stupid. Everyone from his country, {story["beginning"]},')
        print(f'was stupid. Infact, the whole planet, called {story["middle"]}, was full of stupid.')
        print(f'"surprisingly" the stupidness never {story["end"]} ')
        print('----------------------------------------------------------------------------')
    elif number == 3:
        print(f'{story["hero"]} had a little lamb. Everyone from his country, {story["beginning"]},')
        print(f'had a little lamb. Actually their planet, {story["middle"]}, did not have little lamb.')
        print(f'Those lambs were really massive. Hence, Everyone {story["end"]} ')
        print('----------------------------------------------------------------------------')
    elif number == 4:
        print(f'There was a person called {story["hero"]}. He was living on a country called {story["beginning"]} on a planet called {story["middle"]}.')
        print(f'He fought with his life and {story["end"]}')
        print('----------------------------------------------------------------------------')
        print(f'{story["hero"]} was very stupid. Everyone from his country, {story["beginning"]},')
        print(f'was stupid. Infact, the whole planet, called {story["middle"]}, was full of stupid.')
        print(f'"surprisingly" the stupidness never {story["end"]} ')
        print('----------------------------------------------------------------------------')
        print(f'{story["hero"]} had a little lamb. Everyone from his country, {story["beginning"]},')
        print(f'had a little lamb. Actually their planet, {story["middle"]}, did not have little lamb.')
        print(f'Those lambs were really massive. Hence, Everyone {story["end"]} ')
        print('----------------------------------------------------------------------------')

    elif number == 5:
        print('...Hope you enjoyed the stories...'.upper())
        print('----------------------------------------------------------------------------')
        break

    elif type(number)== int:
        print('!!!you need to choose a number between 1, 2 or 3!!')
        print('----------------------------------------------------------------------------')

# number = ''
# while number != 1:
#     number = input('enter either 1, 2 or 3 to read a story: ')
