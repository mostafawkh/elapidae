from goto import goto
def gotoHandler(state):
    global statesDict, stateCount
 
    # find all symbols on which we need to
    # make function call - GOTO
    generateStatesFor = []
    for rule in statesDict[state]:
        # if rule is not "Handle"
        if rule[1][-1] != '.':
            indexOfDot = rule[1].index('.')
            dotPointsHere = rule[1][indexOfDot + 1]
            if dotPointsHere not in generateStatesFor:
                generateStatesFor.append(dotPointsHere)
 
    # call GOTO iteratively on all symbols pointed by dot
    if len(generateStatesFor) != 0:
        for symbol in generateStatesFor:
            goto(state, symbol)
    return