# Collinear-background normal form for the side-four hard-core exchange

## Scope

CMR2722--CMR2751 identify one scalar hard-core exchange functional, prove the sharp two-point threshold for its strict `Q4` chamber, and classify every legal two-point background. This chapter extends the scalar calculation to **every finite collinear outside-grid background**.

The executable checker is:

```text
python scripts/check_prime_power_hard_core_collinear_backgrounds.py
```

The result is finite selector geometry. It does not identify genuine recurrence fibres, labelled child states, routed credits, return/interface rows or recurrent contraction. It permanently reports:

```text
all_n_proved_by_checker = 0
```

## CMR2752--CMR2761

### CMR2752 — arbitrary-background pair-potential decomposition

Let `B` be a finite set of distinct integer points outside the side-four response grid. Retain the four relevant lines

\[
K_-:x-y-1=0,
\quad
K_+:x+y-3=0,
\quad
K_{30}:3x+y-3=0,
\quad
K_{03}:x+3y-9=0.
\]

Define the point weight

\[
\omega(x)
=
3\mathbf 1_{K_-}(x)
-5\mathbf 1_{K_+}(x)
+\mathbf 1_{K_{30}}(x)
+\mathbf 1_{K_{03}}(x).
\]

Let

\[
P_1=(3,2),\quad P_2=(1,0),
\qquad
N_1=(3,0),\quad N_2=(1,2),
\]

and for distinct points `u,v` define

\[
\chi(u,v)
=
\mathbf 1_{P_1,u,v\text{ collinear}}
+
\mathbf 1_{P_2,u,v\text{ collinear}}
-
\mathbf 1_{N_1,u,v\text{ collinear}}
-
\mathbf 1_{N_2,u,v\text{ collinear}}.
\]

Then the hard-core exchange difference is exactly

\[
\boxed{
\Delta(B)
=
\sum_{\{u,v\}\in\binom{B}{2}}\chi(u,v)
+
\sum_{x\in B}\omega(x)
-3.
}
\]

#### Proof

Each gauge-reduced rank-one pair count is a sum over unordered background pairs. The signed four-pivot combination therefore contributes the first sum. The four rank-two line occupancies contribute the point-weight sum, and the rank-three response difference contributes `-3`. ∎

### CMR2753 — collinear compression

Assume every point of `B` lies on one line `L`. Define its pivot balance

\[
\beta(L)
=
\#\{P_1,P_2\in L\}
-
\#\{N_1,N_2\in L\}.
\]

Every unordered pair of distinct points in `B` determines the same line `L`, so

\[
\chi(u,v)=\beta(L)
\]

for every pair. If `m=|B|`, then

\[
\boxed{
\Delta(B)
=
\beta(L)\binom m2
+
\sum_{x\in B}\omega(x)
-3.
}
\]

This is the collinear-background normal form.

### CMR2754 — exact pivot-balance census

The four relevant lines have balances

```text
beta(K_minus) =  2
beta(K_30)    =  1
beta(K_03)    =  1
beta(K_plus)  = -2
```

A line containing exactly one positive pivot and no negative pivot has balance `1`. A line containing exactly one negative pivot and no positive pivot has balance `-1`. A line containing no pivot, or one positive and one negative pivot, has balance `0`.

These are the only possible balance values:

\[
\boxed{\beta(L)\in\{-2,-1,0,1,2\}.}
\]

### CMR2755 — pure `K_minus` polynomial

Let `B` consist of `m` legal distinct points on `K_-`. Every point has weight `3`, and `beta(K_minus)=2`. Hence

\[
\Delta(B)
=
2\binom m2+3m-3
=
\boxed{(m-1)(m+3)}.
\]

Therefore

```text
m=0: Delta=-3
m=1: Delta= 0
m>=2: Delta>0
```

and the exact strict-`Q4` threshold on `K_-` is two points.

### CMR2756 — pure positive unit-line polynomials

