import fileinput
from lark import Lark
import unittest

l = Lark(r"""?start: (exp ["\n"]*)+				

DIGIT: "0".."9"
HEXDIGIT: "a".."f"|"A".."F"|DIGIT
CAPITAL: ["A".."Z"]+
case: exp | exp "->" exp
match:"match" var ["," var]* "with" case ["|" case]+
INT: DIGIT+
comment:"(*" word+ "*)"
inkey:"in"
let:"let" [rec] fvar var* "=" exp+ [inkey|";;"]
var: /[a-z][a-zA-Z0-9]*/
fvar: /[a-z][a-zA-Z0-9]*/
bool: "true"|"false"
rec: "rec"
add: "+"
times: "*"
div: "/"
minus: "-"
operators: add | times | div | minus
binop: var operators var | var operators INT | INT operators var | INT operators INT
intarith: binop | binop operators binop | INT
err: CAPITAL
raise: "raise" err
appf: fvar var+
exp: comment| let | match | var | fvar | bool | intarith | appf
// Allow optional punctuation after each word
word: WORD ["," | "!"]

// imports WORD from library
%import common.WORD   

// Disregard spaces in text
%ignore " "
%ignore "\n"
%ignore "\t"   
   

""")


def toToken(file):
    f = l.parse(file)

    return f.pretty()


class test_TokenBear(unittest.TestCase):

    def test_file1(self):
        # fininput = fileinput.FileInput('files/treeCheck1.ml')
        file1 = ""
        file2 = ""
        with open("files/treeCheck1.ml", "r") as f1, open("files/out1.txt", "r") as f2:
            file1 = f1.read()
            file2 = f2.read()
        check = toToken(file1)
        self.assertEqual(check, file2)

    def test_file2(self):
        file1 = ""
        file2 = ""
        with open("files/treeCheck2.ml", "r") as f1, open("files/out2.txt", "r") as f2:
            file1 = f1.read()
            file2 = f2.read()
        check = toToken(file1)
        self.assertEqual(check, file2)


# added this condition so that this only runs if this file is run directly and not imported
if __name__ == "__main__":
    var = unittest.TestLoader().loadTestsFromTestCase(test_TokenBear)
    unittest.TextTestRunner(verbosity=2).run(var)
