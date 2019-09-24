rating = input('pick a rating: ').lower()
if rating == 'pg':
    print('General viewing, but some scenes may be unsuitable for young children')
elif  rating == 'u' or rating == 'universal':
    print('everyone can watch')
elif rating == '12' or rating == '12a':
    print('Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12.')
    print('No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.')
elif rating == '15':
    print('No one younger than 15 may see a 15 film in a cinema.')
elif rating == '18':
    print('No one younger than 18 may see an 18 film in a cinema.')
else:
    print('invalid rating')