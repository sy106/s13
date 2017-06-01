__author__ = "Alex Li"

import sys,os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(sys.path)
from day5 import package_test

package_test.test1.test()