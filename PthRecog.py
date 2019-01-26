KeyWords = ['print', 'var', 'end']


def Recog(line):
    kw = ''
    for char in range(len(line)):
        kw += line[char]
        if kw in KeyWords:
            return kw


def Args(line, separator):
    keyword = Recog(line)
    args = line.replace(keyword, '').lstrip().replace('(', '').replace(')', '')
    if separator != '':
        args = args.split(separator)
    return args
