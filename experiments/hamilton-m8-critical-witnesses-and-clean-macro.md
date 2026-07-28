# Exact `m=8` critical witnesses and parity-clean macro graph

The checker `scripts/check_hamilton_m8_critical_witnesses_and_clean_macro.cpp`
reconstructs every signed Hamilton state at pair size `m=8`, identifies the
44 states whose strict descent distance is five, and builds the complete
owner-intersecting parity-clean macro graph without materializing its edges.

## Five-step critical witnesses

```text
sharp states                         44
Hamilton cycles supporting them      14
global-sign-complement orbits         22
```

Support split:

```text
one two-owner support, no three-owner support      12
one three-owner support, no two-owner support      32
```

Minimum defect after one legal targeted move:

```text
4: 4 states
8: 8 states
12: 8 states
16: 20 states
20: 4 states
```

Every shortest five-move repair path has one of two move words:

```text
F,R,R,R,R : 12 states
R,R,R,R,R : 32 states
```

Here `F` is an owner orientation flip and `R` is a three-source successor
rotation.

## Complete parity-clean macro graph

A macro step starts from a parity-clean signed state, selects a present
three-owner flaw with owner set `S`, chooses any parity-satisfiable successor
rotation on a source triple `T` with `T intersect S != empty`, and then chooses
any clean orientation in the target fibre.

All `404,080` parity-clean `m=8` states reach one of the 28 valid states.  The
exact macro-distance distribution is

```text
0:     28
1: 66,844
2:303,576
3: 33,632
```

Thus the maximum parity-clean macro distance is three.

Among the 32 sharp three-owner witnesses, the exact macro distances are

```text
1:12
2: 4
3:16
```

The five-step obstruction in the unrestricted targeted graph therefore does
not survive on the parity-clean macro manifold.

## Reproduction

```bash
g++ -O3 -std=c++17 \
  scripts/check_hamilton_m8_critical_witnesses_and_clean_macro.cpp \
  -o /tmp/check_hamilton_m8_critical_witnesses_and_clean_macro
/tmp/check_hamilton_m8_critical_witnesses_and_clean_macro
```

The output must match
`experiments/hamilton-m8-critical-witnesses-and-clean-macro-audit.json`.
