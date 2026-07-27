# Multiplicity-two case-zero orientation-three cover compression through 64 top orders

PX997--PX999 show that the first eight orientation-three top orders of
multiplicity-two case zero have uniform seven-triple covers for both selectors.
This chapter extends the same exact measurement through the first 64 clean top
orders.

The experiment checks

\[
64\cdot2=\boxed{128}
\]

selector/top obligations and all

\[
128\cdot5040=\boxed{645{,}120}
\]

bottom-permutation incidences represented by those obligations.

## 1. Uniform cover size

### Theorem PX1000 -- PROVED FINITE

Every one of the first 64 orientation-three top orders gives a seven-triple full
cover for each of the two selectors. Thus all 128 fixed-top selector obligations
are certified infeasible with exactly

\[
128\cdot7=\boxed{896}
\]

cover entries.

No obligation in this prefix requires an eighth triple.

## 2. Shared dictionary growth

### Theorem PX1001 -- PROVED FINITE

The cumulative dictionary sizes at selected top-order prefixes are:

| Top orders | Selector covers | Triple dictionary | Distinct cover dictionary |
|---:|---:|---:|---:|
| 8 | 16 | 19 | 10 |
| 16 | 32 | 23 | 22 |
| 32 | 64 | 41 | 45 |
| 48 | 96 | 51 | 77 |
| 64 | 128 | 55 | 93 |

The final ordered transcript digest is

`5859277578097176413`.

The triple dictionary has not saturated: it gains four triples between top
orders 48 and 64. Nevertheless, only 55 triples support all 896 cover entries,
and 93 stored covers serve 128 obligations.

## 3. Compression consequence

### Corollary PX1002 -- PROVED REDUCTION

For this orientation and prefix, a replay certificate may share:

- one 55-triple dictionary;
- 93 seven-triple cover lists;
- 128 cover identifiers;
- the 64 top assignments, one signature, and the two selector states.

Compared with 896 independent triple entries, dictionary sharing removes 841
repeated triple records before encoding cover identifiers. Complete-cover reuse
removes a further 35 repeated cover lists.

This supports an orientation-specific proof-object architecture in which the
bottom obstruction is stored once and top orders reference a small cover
vocabulary. It does not yet give a signature-level top nogood: the dictionary
still depends on the exposed top assignment.

## 4. Next target

The next compression step is not merely a wider prefix. It is to deletion-minimize
top assumptions while replaying the stored seven-triple covers, so one cover can
be certified for every top order extending a partial assignment. That would
combine bottom-cover compression with the existing signature-level master-nogood
route.

This is a finite certificate result. It does not advance the selector census
boundary and does not prove an infinite product theorem.

## 5. Verification

```bash
python scripts/verify_product_side_seven_multiplicity2_case0_orientation3_bottom_cover64.py
```

The verifier regenerates all 128 covers, asserts that every cover has size seven,
checks cumulative dictionary and cover counts at five prefixes, and verifies the
ordered transcript digest.
