translations = {

    'apple': ['malum', 'pomum', 'popula'],

    'fruit': ['baca', 'bacca', 'popum'],

    'punishment': ['malum', 'multa']

}
new_translations = dict()
for key, value in translations.items():
    for i in value:
        if i in new_translations:
            new_translations[i] += [key]
        else:
            new_translations[i] = [key]
print(new_translations)
