from coalib.bears.LocalBear import LocalBear
from coalib.results.Result import Result
from coalib.settings.Setting import language
from coalib.bearlib.languages.Language import Language

class comment_length_checker(LocalBear):
    LANGUAGES={'Ocaml'}
    AUTHORS={'VYD'}
    AUTHORS_EMAILS={'avatsal38@gmail.com'}
    MAINTAINERS={'VYD'}
    MAINTAINERS_EMAILS = {'avatsal38@gmail.com'}
    CAN_DETECT={}

    def run(self,filename,file,mw: int=80,language: language=Language['Ocaml']):

        """
        
        Give result for comments longer than max width that is 80.

        :param mw: Denotes the maximum width a comment can have.
        :param language: Programming language of the source code written.

        """
        flag=0

        # setting value of max width allowed in mw variable 
        if 'mw' in language.attributes:
            mw=language.mw

        # iterating on all the lines in the ocaml src code file 
        for comment_no,comment in enumerate(file):
            
            # if the line is a single line comment
            temp=len(comment)
            if comment[0]=='(' and comment[1]=='*' and comment[temp-2]==')' and comment[temp-3]=='*':
                length=len(comment)
                if length-1>mw+6:
                    flag=1
                    yield Result.from_values(origin=self,message='comment size is greater than 80'+'({current}>{allowed})'
                        .format(current=len(comment)-7,allowed=mw),
                    file=filename,line=comment_no+1,column=mw+1,end_line=comment_no+1,end_column=len(comment)
                    )
            
            # multiline comment
            elif comment[0]=='(' and comment[1]=='*':
                length3=len(comment)
                if length3-1>mw+3:
                    flag=1
                    yield Result.from_values(origin=self,message='comment size is greater than 80'+'({current}>{allowed})'
                        .format(current=len(comment)-4,allowed=mw),
                    file=filename,line=comment_no+1,column=mw+1,end_line=comment_no+1,end_column=len(comment)
                    )
            
            elif comment[1]=='*':
                if comment[2]==')':
                    continue
                else:
                    length2=len(comment)
                    if length2-1>mw+3:
                        flag=1
                        yield Result.from_values(origin=self,message='comment size is greater than 80'+'({current}>{allowed})'
                            .format(current=len(comment)-4,allowed=mw),
                        file=filename,line=comment_no+1,column=mw+1,end_line=comment_no+1,end_column=len(comment)
                        )

            # comment not there 
            else:
                continue

        # if all the comments are of acceptable
        if flag==0:
            yield Result.from_values(origin=self,message='All the comments have acceptable width',file=filename)
                    

