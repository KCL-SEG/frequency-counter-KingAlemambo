"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""



 
def frequencies(items):
    frequencies = {}
    count_items=0
    # Your code goes here
    for item in items:
        count_items = 0
        count_items = items.count(item)
        key=str(item)
        frequencies[key]= count_items
    return frequencies

