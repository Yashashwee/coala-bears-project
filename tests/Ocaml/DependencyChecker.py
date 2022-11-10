import unittest
import fileinput
import re

def run(file):

    """
    
    Give result for undeclared function of lists.

    :param language: Programming language of the source code written.

    """
    flag=0
    check1 = 0
    check2 = 0
    regExpfun = r"(let)(\s)([a-zA-Z]+)"
    regExp2Fun = r"(\.)([^\n\s]+)"
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
        extra_matched = re.findall(regExp2Fun,line)

        # print("fun_matched = ", fun_matched)
        l = len(fun_matched)
        for j in range(l):
            res.append(list(fun_matched[j])[2])

        for k in range(len(extra_matched)):
            res.append(list(extra_matched[k])[1])

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
        check1 = 1

    else:
        check2 = 1



    if flag==0:
        check2 = 1

    return check1,check2
class test_StringRepCheckerBear(unittest.TestCase):
	
	def test_file1(self):
		fininput=fileinput.FileInput('files/file23.ml')
		check1,check2=run(fininput)
		self.assertEqual(check1,0)
		self.assertEqual(check2,1)

	def test_file2(self):
		fininput=fileinput.FileInput('files/file24.ml')
		check1,check2=run(fininput)
		self.assertEqual(check1,1)
		self.assertEqual(check2,0)


# added this condition so that this only runs if this file is run directly and not imported 
if __name__ == "__main__":
	var=unittest.TestLoader().loadTestsFromTestCase(test_StringRepCheckerBear)
	unittest.TextTestRunner(verbosity=2).run(var)



