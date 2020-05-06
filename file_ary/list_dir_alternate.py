import glob
import os
for name in glob.glob('*.ht??'):
    os.unlink(name)