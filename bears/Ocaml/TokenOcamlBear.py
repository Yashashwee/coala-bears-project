from coalib.bears.LocalBear import LocalBear
from coalib.results.Result import Result
from coalib.results.HiddenResult import HiddenResult
from coalib.settings.Setting import language
from coalib.bearlib.languages.Language import Language
from lark import Lark
from lark import Transformer

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
exp: comment| let | match | var | fvar | bool | intarith|appf
// Allow optional punctuation after each word
word: WORD ["," | "!"]

// imports WORD from library
%import common.WORD   

// Disregard spaces in text
%ignore " "
%ignore "\n"   
   

""")
# try:
#     parsedTree = l.parse(
#         "let fun3 x y = let newX fun x in match newX with 10->20|1000->1000")
#     print(parsedTree.pretty())
# except:
#     print(failed)


class OtherBear(LocalBear):

    def run(self, filename, file, language: language = Language['Ocaml']):
        """

        HelperBear to return tokens for a file

        :param language: Programming language of the source code written.

        """
        data = ""

        for line_no, line in enumerate(file):
            data = data + line

        try:
            parsed_tree = l.parse(data)
            yield Result.from_values(origin=self,message='Following is parsed tree:\n {}'.format(parsed_tree.pretty()),file=filename)
        
        except:
            yield Result.from_values(origin=self,message='Cannot Parse the code',file=filename)


# from coalib.bears.LocalBear import LocalBear
# from coalib.results.Result import Result
# from coalib.resilts.HiddenResult import HiddenResult
# from coalib.settings.Setting import language
# from coalib.bearlib.languages.Language import Language


# class TokenOcamlBear(LocalBear):
#     LANGUAGES = {'Ocaml'}
#     AUTHORS = {'Yashashwee'}
#     CAN_DETECT = {'Syntax'}

#     def run(self, filename, file, mw: int = 80, language: language = Language['Ocaml']):

#         yield HiddenResult(self,[])
