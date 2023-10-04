"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""



 
def frequencies(items):
    frequencies = {}
    
    # Your code goes here
    for item in items:
        key=str(item)
        frequencies[key]= frequencies.get(key,0)+1
    return frequencies

