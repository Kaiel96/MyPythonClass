import driver

def letter(row, col):
        if row>col:
            return 'T'
        return 'W'
    
if __name__ == '__main__':
      driver.comparePatterns(letter)
