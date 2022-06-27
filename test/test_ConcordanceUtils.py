import sys
import unittest
import io

from generate_concordance import ConcordanceUtils


class TestConcordanceUtils(unittest.TestCase):

    def test_get_input_file(self):
        stdout: io.StringIO = io.StringIO()
        sys.stdout = stdout

        # Since an Inaccessible file cannot be indexed by git, so avoid the inaccessible test case since
        #   it can't be reproduced properly across all users.
        self.assertFalse(ConcordanceUtils.get_input_file_text(input_file="/this_file_should_not_exist.txt"))

        self.assertEqual("This is a simple test.\nA two sentence test.",
                         ConcordanceUtils.get_input_file_text("./test_files/SimpleTest.txt"))

        # Reset stdout redirect
        sys.stdout = sys.__stdout__

        self.assertTrue("The provided input file -- /this_file_should_not_exist.txt -- does not exist."
                        in stdout.getvalue())

    def test_print_lines(self):
        stdout: io.StringIO = io.StringIO()
        sys.stdout = stdout

        ConcordanceUtils.print_lines(lines=list(["This is a test.", "A second sentence."]))

        # Reset stdout redirect
        sys.stdout = sys.__stdout__

        self.assertTrue("This is a test.\nA second sentence." in stdout.getvalue())

    def test_write_lines_to_file(self):
        stdout: io.StringIO = io.StringIO()
        sys.stdout = stdout

        # Since an Inaccessible file cannot be indexed by git, so avoid the inaccessible test case since
        #   it can't be reproduced properly across all users.
        self.assertFalse(ConcordanceUtils.write_lines_to_file(lines=list("Testing"), output_file="/tmp/"))

        # Reset stdout redirect
        sys.stdout = sys.__stdout__

        ConcordanceUtils.write_lines_to_file(lines=list(["Testing", "Testing"]),
                                             output_file="./test_files/TestWriteFile.txt")


if __name__ == '__main__':
    unittest.main()