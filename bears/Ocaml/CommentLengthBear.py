from coalib.bears.LocalBear import LocalBear
from coalib.results.Result import Result
from coalib.settings.Setting import language
from coalib.bearlib.languages.Language import Language


class comment_length_checker(LocalBear):
    LANGUAGES = {'Ocaml'}
    AUTHORS = {'VYD'}
    AUTHORS_EMAILS = {'avatsal38@gmail.com'}
    MAINTAINERS = {'Vatsal'}
    MAINTAINERS_EMAILS = {'avatsal38@gmail.com'}
    CAN_DETECT = {}

    def run(self, filename, file, mw: int = 80, language: language = Language['Ocaml']):
        """

        Give result for comments longer than max width that is 80.

        :param mw: Denotes the maximum width a comment can have.
        :param language: Programming language of the source code written.

        """

        if 'mw' in language.attributes:
            mw = language.mw
        for comment_no, comment in enumerate(file):
            if comment[0] == '(' and comment[1] == '*':
                length = len(comment)
                if length-1 > mw+4:
                    yield Result.from_values(origin=self, message='comment size is greater than 80'+'({current}>{allowed})'
                                             .format(current=len(comment)-5, allowed=mw),
                                             file=filename, line=comment_no+1, column=mw+1, end_line=comment_no+1, end_column=len(comment)
                                             )
