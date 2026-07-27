# Multiplicity-two case-zero eight-top bottom-cover compression

PX960--PX961 reduce one fixed-top bottom obstruction to explicit covers of all
`5,040` bottom permutations by collinear abstract edge triples. This chapter
measures the first eight clean top orders of multiplicity-two case zero in all
four radix orientations.

The experiment contains

\[
4\cdot8\cdot2=\boxed{64}
\]

selector/top obligations. Every obligation is independently covered and every
selected triple is rechecked by exact integer determinants.

## 1. Exact cover existence

### Theorem PX997 -- PROVED FINITE

For multiplicity-two case zero, each of the first eight clean top orders in each
of the four orientations gives a full bottom-permutation cover for both
selectors. Hence all 64 fixed-top selector obligations are infeasible without
calling the shared bottom DFS during certificate checking.

The deterministic greedy-cover size distributions are:

| Orientation | Cover-size distribution | Total entries |
|---:|---:|---:|
| 0 | `1 x 7`, `15 x 12` | 187 |
| 1 | `8 x 12`, `1 x 15`, `5 x 16`, `1 x 19`, `1 x 20` | 230 |
| 2 | `8 x 7`, `7 x 16`, `1 x 19` | 187 |
| 3 | `16 x 7` | 112 |
| **Total** | 64 covers | **716** |

Thus orientation three has a uniform seven-triple fixed-top certificate on this
prefix, while the other orientations require larger and more variable covers.

## 2. Dictionary and cover reuse

### Theorem PX998 -- PROVED FINITE

The exact shared dictionary census is:

| Orientation | Triple dictionary | Distinct cover dictionary | Digest |
|---:|---:|---:|---:|
| 0 | 57 | 16 | `5267506085810822176` |
| 1 | 59 | 16 | `2790833927980393128` |
| 2 | 60 | 16 | `17434165135039401592` |
| 3 | 19 | 10 | `5620182289796700611` |

Orientations zero, one, and two have no complete-cover repetition in the first
eight top orders. Orientation three reuses six complete covers and needs only 19
unique triples for all 112 cover entries.

### Corollary PX999 -- PROVED REDUCTION

Low-multiplicity proof compression is orientation-sensitive. A uniform raw-DFS
replacement should therefore store per-orientation triple dictionaries and
cover identifiers rather than enforce one common cover format.

For orientation three, the first eight-top prefix can be encoded by:

- 19 abstract triples;
- 10 ordered cover lists;
- 16 cover identifiers;
- the eight top assignments and one signature.

This is substantially smaller than storing 112 independent triples and much
smaller than enumerating all `16 x 5,040=80,640` selector-permutation
obligations directly.

## 3. Next compression target

A durable extension is measuring the first 64 orientation-three top orders.
The decisive question is whether the 19-triple dictionary and ten-cover family
saturate, grow sublinearly, or diversify with the top-order prefix.

The other immediate target is top-assumption minimization for multiplicity two,
so one stored cover family can discharge many top orders through a verified
master nogood.

This is a finite certificate-compression result. It does not advance the
selector classification boundary and does not prove an infinite product theorem.

## 4. Verification

```bash
python scripts/verify_product_side_seven_multiplicity2_case0_bottom_cover8.py
```

The verifier recompiles the generic cover generator, regenerates the exact
radius-three layer, measures all 64 obligations, asserts every cover-size
frequency, all four final dictionaries, and all four ordered transcript digests.
