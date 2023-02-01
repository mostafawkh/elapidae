def grammarExpansion(rules, nonterm_userdef,
                        start_symbol):
   
    # newRules stores processed output rules
    newRules = []
 
    # create unique 'symbol' to
    # - represent new start symbol
    newChar = start_symbol + "'"
    while (newChar in nonterm_userdef):
        newChar += "'"
 
    # adding rule to bring start symbol to RHS
    newRules.append([newChar,
                     ['.', start_symbol]])
 
    # new format  => [LHS,[.RHS]],
    # can't use dictionary since
    # - duplicate keys can be there
    for rule in rules:
       
        # split LHS from RHS
        k = rule.split("->")
        lhs = k[0].strip()
        rhs = k[1].strip()
         
        # split all rule at '|'
        # keep single derivation in one rule
        multirhs = rhs.split('|')
        for rhs1 in multirhs:
            rhs1 = rhs1.strip().split()
             
            # ADD dot pointer at start of RHS
            rhs1.insert(0, '.')
            newRules.append([lhs, rhs1])
    return newRules
 
 