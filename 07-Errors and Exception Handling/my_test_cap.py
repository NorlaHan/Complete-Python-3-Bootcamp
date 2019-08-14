import unittest
import cap

class TestCap(unittest.TestCase):

	def test_1_single_world(self):
		text='python'
		result=cap.cap_text(text)
		self.assertEqual(result,'Python')

	def test_2_two_words(self):
		text='monty python'
		result=cap.cap_text(text)
		self.assertEqual(result,'Monty Python')

	def test_3_words_with_comma(self):
		text="jack's monty python story"
		result=cap.cap_text(text)
		self.assertEqual(result,"Jack's Monty Python Story")

if __name__=="__main__":
	unittest.main()
