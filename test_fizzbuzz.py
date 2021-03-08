import unittest
import fizzbuzz
#for capturing output
import io
import sys

#multiples of 3 print Fizz, multiples of 5 print Buzz, both, print FizzBuzz
class TestCase(unittest.TestCase):
    def test_correct(self):
        #long string for comparing function to output, adding 12 lines at a time, manually evaluated
        correctOutput = "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n"
        correctOutput += "13\n14\nFizzBuzz\n16\n17\nFizz\n19\nBuzz\nFizz\n22\n23\nFizz\n"
        correctOutput += "Buzz\n26\nFizz\n28\n29\nFizzBuzz\n31\n32\nFizz\n34\nBuzz\nFizz\n"
        correctOutput += "37\n38\nFizz\nBuzz\n41\nFizz\n43\n44\nFizzBuzz\n46\n47\nFizz\n"
        correctOutput += "49\nBuzz\nFizz\n52\n53\nFizz\nBuzz\n56\nFizz\n58\n59\nFizzBuzz\n"
        correctOutput += "61\n62\nFizz\n64\nBuzz\nFizz\n67\n68\nFizz\nBuzz\n71\nFizz\n"
        correctOutput += "73\n74\nFizzBuzz\n76\n77\nFizz\n79\nBuzz\nFizz\n82\n83\nFizz\n"
        correctOutput += "Buzz\n86\nFizz\n88\n89\nFizzBuzz\n91\n92\nFizz\n94\nBuzz\nFizz\n"
        correctOutput += "97\n98\nFizz\nBuzz\n"

        #code from https://stackoverflow.com/questions/33767627/python-write-unittest-for-console-print
        #to capture stdout
        capturedOutput = io.StringIO()          # Create StringIO object
        sys.stdout = capturedOutput                   #  and redirect stdout.
        fizzbuzz.printFizzBuzz()                              # Call unchanged function.
        sys.stdout = sys.__stdout__
        self.assertEqual(correctOutput, capturedOutput.getValue())
            
if __name__ == '__main__':
    unittest.main(verbosity=2)