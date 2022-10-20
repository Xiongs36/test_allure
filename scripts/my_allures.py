import os
import sys
import allure
import pytest

class MyAllures():
    @allure.step('测试第一步1,True')
    def test_01(self):
        allure.attach('描述','断言成功')
        assert True

    @allure.step('测试第二步1，False')
    @allure.testcase('http://www.baidu.com')
    @allure.issue('http://www.baidu.com')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_02(self):
        assert False
    def test_03(self):
        assert True
    @allure.step(title='步骤4')
    def test_04(self):
        assert True
# if __name__ == '__main__':
#     pytest.main()
#     os.system("allure generate --clean ./temp -o ./report/")