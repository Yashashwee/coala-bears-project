import re
from coalib.bears.LocalBear import LocalBear
from coalib.results.Result import Result
from coalib.settings.Setting import language
from coalib.bearlib.languages.Language import Language

class DependencyBear(LocalBear):
    LANGUAGES={'Ocaml'}
    AUTHORS={'VYD'}
    AUTHORS_EMAILS={'avatsal38@gmail.com'}
    MAINTAINERS={'VYD'}
    MAINTAINERS_EMAILS = {'avatsal38@gmail.com'}
    CAN_DETECT={'Extra string operations'}

    def run(self,filename,file,language: language=Language['Ocaml']):

        """
        
        Give result for undeclared function of lists.

        :param language: Programming language of the source code written.

        """
        flag=0
        regExpfun = r"(let)(\s)([a-zA-Z]+)"
        regoriginal = [r"[^\.]*(length)", r"[^\.]*(compare_lengths)", 
        r"[^\.]*(cons)", r"[^\.]*(compare_length_with)", 
        r"[^\.]*(hd)", r"[^\.]*(tl)", 
        r"[^\.]*(nth)", r"[^\.]*(nth_opt)", 
        r"[^\.]*(rev)", r"[^\.]*(init)", 
        r"[^\.]*(append)", r"[^\.]*(rev_append)",
        r"[^\.]*(concat)", r"[^\.]*(flatten)",
        r"[^\.]*(equal)", r"[^\.]*(map)",
        r"[^\.]*(fold_left)", r"[^\.]*(fold_right)",
        r"[^\.]*(map2)", r"[^\.]*(fold_left2)",
        r"[^\.]*(filter)", r"[^\.]*(fold_right2)"]


        # iterating on all the lines in the ocaml src code file 
        res = []
        errors = []
        final = ""
        for line_no,line in enumerate(file):

            # print("line_no = ",line_no)
            # print("line = ",line)

            fun_matched = re.findall(regExpfun,line)

            # print("fun_matched = ", fun_matched)
            l = len(fun_matched)
            for j in range(l):
                res.append(list(fun_matched[j])[2])

            # print("res = ", res)
            for i in regoriginal:
                x = re.findall(i,line)
                if(not(len(x)==0)):
                    errors.append(x[0])

            # print("errors = ",errors)

            # if the line is a single line comment
            length =len(errors)

            if length > 0:
                flag=1
                l = length

                final = ""
                for i in errors:
                    if i not in res:
                        final = final + " " + i 

        if not (final ==""):
            yield Result.from_values(origin=self,message='Wrong call of function'+'({current})'.format(current=final),
            file=filename)

        else:
            yield Result.from_values(origin=self,message='Everything Good!',file=filename)



        if flag==0:
            yield Result.from_values(origin=self,message='Everything Good',file=filename)
                    

