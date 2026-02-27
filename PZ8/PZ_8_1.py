#Проверьте наличие значения 200 в sample_dict = {'a': 100, 'b': 200, 'c': 300}.

sample = {'a': 100, 'b':200, 'c':300}
for i, key in sample.items():
    if key == 200:
        print('norm')
