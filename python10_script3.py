#!/usr/bin/env python3
import subprocess
subprocess.run(['ls','-lh'])

tmp_file="listing.txt"
with open (tmp_file, 'w') as ofh:
  oops=subprocess.check_call(['ls','-lh'],stdout=ofh)

print("Hello world")
