from coalib.bears.LocalBear import LocalBear
from coalib.results.Result import Result
from coalib.results.HiddenResult import HiddenResult
from coalib.settings.Setting import language
from coalib.bearlib.languages.Language import Language
from lark import Lark


class OtherBear(LocalBear):

    def run(self, filename, file, language: language = Language['Ocaml']):
        """

        HelperBear to return tokens for a file

        :param language: Programming language of the source code written.

        """
        yield HiddenResult(self, ["Some Content", "Some Other Content"])


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
