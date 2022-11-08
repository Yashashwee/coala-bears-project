import unittest
import fileinput

def run(file):

	flag=0
	check=0
	test1=0
	test2=0
	test3=0

	# iterating on all the lines in the ocaml src code file 
	for comment_no,comment in enumerate(file):
			
		# if the line is a single line comment
		temp=len(comment)
		if comment[0]=='(' and comment[1]=='*' and comment[temp-2]==')' and comment[temp-3]=='*':
			if comment[2]==' ' and comment[temp-4]==' ':
				continue
			else:
				check=1
				test1=1
		   
		# multiline comment
		elif comment[0]=='(' and comment[1]=='*':
			flag=1
			continue
			
		elif flag==1:
			if comment[0]==' ' and comment[1]=='*' and comment[2]==')':
				flag=0
				continue
			elif comment[0]==' ' and comment[1]=='*' and comment[2]==' ':
				continue
			else:
				check=1
				test2=1

		# comment not there 
		else:
			continue

	# if all the comments are of acceptable
	if check==0:
		test3=1
	return test1,test2,test3

class test_CommentFormatCheckerBear(unittest.TestCase):
	
	def test_file1(self):
		fininput=fileinput.FileInput('files/file11.ml')
		test1,test2,test3=run(fininput)
		self.assertEqual(test1,1)
		self.assertEqual(test2,0)
		self.assertEqual(test3,0)

	def test_file2(self):
		fininput=fileinput.FileInput('files/file12.ml')
		test1,test2,test3=run(fininput)
		self.assertEqual(test1,0)
		self.assertEqual(test2,1)
		self.assertEqual(test3,0)

	def test_file3(self):
		fininput=fileinput.FileInput('files/file13.ml')
		test1,test2,test3=run(fininput)
		self.assertEqual(test1,0)
		self.assertEqual(test2,0)
		self.assertEqual(test3,1)

	def test_file4(self):
		fininput=fileinput.FileInput('files/file14.ml')
		test1,test2,test3=run(fininput)
		self.assertEqual(test1,1)
		self.assertEqual(test2,1)
		self.assertEqual(test3,0)

# added this condition so that this only runs if this file is run directly and not imported 
if __name__ == "__main__":
	var=unittest.TestLoader().loadTestsFromTestCase(test_CommentFormatCheckerBear)
	unittest.TextTestRunner(verbosity=2).run(var)

