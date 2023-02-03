def grammar_expansion(rules,start_symbol):
    expandedRules  = []
    firstChar = start_symbol + "'"

    expandedRules .append([firstChar,
                     ['.', start_symbol]])
    for rule in rules:
        k = rule.split("->")
        lhs = k[0].strip()
        rhs = k[1].strip()
        multirhs = rhs.split('|')
        for rhs1 in multirhs:
            rhs1 = rhs1.strip().split()
            rhs1.insert(0, '.')
            expandedRules .append([lhs, rhs1])
    return expandedRules 
 
 