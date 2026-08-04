# Coordinate Hall defect packet

`docs/682` gives the exact degree-two defect-incidence criterion, and `docs/688`
gives the exact max-plus packet transfer. This chapter supplies a finite integer
coordinate realization joining those two interfaces.

## PP3dex — Integer realization of degree-two defect graphs

Let `D=(S,H;E)` be a finite simple bipartite graph of maximum degree at most two.
Choose one variable `X_s` for each source label and one variable `Y_h` for each
host label, and represent an edge `(s,h)` by the point

```text
(X_s,Y_h).
```

Distinct source variables and distinct host variables make row or column sharing
exactly the line-graph adjacency in `L(D)`.

For any three distinct edges, the collinearity determinant is a nonzero polynomial
in the `X_s` and `Y_h`. Three edges cannot share one source or one host because the
maximum degree is two. If two share a source, the determinant contains the
nonzero factor formed by their distinct host variables and the third source
variable; the host-sharing case is symmetric. If all source and host labels are
distinct, the determinant contains uncancelled mixed monomials.

Multiply these determinants together with all source- and host-distinctness
factors. The product is a nonzero integer polynomial, so some integer
specialization makes every factor nonzero. Therefore every finite simple
maximum-degree-two defect graph has an integer point realization satisfying

```text
row/column conflict graph = L(D)
```

and containing no collinear triple.

This permits the exact Hall transfer graph to be embedded anew for every finite
packet chain. It does not assert a bounded-coordinate affine translation rule
independent of chain length.

## PP3dey — Explicit ten-motif packet retaining twenty-eight centres

Take ten motifs, each with three centres, and give every motif three private
resource tokens. The resource lists are pairwise disjoint, so the first-stage
packing selects all ten motifs and all thirty centres.

Assign source/host defect edges so that centres `0,1` share one source label,
centres `2,3` share one host label, and every remaining label is private. The
defect graph has two two-edge paths and twenty-six isolated edges. Both source and
host load histograms are

```text
load one: 28 labels,
load two:  1 label.
```

Its line graph is two disjoint conflict edges plus twenty-six isolates. Hence

```text
alpha(L(D)) = 28.
```

An explicit realization assigns powers of two to source coordinates and powers of
three to host coordinates. The thirty points are distinct, row/column sharing
agrees exactly with defect-label sharing, and all `C(30,3)=4,060` triples have
nonzero determinant. The largest coordinate uses 46 bits.

Thus this synthetic coordinate packet meets the exact internal 28-centre Hall
target without an interface estimate.

## PP3dez — Exact repeatable transfer with one boundary conflict

Mark two internally isolated centres as left and right ports. Join packet `k` to
packet `k+1` by sharing the right host label of packet `k` with the left host label
of packet `k+1`. Each interface adds exactly one conflict edge, and the complete
chain conflict graph remains a matching.

For exact left/right occupancy bits, the one-packet table is

```text
W[0,0]=26,
W[0,1]=27,
W[1,0]=27,
W[1,1]=28.
```

Max-plus composition with the interface compatibility condition gives

```text
alpha_K = 27K+1
```

for every `K>=1`. The audit checks the transfer recurrence for `K=1,...,12` and
constructs explicit no-three coordinate chains for one through six packets, up to
180 points. Their maximum-coordinate bit lengths are

```text
46,91,135,180,224,268.
```

`scripts/check_hall_coordinate_defect_packet.py` certifies the explicit packet and
chains. Independently,
`scripts/check_hall_two_motif_incidence_packets.py` classifies all 1,636
six-centre conflict graphs realizable as the union of source and host matchings and
checks 6,544 one-through-four packet transfer values against direct independence
numbers.

## Evidence boundary

This chapter closes the abstract-to-coordinate gap for one synthetic defect
packet and its finite chains. Its motif resource tokens and defect labels are
designed data, not resources extracted from the prime-patching coordinate host.
Consequently the Hall row remains `4/5`: no evidence row is promoted, geometric
closure is false, and the all-`n` theorem remains open.

The next theorem identifier is `PP3dfa`.
