import unittest
from television import Television 

class TestTelevisionMethods(unittest.TestCase):

    def test_init(self):
        tv = Television()
        self.assertFalse(tv.status)  
        self.assertFalse(tv.muted)   
        self.assertEqual(tv.volume, Television.MIN_VOLUME)  
        self.assertEqual(tv.channel, Television.MIN_CHANNEL)  

    def test_power(self):
        tv = Television()
        tv.power()
        self.assertTrue(tv.status)  
        tv.power()
        self.assertFalse(tv.status)  


if __name__ == '__main__':
    unittest.main()
