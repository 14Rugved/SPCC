import re 

keywords = {"int", "float", "if", "else", "while", "for","char", "double","include"}
operators = {"+", "-", "*", "/", "%", "=", "==", "!=", "<", ">", "<=", ">=", "&&", "||", "++", "--"}
punctuations = {",", ";", "(", ")", "{", "}", "[", "]"}

def lexical_analyzer(code):
	#splitting the code into tokens
	tokens = re.findall(r'\w+|\S', code)
	
	header = []
	found_keywords = []
	found_operators = []
	found_punctuations = []
	found_identifiers = []
	found_constants = []

	for token in tokens:
		if token in keywords:
			found_keywords.append(token)
		elif re.match(r'\d+', token):
			found_constants.append(token)
		elif token in operators:
			found_operators.append(token)
		elif token in punctuations :
			found_punctuations.append(token)
		#for header files
		elif re.match(r'#\s*include\s*<[\w.]+>', token):
    			headers.append(token)  # It's a header file like <stdio.h>
		elif re.match(r'[a-zA-Z_]\w*', token):
    			found_identifiers.append(token)
	
	print("header files : ", header)
	print("keywords : ", found_keywords)
	print("operators : ", found_operators)
	print("punctuation marks : ", found_punctuations)
	print("constants : ", found_constants)
	print("identifiers : ", found_identifiers)

	#sample c code
code = """
	#include<math.h>
	double power(double base, int exp){
		double result = 1.0;
		while(exp>0){
			result = result*base;
			exp --;}
		return result;} """
print("Input Program")
print(code)
print("\nLEXICAL ANALYZER :\n")
lexical_analyzer(code)


	
	