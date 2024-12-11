#!/usr/bin/env python3
#data = [
#"47|53",
#"97|13",
#"97|61",
#"97|47",
#"75|29",
#"61|13",
#"75|53",
#"29|13",
#"97|29",
#"53|29",
#"61|53",
#"97|53",
#"61|29",
#"47|13",
#"75|47",
#"97|75",
#"47|61",
#"75|61",
#"47|29",
#"75|13",
#"53|13",
#"",
#"75,47,61,53,29",
#"97,61,53,29,13",
#"75,29,13",
#"75,97,47,61,53",
#"61,13,29",
#"97,13,75,29,47"
#]
f = open("input.txt")
data = f.read().split("\n")

def parse_data(d):
    from_to = {}
    to_from = {}

    entries = []
    for l in d:
        s = l.split('|')
        if len(s) == 2:
            if not s[0] in from_to:
                from_to[s[0]] = []
            from_to[s[0]].append(s[1])
            if not s[1] in to_from:
                to_from[s[1]] = []
            to_from[s[1]].append(s[0])
        elif len(l) > 0:
            entries.append(l.split(','))
    
    return from_to, to_from, entries

def is_good_entry(from_to, to_from, entry):
    for i in range(len(entry)-1):
        for j in range(i+1, len(entry)):
            if not entry[j] in from_to:
                continue
            if entry[i] in from_to[entry[j]]:
                #print(entry[i], entry[j])
                return False
    return True

#print(parse_data(data))
        
from_to, to_from, entries = parse_data(data)

accum = 0
for entry in entries:
    if is_good_entry(from_to, to_from, entry):
        accum += int(entry[int(len(entry) / 2)])
    #print(is_good_entry(from_to, to_from, entry))
print(accum)