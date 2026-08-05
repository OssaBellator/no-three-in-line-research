# Hall thirty-centre extremal signatures

This chapter sharpens the host-extraction target left open by
`docs/697-coordinate-hall-defect-packet.md`. Assume the complete centre-conflict
graph is the line graph of a bipartite defect graph of maximum degree two, so its
components are paths and even cycles.

## PP3dfm — Complete thirty-centre retention classification

For a conflict graph `H` on thirty centres, let `o(H)` be the number of odd-order
path components, including isolates. Then

```text
alpha(H) = (30+o(H))/2.
```

Therefore `alpha(H)>=28` is equivalent to `o(H)>=26`. Since thirty and `o(H)`
have the same parity, only `o=26,28,30` can occur.

Enumerating every multiset of path and even-cycle component orders summing to
thirty gives 18,170 signatures. Exactly nine retain at least twenty-eight
centres:

```text
alpha=30:
  30P1

alpha=29:
  28P1 + P2
  27P1 + P3

alpha=28:
  26P1 + 2P2
  26P1 + P4
  26P1 + C4
  25P1 + P2 + P3
  25P1 + P5
  24P1 + 2P3.
```

Here `Pm` denotes a path on `m` conflict vertices and `Cm` an even cycle on `m`
vertices.

## PP3dfn — Sharp private-label requirement

An isolated conflict vertex is an isolated edge of the bipartite defect graph.
Consequently both its source label and its host label occur nowhere else in the
packet.

Every thirty-centre packet retaining at least twenty-eight centres therefore has
at least twenty-four centres whose source and host labels are both private. At
most six centres may participate in any defect-label collision.

This bound is sharp: the signature

```text
24P1 + 2P3
```

has exactly twenty-four isolated centres and retains twenty-eight. The synthetic
packet from `docs/697` realizes another exact signature,

```text
26P1 + 2P2.
```

## PP3dfo — Host-extraction search reduction

A host-derived thirty-centre candidate satisfying the degree-two incidence model
need not be passed through a general maximum-independent-set search. It can be
rejected immediately unless its complete conflict component signature is one of
the nine signatures above.

For the exact twenty-eight target, only the six `alpha=28` signatures are needed.
Thus host extraction may search directly for ten resource-disjoint motifs whose
thirty centres have at least twenty-four fully private defect-label pairs and at
most one of the six listed nontrivial component patterns.

The exact enumeration is
`scripts/check_hall_thirty_centre_extremal_signatures_702.py`.

## Evidence boundary

This is an exact structural filter, not a host-derived packet. No current
prime-patching host is proved to supply the required motif resources and private
label pattern, so the Hall evidence row remains unpromoted and the all-`n`
theorem remains open.
