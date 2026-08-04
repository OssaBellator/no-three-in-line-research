# Hall packet transfer matrix

`docs/682` gives a safe additive interface charge for concatenated Hall packets.
This chapter records the exact finite-state alternative: retain the boundary
occupancy pattern and compose packets by max-plus dynamic programming.

## PP3ddw — Exact boundary-state transfer matrix

Fix one packet centre-conflict graph with labelled left boundary `L` and right
boundary `R`. For subsets `A subseteq L` and `B subseteq R`, define

```text
W[A,B]
```

as the maximum size of an independent set inside one packet whose selected left
and right boundary vertices are exactly `A` and `B`.

When consecutive packets are joined by matching interface conflicts, a previous
right state `C` is compatible with a current left state `A` exactly when

```text
C intersect A = emptyset.
```

Therefore the exact max-plus transition matrix is

```text
M[C,B] = max_{A: C intersect A = emptyset} W[A,B].
```

Let

```text
v[B] = max_A W[A,B]
```

for the first packet. The exact retained-centre count for a chain of `K>=1`
identical packets is

```text
alpha_K = max_B (v tensor M^(K-1))[B],
```

where `tensor` denotes max-plus multiplication. This formula charges an interface
conflict only when the two adjacent boundary states actually select both
endpoints.

## PP3ddx — Periodic asymptotic retention rate

The state graph of `M` is finite. Restrict it to states reachable from `v`. The
asymptotic retained-centre density per packet is the maximum cycle mean

```text
lambda(M) = max_cycle (sum transition weights)/(cycle length).
```

Consequently

```text
alpha_K = K*lambda(M) + O(1).
```

The exact least packet count reaching the 28-centre Hall target is obtained by the
same finite recurrence. This can be strictly smaller than the packet count from
subtracting every interface edge independently.

The theorem applies without a degree-two assumption once the one-packet table
`W` is available. Degree-two defect incidence remains useful because it makes
`W` and the packet boundary small and coordinate-auditable.

## PP3ddy — Exhaustive five-vertex packet audit

`scripts/check_hall_packet_transfer_matrix.py` exhausts all `2^10=1,024` simple
packet graphs on two left ports, two right ports, and one internal vertex. It
compares the transfer recurrence with a direct maximum-independent-set computation
for one through four copies:

```text
1,024 * 4 = 4,096
```

exact chain checks.

The transfer value agrees with the direct independence number in every case. The
exact recurrence strictly improves on charging both interface edges independently
in 3,060 checks, with maximum improvement six at four copies.

The maximum cycle-mean histogram over the 1,024 packets is

```text
3:381, 5/2:115, 7/3:22, 2:503, 3/2:2, 1:1.
```

For the smallest recorded strict Hall-threshold example, the packet has one
internal edge between its two left ports. Its one-packet independence number is
four and its exact asymptotic rate is three. The transfer recurrence reaches 28
centres in nine packets, while the uniform two-edge interface charge requires
thirteen.

## Evidence boundary

This is an exact periodic-packet interface, not a coordinate packet construction.
Promotion still requires explicit motif resource lists, source/host defect labels,
packet boundaries, and a repeatable geometric embedding realizing the transfer
states.
