"""
AX : 1+3 
AY : 2+6
AZ : 3+0
BX : 1+0
BY : 2+3
BZ : 3+6
CX : 1+6
CY : 2+0
CZ : 3+3
"""

score_matrix = str.maketrans({
    "A X" : 4, 
    "A Y" : 8,
    "A Z" : 3,
    "B X" : 1,
    "B Y" : 5,
    "B Z" : 9,
    "C X" : 7,
    "C Y" : 2,
    "C Z" : 6
})


