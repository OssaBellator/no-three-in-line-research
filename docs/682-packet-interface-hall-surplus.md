# Unified defect-incidence packet Hall criterion

The component-exact first-stage packing in `docs/670` and the degree-two
centre-conflict formula in `docs/676` are local. This chapter packages both stages
into auditable incidence objects and records the exact loss when certified packets
are concatenated through bounded interfaces.

## PP3dde — Defect incidence and odd-path retention

After selecting `q` resource-disjoint motifs, let each of the resulting `3q`
centres carry one source-defect label and one host-defect label. Form the bipartite
defect multigraph `D` whose left and right vertices are the two label classes and
whose edges are the centres.

Assume the complete centre-conflict relation is exactly label sharing. Then the
centre-conflict graph is the line graph

```text
H = L(D).
```

If every source label and every host label occurs on at most two centres, then
`D` has maximum degree two. Its components are paths and even cycles, and the same
is true of `H`. In particular `H` is automatically bipartite; the separate
source- and host-degree restrictions are certified by one incidence table.

Let `o(H)` count odd-order path components, including isolated vertices. Since an
independent set in `L(D)` is a matching in `D`, the exact retained count is

```text
alpha(H) = nu(D) = (3q + o(H))/2.
```

Thus `3q+o(H)>=56` is the exact 28-centre condition inside one packet.

## PP3ddf — Additive packet retention with interface loss

For packet `j`, let the first-stage resource audit select `q_j` motifs and let its
internal defect graph retain

```text
r_j = (3q_j + o_j)/2
```

centres. Suppose the interface between packets `j` and `j+1` contributes at most
`c_j` additional conflict edges. Add an internal minimum vertex cover in every
packet and one endpoint of each interface edge. This covers the complete conflict
graph, so the concatenated family retains at least

```text
sum_j r_j - sum_j c_j.
```

For `K` identical packets with retention `r` and at most `c` interface edges at
each of the `K-1` joins, the bound becomes

```text
K r - (K-1)c = K(r-c)+c.
```

It has positive asymptotic density exactly when `r>c`. The least packet count
supplied by this certificate for the 28-centre target is

```text
max(1, ceil((28-c)/(r-c))).
```

For example, `(r,c)=(9,1)` or `(10,2)` needs four packets, while `(12,2)` needs
three.

## PP3ddg — Unified host-level promotion interface

A coordinate host may therefore certify Hall by supplying three finite data sets:

1. a motif-resource incidence graph whose connected components contain uniformly
   bounded numbers of motifs, so first-stage packing is exactly auditable
   component by component;
2. for each selected packet, a complete source/host defect incidence multigraph
   with both label loads at most two, giving the exact internal retention above;
3. certified bounds `c_j` on every cross-packet conflict interface.

The final Hall claim follows whenever

```text
sum_j (3q_j+o_j)/2 - sum_j c_j >= 28.
```

`scripts/check_hall_defect_incidence_line_graph.py` exhausts all 74,954 bipartite
incidence graphs with side sizes at most four. It verifies first-stage component
projection in every case and, for all 10,172 maximum-degree-two cases, verifies

```text
H=L(D),
alpha(H)=nu(D)=(|E(D)|+o(H))/2.
```

`scripts/check_hall_odd_path_surplus.py` independently checks the odd-path identity
and sharp Hall thresholds. `scripts/check_hall_packet_interface_surplus.py`
checks 76,156 two-packet graphs and confirms the interface lower bound; it is exact
in 3,766 cases and strict in 72,390, with maximum observed slack four.

## Evidence boundary

This is an asymptotic packet interface, not a coordinate construction. No current
host supplies actual motif resources, complete defect labels, uniformly bounded
packet interfaces, and the required source/host load conditions simultaneously.
