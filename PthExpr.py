import PthVar as Var


def Expr(line):
    words = line.split(' ')
    for w in range(words.__len__()):
        if '[' in words[w] and ']' in words[w]:
            expr = words[w][words[w].find('[') + 1:words[w].find(']')]
            if expr in Var.Vars:
                value = Var.getVar(expr)
            words[w] = words[w].replace('[{}]'.format(expr), value)
    return ' '.join(words)
