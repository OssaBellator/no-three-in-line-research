# Bounded-denominator closed-walk gain localization

This note records BDA5dj--BDA5dn. It reduces every finite amplifying source walk to one exact simple directed gain cycle.

## Contract

Let `G` be a finite directed source graph. Every directed edge `e` has a retained positive rational gain `g_e`. Walk gain is the ordered product of edge gains. Vertices, edges and gains are occurrence-faithful and do not change during the argument.

## Theorem block

### BDA5dj — closed-walk decomposition

Every nonempty directed closed walk decomposes, by repeatedly removing the first repeated-vertex segment, into a finite multiset of simple directed cycles.

### BDA5dk — exact product factorization

The gain of the closed walk equals the product of the gains of the extracted simple cycles, with multiplicity.

### BDA5dl — amplification localization

If a closed walk has gain greater than one, at least one extracted simple directed cycle has gain greater than one.

### BDA5dm — sufficiency of simple-cycle checks

All directed closed walks are nonamplifying exactly when every simple directed cycle has gain at most one. Under that condition the rational gain-potential theorem applies.

### BDA5dn — reset boundary

Gain changes inside a traversal, edge relabelling, omitted source vertices, branching/splitting of one occurrence, or source-less creation are outside the theorem and return reset or amplification.

## Proof

Removing a repeated-vertex segment preserves directed order and partitions the edge multiset of the closed walk. Multiplicativity gives the product factorization. A product of positive numbers can exceed one only if one factor exceeds one.

## Remaining physical work

The result reduces physical nonamplification to excluding simple gain cycles in the concrete arithmetic source graph. It does not construct that graph or prove its cycle inequalities.