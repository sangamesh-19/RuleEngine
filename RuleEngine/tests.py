import unittest
from rule_engine import RuleEngine  # This should match your class definition

class TestRuleEngine(unittest.TestCase):
    def setUp(self):
        self.engine = RuleEngine()  # Initialize your RuleEngine here

    def test_add_rule(self):
        result = self.engine.add_rule("age > 18")  # Example rule
        self.assertIsNotNone(result)

    def test_evaluate(self):
        self.engine.add_rule("age > 18")
        result = self.engine.evaluate({"age": 20})  # Example input
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