Let `B` consist of `m` legal distinct points on `K_30` or on `K_03`. Every legal point has weight `1`: all intersections with the other relevant lines lie inside the forbidden response grid. Each line contains exactly one positive pivot and no negative pivot, so its balance is `1`.

Consequently

\[
\Delta(B)
=
\binom m2+m-3
=
\boxed{\frac{(m-2)(m+3)}2}.
\]

Thus

```text
m<=1: Delta<0
m=2:  Delta=0
m>=3: Delta>0
```

and the exact strict-`Q4` threshold on either positive unit-weight line is three points.

### CMR2757 — pure `K_plus` polynomial

Let `B` consist of `m` legal distinct points on `K_+`. Every point has weight `-5`, and `beta(K_plus)=-2`. Therefore

\[
\Delta(B)
=
-2\binom m2-5m-3
=
\boxed{-(m+1)(m+3)}.
\]

This is strictly negative for every `m>=0`. A pure `K_+` background never selects `Q4`.

### CMR2758 — clean pivot pencils

Call a collinear background **clean** when none of its points lies on any of the four relevant lines.

For a clean background of `m` points on a line containing exactly one positive pivot and no negative pivot,

\[
\boxed{\Delta=\binom m2-3.}
\]

Hence strict `Q4` occurs exactly when `m>=4`.

For a clean background on a line containing exactly one negative pivot and no positive pivot,

\[
\boxed{\Delta=-\binom m2-3<0.}
\]

For a clean background on a pivot-neutral line,

\[
\boxed{\Delta=-3.}
\]

Thus clean negative and neutral pencils never select `Q4`.

### CMR2759 — exact collinear threshold table

The pure and clean families have the following strict-`Q4` thresholds:

| Supporting-line family | Exact delta | Least `m` with `Delta>0` |
|---|---:|---:|
| `K_minus` | `(m-1)(m+3)` | `2` |
| `K_30` | `(m-2)(m+3)/2` | `3` |
| `K_03` | `(m-2)(m+3)/2` | `3` |
| clean positive-pivot line | `m(m-1)/2-3` | `4` |
| `K_plus` | `-(m+1)(m+3)` | never |
| clean negative-pivot line | `-m(m-1)/2-3` | never |
| clean neutral line | `-3` | never |

This reveals three distinct mechanisms for collinear strict-`Q4` pressure:

1. double positive-pivot support on `K_-`;
2. a positive-pivot line whose points also receive unit line weight;
3. a clean positive-pivot pencil with enough pair multiplicity to overcome the constant `-3`.

### CMR2760 — executable census, seal and corruption rejection

The checker verifies:

```text
32 named-line polynomial cases
24 clean-pencil polynomial cases
7,442 bounded collinear identities
8 rejected manifest corruptions
```

The bounded census uses every collinear prefix of size two through six arising from the outside-grid box `[-5,7]^2` and checks the direct pair-potential calculation against the compressed collinear formula.

The sealed manifest digest is

```text
3e818c8ece650173676e3afaa94b0adfb65fd0185146dc4b49485131a020c99a
```

The finite census is regression evidence. The collinear formula and polynomial thresholds follow symbolically from CMR2752--CMR2759 and are not restricted to the tested box.

### CMR2761 — T21 consequence and honesty boundary

The scalar hard-core frontier now has an exact arbitrary-cardinality theorem for every collinear survivor background. A genuine recurrence fibre that is proved collinear can be evaluated using only:

1. its supporting line's four-pivot balance;
2. its point count;
3. the finite set of points lying on the four relevant lines.

No pair-by-pair selector reconstruction is then necessary.

This does **not** prove that genuine recurrence backgrounds are collinear, identify their supporting lines, establish the required destroyed-threshold or labelled-child consequences, or prove return, interface or recurrent-contraction semantics. All twenty host-labelled T21 chamber arguments remain open, and the no-three-in-line conjecture remains open.
