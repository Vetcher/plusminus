import unittest
import expression_tree as et
import calc_operands as op
from math import *


class MyTestCase(unittest.TestCase):

    # test Expression tree and calc_operands
    def test_expression(self):
        values = list()
        values.append(et.ExpressionTree(5))
        values.append(et.ExpressionTree(3))
        tr = list()
        tr.append(et.ExpressionTree(op.add_, values[0], values[1]))
        tr.append(et.ExpressionTree(op.sub_, values[0], values[1]))
        tr.append(et.ExpressionTree(op.div_, values[0], values[1]))
        tr.append(et.ExpressionTree(op.mul_, values[0], values[1]))
        print(tr[0].calc(), tr[1].calc(), tr[2].calc(), tr[3].calc())
        tr.append(et.ExpressionTree(op.add_, tr[0], tr[1]))
        tr.append(et.ExpressionTree(op.sub_, tr[1], tr[0]))
        tr.append(et.ExpressionTree(op.div_, tr[0], tr[1]))
        tr.append(et.ExpressionTree(op.mul_, tr[0], tr[1]))
        print(tr[4].calc(), tr[5].calc(), tr[6].calc(), tr[7].calc())

    def test_parsing(self):

        result = et.make_expression_array('ln(5,3+(2-3))+sin(5,3)+5+5*3')
        tree = et.make_expression_tree(result)
        #print(tree.calc())

        result = et.make_expression_array('ln(5,3+(2-3))+sin(5,3)+5+5*3')
        tree = et.make_expression_tree(result)
        #print(tree.calc())

    def test_all(self):

        result = et.make_expression_array('2/ln(e^(1+log(10, 100)))*(6-2^2)*1/abs(6-3^2)*ln(e^(9*4))')
        tree = et.make_expression_tree(result)
        expression = 2/log(e**(1+log(100, 10)))*(6-2**2)*1/abs(6-3**2)*log(e**(9*4))
        self.assertEqual(tree.calc(), expression)

        result = et.make_expression_array('abs(5*2^2-5^2/(3^2-lg(10^4)))-6^2/4*lg(10)')
        tree = et.make_expression_tree(result)
        expression = abs(5*2**2-5**2/(3**2-log(10**4, 10)))-6**2/4*log(10, 10)
        self.assertEqual(tree.calc(), expression)

    def test_signs(self):
        result = et.make_expression_array('')
        tree = et.make_expression_tree(result)
        self.assertEqual(tree.calc(), None)

        result = et.make_expression_array('15+3')
        tree = et.make_expression_tree(result)
        self.assertEqual(tree.calc(), 15.0+3.0)

        result = et.make_expression_array('15-3')
        tree = et.make_expression_tree(result)
        self.assertEqual(tree.calc(), 15.0-3.0)

        result = et.make_expression_array('15*3')
        tree = et.make_expression_tree(result)
        self.assertEqual(tree.calc(), 15.0*3.0)

        result = et.make_expression_array('15/3')
        tree = et.make_expression_tree(result)
        self.assertEqual(tree.calc(), 15.0/3.0)

        result = et.make_expression_array('15^3')
        tree = et.make_expression_tree(result)
        self.assertEqual(tree.calc(), 15.0**3.0)

        result = et.make_expression_array('15^0.5')
        tree = et.make_expression_tree(result)
        print(tree.calc())
        self.assertEqual(tree.calc(), 15.0**0.5)

        result = et.make_expression_array('15/0.5')
        tree = et.make_expression_tree(result)
        self.assertEqual(tree.calc(), 15.0/0.5)

        result = et.make_expression_array('1/3')
        tree = et.make_expression_tree(result)
        self.assertEqual(tree.calc(), 1.0/3.0)

    def test_priority(self):
        result = et.make_expression_array('(15+3)*2')
        tree = et.make_expression_tree(result)
        self.assertEqual(tree.calc(), (15.0+3.0)*2.0)

    def test_functions(self):
        result = et.make_expression_array('abs(6-9)')
        tree = et.make_expression_tree(result)
        self.assertEqual(tree.calc(), abs(6-9))

        result = et.make_expression_array('ln(5)')
        tree = et.make_expression_tree(result)
        self.assertEqual(tree.calc(), log(5))

        result = et.make_expression_array('log(3, 5)')
        tree = et.make_expression_tree(result)
        self.assertEqual(tree.calc(), log(5, 3))

        result = et.make_expression_array('lg(15)')
        tree = et.make_expression_tree(result)
        self.assertEqual(tree.calc(), log(15, 10))

        result = et.make_expression_array('sin(15)')
        tree = et.make_expression_tree(result)
        self.assertEqual(tree.calc(), sin(15))

        result = et.make_expression_array('cos(15)')
        tree = et.make_expression_tree(result)
        self.assertEqual(tree.calc(), cos(15))

        result = et.make_expression_array('tg(15)')
        tree = et.make_expression_tree(result)
        self.assertEqual(tree.calc(), tan(15))

        result = et.make_expression_array('tan(15)')
        tree = et.make_expression_tree(result)
        self.assertEqual(tree.calc(), tan(15))

        result = et.make_expression_array('ctg(15)')
        tree = et.make_expression_tree(result)
        self.assertEqual(tree.calc(), 1.0 / tan(15))

        result = et.make_expression_array('ctan(15)')
        tree = et.make_expression_tree(result)
        self.assertEqual(tree.calc(), 1.0 / tan(15))

if __name__ == '__main__':
    unittest.main()
