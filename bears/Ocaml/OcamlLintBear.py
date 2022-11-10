import json

from coalib.bearlib.abstractions.Linter import linter
from dependency_management.requirements.AnyOneOfRequirements import (
    AnyOneOfRequirements)
from dependency_management.requirements.DistributionRequirement import (
    DistributionRequirement)
from coalib.results.Diff import Diff
from coalib.results.Result import Result
from coalib.results.RESULT_SEVERITY import RESULT_SEVERITY


@linter(executable='opam lint')
class OcamlLintBear:
    """
    Check Ocaml code for possible problems. This bear can propose patches for
    using alternative functions, simplifying code and removing redundancies.

    See <https://opam.ocaml.org/doc/man/opam-lint.html> for more
    information.
    """

    LANGUAGES = {'Ocaml'}
    REQUIREMENTS = {
        AnyOneOfRequirements(
            [
                DistributionRequirement(apt_get='opam'),
            ],
        ),
    }
    AUTHORS = {'Dhananjay Kumar Jha'}
    AUTHORS_EMAILS = {'coala-devel@googlegroups.com'}
    LICENSE = 'AGPL-3.0'
    CAN_DETECT = {'Duplication'}
    CAN_FIX = {'Unused Code', 'Code Simplification'}

    severity_map = {'Error': RESULT_SEVERITY.MAJOR,
                    'Warning': RESULT_SEVERITY.NORMAL,
                    'Suggestion': RESULT_SEVERITY.INFO}

    @staticmethod
    def create_arguments(filename, file, config_file):
        return '--json', filename

    def process_output(self, output, filename, file):
        output = json.loads(output)

        for issue in output:
            diff = Diff(file)
            from_lines = issue['from'].splitlines()
            to_lines = issue['to'].splitlines()
            assert len(from_lines) == len(to_lines)
            for other_lines in range(1, len(from_lines)):
                assert from_lines[other_lines] == to_lines[other_lines]
            line_nr = issue['startLine']
            line_to_change = file[line_nr-1]
            newline = line_to_change.replace(from_lines[0], to_lines[0])
            diff.change_line(line_nr, line_to_change, newline)

            yield Result.from_values(
                origin=self,
                message=issue['hint'],
                file=filename,
                severity=self.severity_map[issue['severity']],
                line=issue['startLine'],
                column=issue['startColumn'],
                end_line=issue['endLine'],
                end_column=issue['endColumn'],
                diffs={filename: diff})
