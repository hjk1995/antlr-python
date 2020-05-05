import os
from file_grammar import FileGrammer

def format_tree(tree_string):
    indent_size = 3
    add_indent = ' ' * indent_size
    formatted_string = tree_string[0]
    indent = ''
    for i in range(1, len(tree_string)):
        if tree_string[i] == '(' and tree_string[i + 1] != ' ':
            indent += add_indent
            formatted_string += "\n" + indent + '('
        elif tree_string[i] == ')':
            formatted_string += ')'
            if len(indent) > 0:
                indent = indent.replace(add_indent, '', 1)
        else:
            formatted_string += tree_string[i]
    return formatted_string


fileGrammar = FileGrammer()
filename = input()
fileG = fileGrammar.executeFile(os.path.splitext(filename)[1][1::], open(filename, 'r').read())
tree = fileG['tree']
parser = fileG['parser']
lisp_tree_str = tree.toStringTree(recog=parser)
print(format_tree(lisp_tree_str))