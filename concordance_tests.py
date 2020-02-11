import unittest
import filecmp
from concordance import *

class TestList(unittest.TestCase):

   def test_01(self):
       conc = Concordance()
       conc.load_stop_table("stop_words.txt")
       conc.load_concordance_table("file1.txt")
       conc.write_concordance("file1_con.txt")
       self.assertTrue(filecmp.cmp("file1_con.txt", "file1_sol.txt"))

   def test_02(self):
       conc = Concordance()
       conc.load_stop_table("stop_words.txt")
       conc.load_concordance_table("file2.txt")
       conc.write_concordance("file2_con.txt")
       self.assertTrue(filecmp.cmp("file2_con.txt", "file2_sol.txt"))

   def test_03(self):
       conc = Concordance()
       conc.load_stop_table("stop_words.txt")
       conc.load_concordance_table("declaration.txt")
       conc.write_concordance("declaration_con.txt")
       self.assertTrue(filecmp.cmp("declaration_con.txt", "declaration_sol.txt"))

   def test_04(self):
       conc = Concordance()
       conc.load_stop_table("empty.txt")
       conc.load_concordance_table("a.txt")
       conc.write_concordance("a_con.txt")
       self.assertTrue(filecmp.cmp("a_con.txt", "a_sol.txt"))

   def test_05_stop_table_not_found(self):
       conc = Concordance()
       with self.assertRaises(FileNotFoundError):
           conc.load_stop_table("pppppp.txt")

   def test_06_concordance_not_found(self):
       conc = Concordance()
       with self.assertRaises(FileNotFoundError):
           conc.load_concordance_table("pppppp.txt")

   def test_07(self):
       conc = Concordance()
       conc.load_stop_table("stop_words.txt")
       conc.load_concordance_table("empty.txt")
       conc.write_concordance("empty_con.txt")
       self.assertTrue(filecmp.cmp("empty_con.txt", "empty.txt"))

   def test_08(self):
       conc = Concordance()
       self.assertEqual(conc.stop_table, None)
       self.assertEqual(conc.concordance_table, None)
       conc.load_stop_table("empty.txt")
       conc.load_concordance_table("a.txt")
       self.assertEqual(conc.concordance_table.table_size, 191)
       self.assertEqual(conc.concordance_table.num_items, 2)
       conc.write_concordance("a_con.txt")
       self.assertTrue(filecmp.cmp("a_con.txt", "a_sol.txt"))

   def test_09(self):
       conc = Concordance()
       conc.load_stop_table("stop_words.txt")
       conc.load_concordance_table("punctuation.txt")
       conc.write_concordance("punctuation_con.txt")
       self.assertTrue(filecmp.cmp("punctuation_con.txt", "empty.txt"))

   def test_10(self):
       conc = Concordance()
       conc.load_stop_table("stop_words.txt")
       conc.load_concordance_table("bed.txt")
       conc.write_concordance("bed_con.txt")
       self.assertTrue(filecmp.cmp("bed_con.txt", "bed_sol.txt"))

if __name__ == '__main__':
   unittest.main()
