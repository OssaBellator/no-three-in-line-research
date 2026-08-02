# Multiplicity-two case-zero orientation-three semantic cover core

PX1007--PX1009 show that stored seven-triple bottom covers induce partial-top
nogoods by fixing only the columns occurring syntactically in the cover. This
chapter semantically minimizes one especially small pair of covers: top order
`35` of multiplicity-two case zero in orientation three.

The two selectors have greedy seven-triple covers with syntactic support masks

- selector zero: `11531`, size `7`;
- selector one: `9503`, size `8`.

Every deletion test enumerates all clean top assignments extending the remaining
literals and rechecks the stored seven triples against all `5,040` bottom
permutations.

## 1. Selector-level semantic deletion

### Theorem PX1010 -- PROVED FINITE

For selector zero, column zero may be deleted from the seven-column syntactic
support. The resulting semantic mask is

\[
\boxed{11530}
\]

with size `6`. It has four clean top extensions, and the stored cover remains a
full bottom-permutation cover for all four.

Every attempted deletion from this six-column mask fails:

| Deleted column | Candidate size | Clean extensions | First failure after checked extensions |
|---:|---:|---:|---:|
| 1 | 5 | 11 | 1 |
| 3 | 5 | 7 | 3 |
| 8 | 5 | 8 | 2 |
| 10 | 5 | 12 | 1 |
| 11 | 5 | 5 | 5 |
| 13 | 5 | 12 | 1 |

For selector one, columns zero, one, and two may be deleted successively from
the eight-column syntactic support. The resulting semantic mask is

\[
\boxed{9496}
\]

with size `5`. It has five clean top extensions, and the stored cover remains a
full bottom-permutation cover for all five.

Every attempted deletion from this five-column mask fails:

| Deleted column | Candidate size | Clean extensions | First failure after checked extensions |
|---:|---:|---:|---:|
| 3 | 4 | 72 | 1 |
| 4 | 4 | 25 | 1 |
| 8 | 4 | 10 | 2 |
| 10 | 4 | 18 | 1 |
| 13 | 4 | 20 | 1 |

Thus the fixed covers have deletion-minimal semantic supports of sizes six and
five.

## 2. Two-selector master nogood

### Theorem PX1011 -- PROVED FINITE

The union of the two semantic support masks is

\[
11530\mathbin{\mathrm{OR}}9496
=
\boxed{11546},
\]

which has exactly seven fixed top columns.

There are four clean top assignments extending this pair mask. For each
extension, both stored covers remain valid across every bottom permutation. The
verifier therefore checks exactly

\[
4\cdot2\cdot5040=\boxed{40{,}320}
\]

bottom obligations.

The exact final transcript is:

```text
FINAL case=0 orientation=3 top_index=35 selector0_mask=11530 selector1_mask=9496 pair_mask=11546 pair_size=7 clean_extensions=4 top_nodes=15 tested_bottoms=40320 digest=2649867520580673397 PASS
```

Hence one seven-literal partial-top assignment refutes both selectors
simultaneously across four complete top orders.

## 3. Master-learning consequence

### Corollary PX1012 -- PROVED REDUCTION

For these fixed seven-triple covers, mask `11546` is an inclusion-minimal
pair-cover master nogood under the deterministic deletion order: removing any
literal belonging exclusively to either minimized selector support invalidates
that selector cover on a clean extension.

The certificate consists of:

- one multiplicity-two signature;
- two selector states;
- two stored seven-triple covers;
- seven top literals;
- four clean extensions;
- the exact 40,320 cover checks.

This replaces four independent shared-bottom DFS calls by one compact partial-top
proof object. It is the first exact semantic bridge from bottom-cover
compression to two-selector master learning at multiplicity two.

The result is cover-relative: another choice of seven triples could admit a
smaller semantic support. No global minimum over all possible covers is claimed.

## 4. Next target

The next proof-compression step is to run this semantic deletion procedure over
the repeated support-mask and cover classes in the 64-top orientation-three
prefix. The objective is to build a small library of partial-top master nogoods
whose clean-extension families cover a large fraction of all top orders in the
signature.

This finite certificate result does not advance the selector census boundary
and does not prove an infinite product theorem.

## 5. Verification

```bash
python scripts/verify_product_side_seven_multiplicity2_case0_orientation3_semantic_cover_core.py
```

The verifier recompiles the semantic minimizer, regenerates both covers, replays
every deletion test, asserts the exact extension and bottom-check counts, and
checks the final ordered digest.
