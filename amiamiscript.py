import amiami
from pathlib import Path

#this script searches the amiami API and returns available items according to the search items found in input.txt
#currently an issue with search queries with large numbers of results

def open_file():
  p = Path(__file__).with_name('input.txt')
  with p.open('r') as f:
    lines = f.readlines()
    return lines

def amiami_search():

  lines = open_file()
  for line in lines:
    results = amiami.search(str(line))
    for item in results.items:
      if item.availability == "Available":
        print(("{}, {}".format(item.productName, item.availability)))
        print("\n")
  





amiami_search()
