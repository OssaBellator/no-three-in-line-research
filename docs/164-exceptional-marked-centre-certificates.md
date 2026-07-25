# Exceptional marked-centre support certificates

PP3yp leaves one predetermined captive star centre as a possible exception to the
marked-filler resource-bank theorem. The exception is not qualitative. The marked
source and Xi first moments are sums of finitely many nonnegative support-ranked
terms. If no paid source-valid filler block exists at the centre, one term must be
large at an explicit scale.

This chapter records those scales and converts a fixed exceptional centre into a
finite list of local support-degree cores.

## 1. Marked centre data

Let the full controller pool have `N` endpoints, let the filler block have size
`b`, and fix the marked endpoint `c`.

Use the source degrees

```text
d_U(c)       unary source support degree,
d_tr(c)      anchored transition support degree,
D_P(c)       rank-four anchored-pair degree,
D_4(c)       rank-four inserted-triple degree,
D_5(c)       rank-five inserted-triple degree,
D_6(c)       rank-six inserted-triple degree.
```

Use the weighted Xi degrees

```text
D_A,1(c), D_A,2(c),
D_B,2(c), D_B,3(c), D_B,4(c).
```

Let `R_c>0` be the exact removal credit obtained when the trade moves `c`.

## 2. Normalized marked load

Ignoring fixed spread constants, define

```text
Lambda_src(c)
=
 d_U(c)/N
 + d_tr(c)/N^2
 + D_P(c)b/N^3
 + D_4(c)/N^3
 + D_5(c)b/N^4
 + D_6(c)b^2/N^5,
```

and

```text
Lambda_Xi(c)
=
 D_A,1(c)/b
 + D_A,2(c)/N
 + D_B,2(c)/(bN)
 + D_B,3(c)/N^2
 + D_B,4(c)b/N^3.
```

The unmarked filler terms are those in PP3xq, PP3xx, PP3yd, and PP3yk.

### Proposition PP3yq -- PROVED

If the unmarked source expectation is `o(1)` and the unmarked Xi cost is
`o(R_c)`, then a source-valid strict improvement exists whenever

```text
Lambda_src(c)+Lambda_Xi(c)/R_c < 1-o(1),
```

after restoring the fixed spread constants.

#### Proof

Add the marked terms from PP3xq, PP3xx, PP3yd, and PP3yk in one nonnegative
first-moment objective and apply PP3kx. ∎

## 3. Finite large-term certificate

There are eleven marked terms: six source terms and five Xi terms.

### Theorem PP3yr -- PROVED

Fix `rho>0`. Suppose the unmarked terms are negligible but the marked paid
criterion fails with margin at least `rho`. After passing to a subsequence, one of
the following holds with a fixed constant `c_rho>0`.

1. `d_U(c) >= c_rho N`.
2. `d_tr(c) >= c_rho N^2`.
3. `D_P(c) >= c_rho N^3/b`.
4. `D_4(c) >= c_rho N^3`.
5. `D_5(c) >= c_rho N^4/b`.
6. `D_6(c) >= c_rho N^5/b^2`.
7. `D_A,1(c) >= c_rho R_c b`.
8. `D_A,2(c) >= c_rho R_c N`.
9. `D_B,2(c) >= c_rho R_c bN`.
10. `D_B,3(c) >= c_rho R_c N^2`.
11. `D_B,4(c) >= c_rho R_c N^3/b`.

#### Proof

If every source term and every normalized Xi term were below `rho/22`, their sum
would be below `rho`. Restore fixed spread constants by reducing `c_rho`. ∎

Thus a captive centre cannot fail diffusely across many support ranks.

## 4. Correct local interpretations

### Proposition PP3ys -- PROVED

The source-unary alternative `d_U(c)=Omega(N)` is a genuine unary star at one of
the two typed resources of the marked endpoint and feeds PP3wf--PP3wg.

The rank-one Xi alternative is instead a local one-index state cost. In a strict
derangement it is absent; in a more general state family it must be paid or
removed locally.

The rank-two unary Xi alternative is a paid unary fibre through the marked
endpoint resources.

#### Proof

A support-rank-two unary cell contains the marked index and one other tied index,
so pigeonholing its typed side gives a resource star. Support rank one has no
second endpoint resource and is therefore a local state term rather than a star.
∎

### Proposition PP3yt -- PROVED

The rank-two binary Xi alternative is a concentrated two-index transposition-type
core. The rank-three and rank-four alternatives are genuine binary support cores
through the marked endpoint and may be subjected to resource star/matching,
conditional-Hall, and two-resource choice-grid reductions PP3wj--PP3xo.

#### Proof

A support-rank-two binary pattern uses the same two tied indices in both inserted
cells, so its geometry is a two-index exchange. Support ranks three and four
introduce additional endpoint resources and admit the standard binary resource-
incidence representation. ∎

## 5. Source-core role localization

For source alternatives 2--6, pigeonhole the role of `c` inside the support and,
for anchored patterns, the retained source anchor or witness-line type.

### Proposition PP3yu -- PROVED

Each source-core alternative contains a fixed-role subfamily of the same order up
to a constant factor:

- a transition core has predecessor, middle, or successor concentration;
- an anchored-pair core has one of four endpoint-index roles concentrated;
- a rank-`h` triple core has one of `h` endpoint-index roles concentrated.

#### Proof

There are at most three, four, or six roles respectively. Pigeonhole. ∎

This converts the certificate into an oriented algebraic counting problem with one
endpoint index fixed.

## 6. Slab-optimal scales

Use

```text
N=m^(19/20+o(1)),
b=m^(kappa+o(1)),
0<kappa<19/80.
```

### Corollary PP3yv -- PROVED

The marked source thresholds have exponents

```text
unary:          19/20,
transition:     19/10,
anchored pair:  57/20-kappa,
rank-4 triple:  57/20,
rank-5 triple:  19/5-kappa,
rank-6 triple:  19/4-2kappa.
```

The Xi thresholds are multiplied by the exact centre credit where displayed in
PP3yr.

#### Proof

Substitute the powers of `N` and `b`. ∎

The exponents are bookkeeping labels, not assertions that the cores exist.

## 7. Revised captive-centre endpoint

### Corollary PP3yw -- PROVED

A predetermined captive star centre has one of two forms.

1. It admits a marked filler block that is source-valid and has Xi-insertion cost
   below its concentrated star credit.
2. It carries one of the eleven explicit support-degree cores in PP3yr, with the
   corrected local interpretations PP3ys--PP3yt and role localization PP3yu.

Therefore an exceptional captive centre is no longer a qualitative frontier. The
remaining task is to convert the finite algebraic/geometric cores above.
