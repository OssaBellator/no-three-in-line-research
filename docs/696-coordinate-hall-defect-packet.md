# Coordinate Hall defect packet

`docs/682` gives the exact degree-two defect-incidence criterion, and `docs/688`
gives the exact max-plus packet transfer. This chapter supplies a finite integer
coordinate realization joining those two interfaces.

## PP3deu — Integer realization of degree-two defect graphs

Let `D=(S,H;E)` be a finite simple bipartite graph of maximum degree at most two.
Choose one variable `X_s` for each source label and one variable `Y_h` for each
host label, and represent an edge `(s,h)` by the point

```text
(X_s,Y_h).
```

Distinct source variables and distinct host variables make row or column sharing
exactly the line-graph adjacency in `L(D)`.

For any three distinct edges, the collinearity determinant is a nonzero polynomial
in the `X_s` and `Y_h`. Indeed, three edges cannot share one source or one host
because the maximum degree is two. If two share a source, the determinant contains
the nonzero factor formed by their distinct host variables and the third source
variable; the host-sharing case is symmetric. If all source and host labels are
distinct, the determinant visibly contains uncancelled mixed monomials.

Multiply all such determinants together with all source- and host-distinctness
factors. The product is a nonzero integer polynomial, so it has an integer
specialization at which none of its factors vanish. Therefore every finite simple
maximum-degree-two defect graph has an integer point realization satisfying

```text
row/column conflict graph = L(D)
```

and containing no collinear triple.

This is a finite realization theorem. It permits the exact Hall transfer graph to
be embedded anew for every finite packet chain; it does not assert a fixed affine
translation rule or bounded coordinates independent of chain length.

## PP3dev — Explicit ten-motif packet retaining twenty-eight centres

Take ten motifs, each with three centres, and assign three private coordinate
resource tokens to every motif. The ten resource lists are pairwise disjoint, so
the first-stage exact packing selects

```text
q=10
```

motifs and all thirty candidate centres.

Choose the source/host defect edges so that centres `0,1` share one source label,
centres `2,3` share one host label, and all remaining labels are private. The
defect graph has

```text
two two-edge paths and twenty-six isolated edges.
```

Both source and host load histograms are

```text
load one: 28 labels,
load two:  1 label.
```

Its line graph is two independent conflict edges plus twenty-six isolated
vertices. Hence

```text
alpha(L(D)) = 26 + 2 = 28.
```

The checker gives an explicit realization by assigning powers of two to source
coordinates and powers of three to host coordinates. The thirty points are
distinct, row/column sharing agrees exactly with defect-label sharing, and every
one of the `C(30,3)=4,060` triples has nonzero determinant. The largest coordinate
uses 46 bits.

Thus this synthetic coordinate packet meets the exact internal 28-centre Hall
target without an interface estimate.

## PP3dew — Exact repeatable transfer with one boundary conflict

Mark two internally isolated centres as left and right ports. Join packet `k` to
packet `k+1` by identifying the right host label of packet `k` with the left host
label of packet `k+1`. Each interface adds exactly one conflict edge, and the
complete chain conflict graph remains a matching.

For exact left/right occupancy bits, the one-packet table is

```text
W[0,0]=26,
W[0,1]=27,
W[1,0]=27,
W[1,1]=28.
```

Max-plus composition with the compatibility condition forbidding simultaneous
selection of adjacent interface ports gives

```text
alpha_K = 27K+1
```

for every `K>=1`. The asymptotic transfer rate is therefore 27 retained centres
per packet. The audit checks the transfer recurrence for `K=1,...,12` and obtains

```text
28,55,82,109,136,163,190,217,244,271,298,325.
```

It also constructs explicit power-coordinate realizations for chains of one
through six packets, up to 180 points. Every chain has exact row/column conflict
adjacency and no collinear triple; the maximum-coordinate bit lengths are

```text
46,91,135,180,224,268.
```

The exact checker is `scripts/check_hall_coordinate_defect_packet.py`.

## Evidence boundary

This chapter closes the abstract-to-coordinate gap for one synthetic defect
packet and for its finite chains. Its motif resource tokens and defect labels are
designed data, not resources extracted from the prime-patching coordinate host.
Consequently the Hall row remains `4/5`: no evidence row is promoted, geometric
closure is false, and the all-`n` theorem remains open.

The next theorem identifier is `PP3dex`.
