class ProductOfNumbers(object):

    def __init__(self):
     self.s = [1]

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num == 0:
          self.s = [1]
        else:
         print( self.s.append(num))

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        last_k_num = self.s[-k]
        product = 1
        for num in last_k_num:
          product = product * num
          print(product)
          
    print(getProduct('1,4,5,3,2',3))      
