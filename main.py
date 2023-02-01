from grammar import grammarExpansion
from closure import find_closure
from states import create_states
from parser import create_parse_table

def printResult(rules):
    for rule in rules:
        print(f"{rule[0]} ->"
              f" {' '.join(rule[1])}")
 
def printAllGOTO(diction):
    for itr in diction:
        print(f"GOTO ( I{itr[0]} ,"
              f" {itr[1]} ) = I{stateMap[itr]}")
 
# *** MAIN *** - Driver Code
 
# uncomment any rules set to test code
# follow given format to add -
# user defined grammar rule set
# rules section - *START*
 
# example sample set 01
rules = ["E -> E + T | T",
         "T -> T * F | F",
         "F -> ( E ) | id"
         ]
nonterm_userdef = ['E', 'T', 'F']
term_userdef = ['id', '+', '*', '(', ')']
start_symbol = nonterm_userdef[0]
 
# example sample set 02
# rules = ["S -> a X d | b Y d | a Y e | b X e",
#          "X -> c",
#          "Y -> c"
#          ]
# nonterm_userdef = ['S','X','Y']
# term_userdef = ['a','b','c','d','e']
# start_symbol = nonterm_userdef[0]
 
# rules section - *END*
print("\nOriginal grammar input:\n")
for y in rules:
    print(y)
 
# print processed rules
print("\nGrammar after Augmentation: \n")
separatedRulesList = \
    grammarExpansion(rules,
                        nonterm_userdef,
                        start_symbol)
printResult(separatedRulesList)
 
# find closure
start_symbol = separatedRulesList[0][0]
print("\nCalculated closure: I0\n")
I0 = find_closure(0, start_symbol)
printResult(I0)
 
# use statesDict to store the states
# use stateMap to store GOTOs
statesDict = {}
stateMap = {}
 
# add first state to statesDict
# and maintain stateCount
# - for newState generation
statesDict[0] = I0
stateCount = 0
 
# computing states by GOTO
create_states(statesDict)
 
# print goto states
print("\nStates Generated: \n")
for st in statesDict:
    print(f"State = I{st}")
    printResult(statesDict[st])
    print()
 
print("Result of GOTO computation:\n")
printAllGOTO(stateMap)
 
# "follow computation" for making REDUCE entries
diction = {}
 
# call createParseTable function
create_parse_table(statesDict, stateMap,
                 term_userdef,
                 nonterm_userdef)