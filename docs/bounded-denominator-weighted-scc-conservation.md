# BDA weighted conservation through cyclic source components

This note upgrades the source-SCC quotient from token counts to exact nonnegative numerator mass. It does not prove BDA6 or the no-three-in-line conjecture.

## Weighted source occurrences

Each live source occurrence carries a nonnegative integer mass. Initial occurrences and externally paid deposits are the only permitted sources of new mass.

A dependency transition is complete when it records one input occurrence, one output occurrence, their source-component addresses, and both masses.

## Conservative transition contract

Every internal or cross-component transition must satisfy:

- one input occurrence produces at most one output occurrence;
- the output retains the same occurrence lineage;
- output mass is at most input mass;
- the condensation-component index never moves backward.

Transitions inside a strongly connected component may repeat arbitrarily. They recycle physical mass but do not create it.

## Exact weighted potential

Let `M_0` be total initial mass and `D` total deposited mass. At every time,

`used terminal mass + remaining live mass <= M_0 + D`.

Therefore cumulative terminal restoration cost is at most `M_0+D` whenever every restoration unit is charged to consumed source mass.

Cyclic dependency components cause no additional factor: repeated circulation changes the location of a token, not its available mass. Cross-component motion can still be recorded by the finite condensation rank when a path-length or address bound is needed.

## Restoration routing

Combining this potential with the exact large-jump source/restoration pair gives:

- all bounded and unbounded restoration magnitudes are paid by weighted source mass;
- an exhausted source returns an exact least-mass source address;
- any mass increase, split, source-less creation, merge without complete accounting, or lineage loss is an explicit amplification/reset obstruction.

## Outside the contract

The statement does not cover fractional hidden mass, destructive transitions whose lost mass is later recreated without a deposit, dynamic source dictionaries, or physical operations that duplicate one occurrence into several chargeable descendants.
