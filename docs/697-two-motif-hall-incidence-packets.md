# Two-motif Hall incidence packets

This chapter intersects the exact transfer formalism of `docs/688` with the
source/host degree-two defect model of `docs/682`. The result is a complete finite
classification of the smallest motif-compatible packet: two selected motifs,
six centres, two left ports, two right ports, and two internal centres.

## PP3dex — Exact incidence-realizable packet class

A source-defect assignment of load at most two is a partition of the six labelled
centres into singleton and two-element classes. There are exactly 76 such
partitions. The same count holds for the host-defect assignment, so the complete
labelled incidence census contains

```text
76 * 76 = 5,776
```

source/host tables.

The centre-conflict graph is the union of the source-sharing edges and the
host-sharing edges. Each edge set is a matching. Conversely, every simple graph
whose connected components are paths and even cycles is the union of two
matchings, by alternating the two edge colours on every component. Therefore the
incidence-realizable six-centre graphs are exactly the unions of two matchings.

After deduplication, precisely 1,636 of the `2^15=32,768` labelled simple graphs on
six centres are realizable. Their edge-count histogram is

```text
0:1, 1:15, 2:105, 3:375,
4:675, 5:405, 6:60.
```

Thus a coordinate search does not need to consider arbitrary packet graphs: it
must realize one of these 1,636 exact defect-incidence types.

## PP3dey — Exact transfer rates and Hall thresholds

For every realizable graph, use two left ports, two right ports, and the matching
interface conflicts from each right port to the corresponding next left port.
Compute the exact boundary-state transfer matrix from `docs/688`.

The one-packet independence-number histogram is

```text
3:660, 4:900, 5:75, 6:1.
```

The reachable maximum cycle-mean histogram is

```text
3:1059, 10/3:16, 7/2:120, 4:441.
```

The exact least number of repeated packets needed to retain at least 28 centres
has histogram

```text
7:441, 8:120, 9:415, 10:660.
```

In particular every degree-two two-motif packet has positive exact transfer
rate, and 441 packet types reach the Hall target in seven repeats.

## PP3dez — Direct-chain verification and explicit defect template

`scripts/check_hall_two_motif_incidence_packets.py` constructs all 1,636 graphs,
computes their transfer recurrences, and compares each value with a direct maximum
independent set for one through four packets:

```text
1,636 * 4 = 6,544
```

exact chain comparisons. Every comparison agrees.

Against the safe charge of both interface edges at every join, exact transfer is
strictly better in 4,866 comparisons, with maximum improvement six at four
packets.

A smallest strict template uses centres

```text
L0,L1,R0,R1,I0,I1.
```

Take two abstract resource-disjoint motifs

```text
M0 = {L0,R0,I0},
M1 = {L1,R1,I1}.
```

Let `L0,L1` share one source-defect label and give every other source label and all
six host labels independently. The only internal conflict is `L0--L1`. Exact
retained counts for one through seven packets are

```text
5,9,13,17,21,25,29.
```

Hence exact transfer reaches 28 in seven packets. Uniform two-edge interface
charging gives `3K+2` and first reaches 28 at nine packets.

## Evidence boundary

This is a complete combinatorial packet template: motif membership, resource
disjointness interface, source/host labels, boundary ports, internal conflicts,
and periodic transfer are explicit. It is not yet a coordinate packet. Promotion
still requires actual coordinate motifs realizing one audited incidence table and
showing that periodic translation creates exactly the two declared interface
conflicts and no others.

The all-`n` theorem remains open, and the next theorem identifier is `PP3dfa`.
