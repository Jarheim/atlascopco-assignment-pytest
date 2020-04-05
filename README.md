#Instructions to run tests with code coverage
pip install -r requirements.txt
coverage run -m pytest
coverage report (to report on the results)

#Instructions for assignment
Your team has written a small utility package that will be used around the organization. Your task is to pick two of the 
methods in that package and write unit tests for them. The methods may or may not contains bugs. 

Along with this document you have received a folder containing the code to test. It exposes a class called VariousMethods.

##The task 
Create a unit test in python and import the provided package. Don’t put the unit test code in the same folder as the code. 
Pick two of the above methods and write as many test cases as you think is necessary to test them. Make a note of any bugs 
you may find in a separate .txt file and return the entire solution.

##Methods choosen
ConvertToAtlasCopcoString(self, toConvert):
ReverseString(self, toReverse):

#Stack choosen
Python3, pytest
