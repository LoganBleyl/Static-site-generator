import unittest
from main import extract_title

class TestMain(unittest.TestCase):
        # extract title tests

    def test_extract_title(self):
        title = "# Tolkien Fan Club"
        extracted_title = extract_title(title)

        expected = "Tolkien Fan Club"
        self.assertEqual(extracted_title, expected)


    def test_extract_title2(self):
        title = "Tolkien Fan club"

        with self.assertRaises(Exception):
            extract_title(title)

    if __name__ == "__main__":
            unittest.main()
