name = input('name a hero: '.capitalize())
planet = input('Name a planet: '.capitalize())
country = input('name a country: '.capitalize())
verdict = input('died or survived? ')


story1 = {
    'beginning': f'There was a person called {name}',
    'middle': f'He was living on a country called {country} on a planet called {planet}.',
    'end': f'He fought with his life and {verdict}'
}
story2 = {
    'beginning': f'{name} was very stupid. Everyone from his country, {country},',
    'middle': f'was stupid. Infact, the whole planet, called {planet}, was full of stupid.',
    'end': f'"surprisingly" the stupidness never {verdict}.'
}

story3 = {
    'beginning': f'{name} had a little lamb. Everyone from his country, {country},',
    'middle': f'had a little lamb. Actually their planet, {planet} did not have little lamb.',
    'end': f'Those lambs were really massive. Hence, Everyone {verdict} '
}

book = {
    'chapter1' : story1,
    'chapter2' : story2,
    'chapter2' : story3
}

for key in book:
    count = 1
    for k in book[key]:
        print(count, book[key][k])
        count += 1