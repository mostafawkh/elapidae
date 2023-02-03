def grammar_expansion(rules, nonterm_userdef,
                        start_symbol):

    newRules = []

    newChar = start_symbol + "'"
    while (newChar in nonterm_userdef):
        newChar += "'"
 
    newRules.append([newChar,
                     ['.', start_symbol]])
 
    for rule in rules:
       
        k = rule.split("->")
        lhs = k[0].strip()
        rhs = k[1].strip()
         
        multirhs = rhs.split('|')
        for rhs1 in multirhs:
            rhs1 = rhs1.strip().split()
             
            rhs1.insert(0, '.')
            newRules.append([lhs, rhs1])
    return newRules
 
 