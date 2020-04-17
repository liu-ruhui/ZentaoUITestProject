import os,time
import unittest
import HTMLTestRunner

current = os.path.dirname(__file__)
report_path = os.path.join(current,'report')

case_path = os.path.join(current,'test_cases')
html_path = os.path.join(report_path,'report_%s.html'%time.strftime('%Y-%m-%d-%H-%M-%S'))

discover = unittest.defaultTestLoader.discover(start_dir=case_path,
                                               pattern='*_case.py',
                                               top_level_dir=case_path)
main_suite = unittest.TestSuite()
main_suite.addTest(discover)

file = open(html_path,'wb')
html_runner = HTMLTestRunner.HTMLTestRunner(stream=file,
                                            title='禅道UI自动化测试项目',
                                            description='由自动化测试完成，包含大部分功能')
html_runner.run(main_suite)
