from coalib.bears.LocalBear import LocalBear
from coalib.results.Result import Result
from coalib.results.HiddenResult import HiddenResult
from coalib.settings.Setting import language
from coalib.bearlib.languages.Language import Language
from coalib.results.RESULT_SEVERITY import RESULT_SEVERITY


def commentStartInLine(line):
    for i in range(len(line)-1):
        if line[i] == "(" and line[i+1] == "*":
            return True, i


def commentEndInLine(line):
    for i in range(len(line)-1):
        if line[i] == "*" and line[i+1] == ")":
            return True, i


class RemoveComments(LocalBear):
    def run(self, filename, file, language: language = Language['Ocaml']):
        newFile = []
        flag = False
        for line in file:
            if flag:
                boo, ind = commentStartInLine(line)
                if boo:
                    flag = True
                else:
                    newFile.append(line)
            else:
                boo, ind = commentEndInLine(line)
                if boo:
                    flag = False

        yield HiddenResult(self, [newFile])
