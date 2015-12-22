 import driver

   def letter(row, col):
        if 4<row<6 and 6<col<10:
             return 'X'
        elif 2<row<6 and 4<col<8:
            return 'Z'
        elif 4<row<8 and 7<col<12:
            return 'B'

        return 'T'
    
if __name__ == '__main__':
      driver.comparePatterns(letter)
