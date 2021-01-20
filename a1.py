import unittest

rank ='23456789TJQKA'
suit = 'cdhs'

def evaluate(hand):
    for i in hand: 
        for j in hand:
            if i in rank and hand.count(i)== 4: 
                return('Four of a kind')  
                break       
            elif i in rank and hand.count(i) == 2:
                if j in rank and hand.count(j)== 3:
                    return('Full house')      
                    break    
            elif j in suit and hand.count(j) == 5:
                return('Flush')
                break
            elif j in rank and hand.count(j) == 3:
                return('Three of a kind')
                break
            elif j in rank and hand.count(j) == 2:
                return('Pair')
                break
        else:
            for k in rank[::-1]:
                for a in hand:
                    if a == k:
                        return a + ' high'
        break
    
print('Qs7s2s4s5s:')
print(evaluate('Qs7s2s4s5s')) 
print('7h8hKsTs8s:')
print(evaluate('7h8hKsTs8s'))
print('2h4d2d4s4c:')
print(evaluate('2h4d2d4s4c'))
print('KsKhKc8sKd:')
print(evaluate('KsKhKc8sKd'))
print('3s9hTh9s9d:')
print(evaluate('3s9hTh9s9d'))
print('2s8hThQs9d:')
print(evaluate('2s8hThQs9d'))

class evaluateTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(evaluate('Qs7s2s4s5s'), 'Flush')
    def test2(self):
        self.assertEqual(evaluate('7h8hKsTs8s'), 'Pair')
    def test3(self):
        self.assertEqual(evaluate('2h4d2d4s4c'), "Full house")
    def test4(self):
        self.assertEqual(evaluate('KsKhKc8sKd'), "Four of a kind")
    def test5(self):
        self.assertEqual(evaluate('3s9hTh9s9d'), "Three of a kind")
    def test6(self):
        self.assertEqual(evaluate('2s8hThQs9d'), "Q high")

if __name__ =="__main__":
    unittest.main(exit = False)