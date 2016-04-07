from template import CodeBuilder, Template

__author__ = 'weiqisong'

import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)
    # def test_code_builder(self):
    #     code = CodeBuilder()
    #     code.add_line("test")
    #     code2 = code.add_section()
    #     code.add_line("test1")
    #     code2.add_line("end")
    #     print(str(code))

    def test_code_generate(self):
        template = Template("abadfdfd{{df}}dfdsf")
        print(template.test_code())





if __name__ == '__main__':
    unittest.main()
