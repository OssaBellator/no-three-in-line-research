# Independent cylinder microcensus for Hall gadgets

`docs/556` proved that a quotient kernel does not determine its microscopic
lift.  This chapter reverses the order of construction: define local
microscopic states and completion rules first, enumerate every transition, and
only then search for a syndrome partition.

The microscopic state is `(s,e)` with

```text
s in Z/3Z, e in Z/2Z.
```

Each gadget has four labelled local choices `c=0,1,2,3`.  Orientation changes by

```text
e' = e xor (c mod 2).
```

The syndrome rules are

```text
A: s'=s       for c<3,  s'=s+1 for c=3,
B: s'=-s      for c<3,  s'=1-s for c=3,
```

with arithmetic modulo three.

## 1. Complete independent transition census

### Theorem PP3cpi -- PROVED / CYLINDER MICROGADGET ENUMERATION

The two displayed local rules produce two exact `6 x 6` nonnegative integer
transition matrices.  Every row and every column has sum four, and every
positive entry carries an explicit list of local choice labels realizing it.
There are thirty-six positive matrix entries across the two gadgets.

#### Proof

For each of the six source states and four choice labels, the displayed formulas
give one target state.  Counting equal targets gives the transition entries and
choice witnesses.  Direct summation verifies every row and column margin. ∎

## 2. Partition search after enumeration

### Theorem PP3cpj -- PROVED / UNIQUE COMMON PAIR-LUMPING

Among all fifteen partitions of six microscopic states into three unordered
pairs, exactly one is strongly lumpable for both enumerated gadgets:

```text
{{(0,0),(0,1)}, {(1,0),(1,1)}, {(2,0),(2,1)}}.
```

The resulting quotient matrices are

```text
A=((3,1,0),(0,3,1),(1,0,3)),
B=((3,1,0),(1,0,3),(0,3,1)).
```

#### Proof

Strong lumpability requires the two rows in every proposed source pair to have
identical aggregate counts into every proposed target pair.  Exhausting the
fifteen pair partitions leaves only the displayed syndrome fibres.  Aggregating
one row from each fibre gives the quotient matrices. ∎

## 3. Exact switched commutation

### Theorem PP3cpk -- PROVED / INDEPENDENT MICRO-TO-QUOTIENT COMMUTATION

For every microscopic starting state and every word in `A,B`, aggregation by the
unique syndrome partition commutes with the microscopic product.  Thus all
switched quotient estimates from `docs/532` apply to this independently
enumerated combinatorial candidate.

#### Proof

Strong lumpability is the matrix intertwining identity `MK=KQ` for each gadget,
where `K` aggregates microscopic states to syndrome fibres.  Multiplying these
identities proves commutation for every word. ∎

## 4. Stored exact audit

Run

```bash
python scripts/check_independent_hall_microcensus.py
```

The checker reconstructs all local transitions and choice witnesses, searches
all fifteen pair partitions, and directly checks all 511 switch words through
length eight from every microscopic start.

## 5. Prime-patching consequence

This removes the circular quotient-to-micro construction for one explicit
candidate model.  It does not yet promote the Hall row: the cylinder choices
have not been decoded as point configurations, matching moves, or local
prime-patching gadgets.  The remaining Hall task is now one precise map from
these or other independently enumerated states to actual geometry.
