import unittest
import fileinput
import re
def run(file):

	flag=0
	check1=0
	check2=0
	regExp = r"(\"[^n]+\"[^\n]+)(\^)([^\n]+\"[^\n]+\")"

	for line_no,line in enumerate(file):

		matched = re.findall(regExp,line)

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
			check1=1;

	if flag==0:
		check2=1

	return check1,check2

class test_StringRepCheckerBear(unittest.TestCase):
	
	def test_file1(self):
		fininput=fileinput.FileInput('files/file21.ml')
		check1,check2=run(fininput)
		self.assertEqual(check1,1)
		self.assertEqual(check2,0)

	def test_file2(self):
		fininput=fileinput.FileInput('files/file22.ml')
		check1,check2=run(fininput)
		self.assertEqual(check1,0)
		self.assertEqual(check2,1)


# added this condition so that this only runs if this file is run directly and not imported 
if __name__ == "__main__":
	var=unittest.TestLoader().loadTestsFromTestCase(test_StringRepCheckerBear)
	unittest.TextTestRunner(verbosity=2).run(var)



