from pyunpack import Archive
import os
import binwalk

for filename in os.listdir('./part2'):
    print(f"Extracting {filename}")
    os.mkdir(f"./extracted/{filename}")
    Archive(f'./part2/{filename}').extractall(f"./extracted/{filename}")

print("done")