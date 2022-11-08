import unittest
import fileinput

def run(file):

	flag=0
	check1=0
	check2=0
	check3=0
	check4=0

	for comment_no,comment in enumerate(file):
					
		mw=80
		temp=len(comment)
		if temp<=1:
			continue
		if comment[0]=='(' and comment[1]=='*' and comment[temp-2]==')' and comment[temp-3]=='*':
			length=len(comment)
			if length-1>mw+6:
				flag=1
				check1=1
								
		elif comment[0]=='(' and comment[1]=='*':
			length3=len(comment)
			if length3-1>mw+3:
				flag=1
				check2=1
												
		elif comment[1]=='*':
			if comment[2]==')':
				continue
			else:
				length2=len(comment)
				if length2-1>mw+3:
					flag=1
					check3=1
								
		else:
			continue

	if flag==0:
		check4=1
	return check1,check2,check3,check4

class test_CommentLengthCheckerBear(unittest.TestCase):
	
	def test_file1(self):
		fininput=fileinput.FileInput('files/file1.ml')
		check1,check2,check3,check4=run(fininput)
		self.assertEqual(check1,1)
		self.assertEqual(check2,0)
		self.assertEqual(check3,0)
		self.assertEqual(check4,0)

	def test_file2(self):
		fininput=fileinput.FileInput('files/file2.ml')
		check1,check2,check3,check4=run(fininput)
		self.assertEqual(check1,0)
		self.assertEqual(check2,0)
		self.assertEqual(check3,0)
		self.assertEqual(check4,1)

	def test_file3(self):
		fininput=fileinput.FileInput('files/file3.ml')
		check1,check2,check3,check4=run(fininput)
		self.assertEqual(check1,0)
		self.assertEqual(check2,0)
		self.assertEqual(check3,1)
		self.assertEqual(check4,0)

	def test_file4(self):
		fininput=fileinput.FileInput('files/file4.ml')
		check1,check2,check3,check4=run(fininput)
		self.assertEqual(check1,1)
		self.assertEqual(check2,1)
		self.assertEqual(check3,1)
		self.assertEqual(check4,0)

	def test_file5(self):
		fininput=fileinput.FileInput('files/file5.ml')
		check1,check2,check3,check4=run(fininput)
		self.assertEqual(check1,0)
		self.assertEqual(check2,0)
		self.assertEqual(check3,0)
		self.assertEqual(check4,1)

	def test_file6(self):
		fininput=fileinput.FileInput('files/file6.ml')
		check1,check2,check3,check4=run(fininput)
		self.assertEqual(check1,0)
		self.assertEqual(check2,1)
		self.assertEqual(check3,0)
		self.assertEqual(check4,0)


# added this condition so that this only runs if this file is run directly and not imported 
if __name__ == "__main__":
	var=unittest.TestLoader().loadTestsFromTestCase(test_CommentLengthCheckerBear)
	unittest.TextTestRunner(verbosity=2).run(var)

