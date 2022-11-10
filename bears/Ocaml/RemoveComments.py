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
    return False, -1


def commentEndInLine(line):
    for i in range(len(line)-1):
        if line[i] == "*" and line[i+1] == ")":
            return True, i
    return False, -1


class RemoveComments(LocalBear):
    def run(self, filename, file, language: language = Language['Ocaml']):

        newFile = []
        # print(file)
        flag = False
        for line in file:
            if not flag:
                booStart, indStart = commentStartInLine(line)
                booEnd, indEnd = commentEndInLine(line)
                if booStart and not booEnd:
                    flag = True
                elif booStart and booEnd:
                    flag = False
                else:
                    newFile.append(line)
            else:
                boo, ind = commentEndInLine(line)
                if boo:
                    flag = False
        # print(newFile)

        yield HiddenResult(self, [newFile])
