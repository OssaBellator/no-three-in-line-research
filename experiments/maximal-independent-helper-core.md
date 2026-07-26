# Maximal-independent helper-core diagnostic

Run

```text
python scripts/check_maximal_independent_helper_core.py \
  experiments/maximal-independent-helper-core-example.json
```

The stored instance uses

```text
N=20,
b=5,
k_0=3.
```

The dense branch is the complete 3-uniform support hypergraph.  The sparse branch
is a matching of six disjoint triples.  The exact output is

```text
N 20
b 5
maximum support rank 3
dense complete supports 1140
dense maximal independent size 2
dense fixed core [0, 1]
dense fixed core size 2
dense extension degree 18
completion record count 4
exact pigeonhole lower bound 4.250000000000
required-size theorem lower bound 2.142857142857
sparse disjoint supports 6
sparse maximal independent size 14
support-free helper host [0, 1, 3, 4]
outcome support_free_host_or_fixed_core_pencil
```

For the complete triple table, the greedy maximal independent set is `{0,1}`.
Every other helper completes the forbidden support `{0,1,v}`, so one fixed core
has 18 singleton extensions, well above both PP3ann and PP3ano lower bounds.

For the sparse table, selecting two vertices from each disjoint triple gives a
large independent helper set.  The displayed four-point host contains no residual
support and is immediately eligible for a marked single-cycle completion.
