from chain_code import Solution
import unittest

class SolutionTests(unittest.TestCase):

    
    def test1(self):
        solution = Solution()
        self.assertEqual(solution.chain("The cat sat on the Ikea mat"), "Eht act ast no eht Aeik amt")

    def test2(self):
        solution = Solution()
        self.assertEqual(solution.chain("Once upon a time."), "Ceno nopu a eimt.")
    
    def test3(self):
        solution = Solution()
        self.assertEqual(solution.chain("The quick brown Mr Fox."), "Eht cikqu bnorw Mr Fox.")

    def test4(self):
        solution = Solution()
        self.assertEqual(solution.chain("Is"), "Is")

    def test5(self):
        solution = Solution()
        # double space
        self.assertEqual(solution.chain("a"), "a")

    def test6(self):
        solution = Solution()
        self.assertEqual(solution.chain("^&%$£()!+"), "^&%$£()!+")
    def test7(self):
        solution = Solution()
        self.assertEqual(solution.chain("AZ-^&%$!()!+c"), "AC-^&%$!()!+z")
    
    def test8(self):
        solution = Solution()
        self.assertEqual(solution.chain("CaB pUn NASA ZxY"), "AbC nPu AANS XyZ")
    def test9(self):
        solution = Solution()
        self.assertEqual(solution.chain(""), "")
    def test10(self):
        solution = Solution()
        self.assertEqual(solution.chain("East, west, home's best"), "Aest, estw, ehmo's best")
    def test11(self):
        solution = Solution()
        self.assertEqual(solution.chain("One % inspiration, ninety-nine % perspiration."), "Eno % aiiinnoprst, eeiinn-nnty % aeiinopprrst.")

    def test12(self):
        solution = Solution()
        self.assertEqual(solution.chain("Waste not want not ."), "Aestw not antw not .")
    def test13(self):
        solution = Solution()
        self.assertEqual(solution.chain("If iT Ain'T BRoKe, doN't Fix IT"), "Fi iT Ain'T BEkOr, dnO't Fix IT")
    
    def test9(self):
        solution = Solution()
        self.assertEqual(solution.chain("Han&nah An-na Ci'vic Race-car R'adar."), "Aah&hnn Aa-nn Cc'iiv Aacc-err A'adrr.")
if __name__ == '__main__':
    unittest.main()