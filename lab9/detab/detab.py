import sys

OUTFILE_NAME = "detabbed"
TAB_STOP_SIZE = 8
NUM_ARGS = 2
FILE_ARG_IDX = 1


def args(argv):
   if (len(argv) < NUM_ARGS):
      print >> sys.stderr, "file name missing"
      sys.exit(1)

   try:
      infile = open(argv[FILE_ARG_IDX], "r")
   except IOError as e:
      print >> sys.stderr, e
      sys.exit(1)


if __name__ == "__args__":
   args(sys.argv)

def writer():
   try:
      outfile = open(OUTFILE_NAME, "w")
   except IOError as e:
      print >> sys.stderr, e
      sys.exit(1)

if __name__ == "__writer__":
      writer()

def tabber(): 
   character_count = 0;

   c = infile.read(1)
   while (c):
      if (c == '\t'):
         num_spaces =  TAB_STOP_SIZE - (character_count % TAB_STOP_SIZE)
         for i in range(num_spaces):
            outfile.write(' ')
         character_count = character_count + num_spaces
      elif (c == '\n'):
         outfile.write('\n')
         character_count = 0
      else:
         outfile.write(c)
         character_count = character_count + 1
      c = infile.read(1)

   infile.close()
   outfile.close()

if __name__ == "__tabber__":
      tabber()
   


