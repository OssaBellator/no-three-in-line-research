#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import product

BLOCKS = [
    [(0,0,0,(F(9,10),F(1,10)),"A"),(0,1,1,(F(2,5),F(3,5)),"B"),(0,0,2,(F(1,5),F(4,5)),"C")],
    [(0,0,1,(F(4,5),F(1,5)),"D"),(0,1,2,(F(1,2),F(1,2)),"E"),(1,0,1,(F(3,5),F(2,5)),"F"),(1,1,0,(F(7,10),F(3,10)),"G")],
    [(0,0,0,(F(1,10),F(9,10)),"H"),(0,0,2,(F(1,2),F(1,5)),"I"),(1,0,1,(F(2,5),F(2,5)),"J")],
]

def dominates(left,right): return left[0]<=right[0] and left[1]<=right[1]

def pareto(items):
    unique={}
    for error,plan in items: unique.setdefault(error,plan)
    return sorted((error,plan) for error,plan in unique.items() if not any(other!=error and dominates(other,error) for other in unique))

plans=[]
for choice in product(*BLOCKS):
    if choice[0][0]!=0 or choice[-1][1]!=0: continue
    if any(choice[i][1]!=choice[i+1][0] for i in range(len(choice)-1)): continue
    work=sum(option[2] for option in choice)
    error=(sum(option[3][0] for option in choice),sum(option[3][1] for option in choice))
    plans.append((work,error,tuple(option[4] for option in choice)))
assert len(plans)==9

messages={(0,0):[((F(0),F(0)),tuple())]}
layer_sizes=[]
for block in BLOCKS:
    raw={}
    for (left_state,work),entries in messages.items():
        for option in block:
            if option[0]!=left_state: continue
            key=(option[1],work+option[2])
            for error,plan in entries:
                new_error=(error[0]+option[3][0],error[1]+option[3][1])
                raw.setdefault(key,[]).append((new_error,plan+(option[4],)))
    messages={key:pareto(entries) for key,entries in raw.items()}
    layer_sizes.append(sum(len(entries) for entries in messages.values()))

frontier_sizes=[]
for budget in range(9):
    message_items=[]
    for (state,work),entries in messages.items():
        if state==0 and work<=budget: message_items.extend(entries)
    message_frontier=pareto(message_items)
    brute_frontier=pareto([(error,plan) for work,error,plan in plans if work<=budget])
    assert [error for error,_ in message_frontier]==[error for error,_ in brute_frontier]
    frontier_sizes.append(len(message_frontier))

TOLERANCE=(F(8,5),F(5,4))
minimum_budget=None
feasible=[]
for budget in range(9):
    items=[]
    for (state,work),entries in messages.items():
        if state==0 and work<=budget: items.extend(entries)
    candidates=[(error,plan) for error,plan in pareto(items) if dominates(error,TOLERANCE)]
    if candidates:
        minimum_budget=budget
        feasible=candidates
        break
assert minimum_budget==4
assert feasible==[((F(3,2),F(6,5)),("B","F","I"))]

budget_three=pareto([(error,plan) for work,error,plan in plans if work<=3])
assert all(not dominates(error,TOLERANCE) for error,_ in budget_three)
assert [error for error,_ in budget_three]==[(F(11,10),F(19,10)),(F(3,2),F(13,10)),(F(9,5),F(1)),(F(11,5),F(1,2))]

print({"compatible_full_plans":len(plans),"message_entries_after_each_block":layer_sizes,"frontier_sizes_by_budget_0_to_8":frontier_sizes,"minimum_feasible_budget":minimum_budget,"unique_plan":list(feasible[0][1]),"certified_error":[str(x) for x in feasible[0][0]],"budget_three_obstruction_size":len(budget_three)})
