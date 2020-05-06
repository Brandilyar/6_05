def count_words(filename):
    """ Считает количество строк в файле"""
    try:
        with open(filename, encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        # pass
        print(f"неверное имя файла  {filename}")
    else:
        words = content.split()
        num_words = len(words)
        print(f" В этом  {filename}  около {num_words} слов")


filenames = ['prestuplenie-i-nakaznia.txt', 'voyna-i-mir.txt',
             'evgini-onegin.txt']
for file in filenames:
    count_words(file)
