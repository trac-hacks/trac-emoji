import unittest
from minimocktest import MockTestCase
from trac.core import ComponentManager 
from trac_emoji import TracEmoji
import re

class TestTracEmoji(MockTestCase):

    def setUp(self):
        compmgr = ComponentManager() 
        self.e = TracEmoji(compmgr)
        super(self.__class__, self).setUp()

    def test_TracEmoji_wikiSyntaxWorks(self):
        tests = [':+1:', ':boom:']
        for test in tests:
            for r,c in self.e.get_wiki_syntax():
                rr = re.compile(r)
                if rr.match(test):
                    break
            else:
                self.fail('%s not matched' %(test))

if __name__ == '__main__':
    unittest.main()
