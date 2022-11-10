from coalib.bears.LocalBear import LocalBear
from coalib.results.Result import Result
from coalib.settings.Setting import language
from coalib.bearlib.languages.Language import Language

class CommentFormatBear(LocalBear):
	LANGUAGES={'Ocaml'}
	AUTHORS={'VYD'}
	AUTHORS_EMAILS={'avatsal38@gmail.com'}
	MAINTAINERS={'VYD'}
	MAINTAINERS_EMAILS = {'avatsal38@gmail.com'}
	CAN_DETECT={}

	def run(self,filename,file,language: language=Language['Ocaml']):

		"""
		
		Give result for multiline not following the standard style
		:param language: Programming language of the source code written.

		"""
		flag=0
		check=0

		# iterating on all the lines in the ocaml src code file 
		for comment_no,comment in enumerate(file):
			
			# if the line is a single line comment
			temp=len(comment)
			if comment[0]=='(' and comment[1]=='*' and comment[temp-2]==')' and comment[temp-3]=='*':
				if comment[2]==' ' and comment[temp-4]==' ':
					continue
				else:
					check=1
					yield Result.from_values(origin=self,message='incorrect format of singleline comment on line number ' 
						+ '{length}'.format(length=comment_no+1) + ' -> ' + '{comp}'.format(comp=comment),file=filename)
		   
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
					yield Result.from_values(origin=self,message='incorrect format of multiline comment on line number ' 
						+ '{length}'.format(length=comment_no+1) + ' -> ' + '{comp}'.format(comp=comment),file=filename)

			# comment not there 
			else:
				continue

		# if all the comments are of acceptable
		if check==0:
			yield Result.from_values(origin=self,message='All the comments have correct formatting',file=filename)
