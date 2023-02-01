def findClosure(input_state, dotSymbol):
    global start_symbol, \
        separatedRulesList, \
        statesDict
 
    # closureSet stores processed output
    closureSet = []
 
    # if findClosure is called for
    # - 1st time i.e. for I0,
    # then LHS is received in "dotSymbol",
    # add all rules starting with
    # - LHS symbol to closureSet
    if dotSymbol == start_symbol:
        for rule in separatedRulesList:
            if rule[0] == dotSymbol:
                closureSet.append(rule)
    else:
        # for any higher state than I0,
        # set initial state as
        # - received input_state
        closureSet = input_state
 
    # iterate till new states are
    # - getting added in closureSet
    prevLen = -1
    while prevLen != len(closureSet):
        prevLen = len(closureSet)
 
        # "tempClosureSet" - used to eliminate
        # concurrent modification error
        tempClosureSet = []
 
        # if dot pointing at new symbol,
        # add corresponding rules to tempClosure
        for rule in closureSet:
            indexOfDot = rule[1].index('.')
            if rule[1][-1] != '.':
                dotPointsHere = rule[1][indexOfDot + 1]
                for in_rule in separatedRulesList:
                    if dotPointsHere == in_rule[0] and \
                            in_rule not in tempClosureSet:
                        tempClosureSet.append(in_rule)
 
        # add new closure rules to closureSet
        for rule in tempClosureSet:
            if rule not in closureSet:
                closureSet.append(rule)
    return closureSet