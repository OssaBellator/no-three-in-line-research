# Packet-interface Hall surplus

The component-exact first-stage packing in `docs/670` and the degree-two
centre-conflict formula in `docs/676` are local. This chapter records the exact
loss incurred when certified local packets are concatenated through bounded
interfaces.

## PP3dde — Additive packet retention with interface loss

For packet `j`, suppose the first-stage audit selects `q_j` motifs and the internal
bipartite degree-two centre-conflict graph has matching loss `m_j`. The packet then
retains exactly

```text
r_j = 3 q_j - m_j
```

centres before cross-packet conflicts are added.

Suppose the interface between packets `j` and `j+1` contains at most `c_j`
additional conflict edges. Add an internal minimum vertex cover in each packet and
one endpoint of every interface edge. This covers the complete centre-conflict
graph, so the concatenated family retains at least

```text
sum_j r_j - sum_j c_j.
```

No independence or disjointness assumption is needed between the internal covers
and the chosen interface endpoints; overlap can only improve the bound.

## PP3ddf — Identical-packet surplus and exact packet threshold

For `K` identical packets with local retained count `r` and at most `c` interface
edges at each of the `K-1` joins, the certified retained count is

```text
K r - (K-1)c = K(r-c)+c.
```

Thus a positive asymptotic Hall density is certified exactly when

```text
r > c.
```

For the 28-centre target, the least packet count supplied by this certificate is

```text
max(1, ceil((28-c)/(r-c))).
```

For example, `(r,c)=(9,1)` or `(10,2)` needs four packets, while `(12,2)` needs
three.

## PP3ddg — Exact small-interface audit

`scripts/check_hall_packet_interface_surplus.py` exhausts every bipartite packet
graph with side sizes at most two, every pair of such packets, and every matching
interface between them. It checks 76,156 complete two-packet graphs.

In all cases the exact independence number is at least

```text
|V_1|+|V_2|-m_1-m_2-|I|.
```

The bound is exact in 3,766 cases and strict in 72,390 cases; the largest observed
slack is four. This confirms that the interface certificate is safe but can be
conservative when one deletion covers several internal and interface conflicts.

## Evidence boundary

This theorem converts local Hall certificates into an asymptotic packet template,
but it does not construct the packets. A coordinate host must still supply actual
motif resource lists, internal bipartite degree-two centre graphs, certified
interface edge bounds, and both source- and host-defect restrictions.
