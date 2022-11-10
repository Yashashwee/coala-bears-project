import re
from coalib.bears.LocalBear import LocalBear
from coalib.results.Result import Result
from coalib.settings.Setting import language
from coalib.bearlib.languages.Language import Language

class StringRepChecker(LocalBear):
    LANGUAGES={'Ocaml'}
    AUTHORS={'VYD'}
    AUTHORS_EMAILS={'avatsal38@gmail.com'}
    MAINTAINERS={'VYD'}
    MAINTAINERS_EMAILS = {'avatsal38@gmail.com'}
    CAN_DETECT={'Extra string operations'}

    def run(self,filename,file,language: language=Language['Ocaml']):

        """
        
        Give result for comments longer than max width that is 80.

        :param mw: Denotes the maximum width a comment can have.
        :param language: Programming language of the source code written.

        """
        flag=0
        regExp = r"(\"[^n]+\"[^\n]+)(\^)([^\n]+\"[^\n]+\")"


        # iterating on all the lines in the ocaml src code file 
        for line_no,line in enumerate(file):

            matched = re.findall(regExp,line)

            # if the line is a single line comment
            length =len(matched)

            if length > 0:
                flag=1
                l = length
                res = []
                for j in range(l):
                    res.append(list(matched[j]))
                st = "("
                for x in range(l-1):
                    st = st + ",".join(res[x]) + "), ("
                st = st + ",".join(res[l-1]) +")."

                yield Result.from_values(origin=self,message='Strings badly represented on line_number {num}'.format(num = line_no)+'({current})'.format(current=st),
                    file=filename
                )

        if flag==0:
            yield Result.from_values(origin=self,message='All the strings are accepted in',file=filename)
                    

