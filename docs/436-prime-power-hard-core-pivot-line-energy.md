# Arbitrary-background pivot-line energy for the side-four hard core

## Scope

CMR2722--CMR2761 identify one scalar hard-core exchange functional, classify all legal two-point backgrounds and compress every collinear background. This chapter removes the collinearity hypothesis from the scalar calculation.

The executable checker is:

```text
python scripts/check_prime_power_hard_core_pivot_line_energy.py
```

The result applies to every finite set of distinct integer background points outside the side-four response grid. It is finite scalar-selector geometry. It does not identify genuine recurrence fibres, labelled child states, routed credits, return/interface rows or recurrent contraction. It permanently reports:

```text
all_n_proved_by_checker = 0
```

## CMR2762--CMR2771

### CMR2762 — pivot pencils and line multiplicities

Retain the two positive pivots

\[
P_1=(3,2),\qquad P_2=(1,0),
\]

and the two negative pivots

\[
N_1=(3,0),\qquad N_2=(1,2).
\]

For a pivot `p` and a finite legal background `B`, partition `B` by the line through `p`. If `n_{p,L}` is the number of points of `B` on a line `L` through `p`, define

\[
E_p(B)=\sum_{L\ni p}\binom{n_{p,L}}2.
\]

This counts the unordered background pairs whose joining line passes through `p`.

Put

\[
E_+(B)=E_{P_1}(B)+E_{P_2}(B),
\qquad
E_-(B)=E_{N_1}(B)+E_{N_2}(B).
\]

### CMR2763 — exact arbitrary-background energy identity

For the four relevant lines

\[
K_-:x-y-1=0,
\quad
K_+:x+y-3=0,
\quad
K_{30}:3x+y-3=0,
\quad
K_{03}:x+3y-9=0,
\]

define the point weight

\[
\omega(x)
=
3\mathbf 1_{K_-}(x)
-5\mathbf 1_{K_+}(x)
+\mathbf 1_{K_{30}}(x)
+\mathbf 1_{K_{03}}(x)
\]

and the total weight

\[
W(B)=\sum_{x\in B}\omega(x).
\]

Then for every finite legal background,

\[
\boxed{
\Delta(B)=E_+(B)-E_-(B)+W(B)-3.
}
\]

#### Proof

For each pivot `p`, every background pair collinear with `p` lies in exactly one pencil class `L` through `p`. The number of such pairs is therefore `E_p(B)`. The gauge-reduced rank-one part is the sum over the two positive pivots minus the sum over the two negative pivots. The four rank-two line occupancies contribute `W(B)`, and the rank-three exchange contributes `-3`. ∎

### CMR2764 — exact integer pressure criterion

All quantities in CMR2763 are integers. Since the deterministic selector chooses `Q4` exactly when `Delta>0`,

\[
\boxed{
Q_4\text{ is selected}
\iff
E_+(B)+W(B)\ge E_-(B)+4.
}
\]

Thus the arbitrary-background selector is an exact competition between positive-pivot pair concentration and point-line pressure on one side, and negative-pivot pair concentration plus the four-unit strict threshold on the other.

### CMR2765 — insertion and deletion marginal

Let `x` be a legal point not in `B`. Define

\[
\chi(x,y)
=
\mathbf 1_{P_1,x,y\text{ collinear}}
+
\mathbf 1_{P_2,x,y\text{ collinear}}
-
\mathbf 1_{N_1,x,y\text{ collinear}}
-
\mathbf 1_{N_2,x,y\text{ collinear}}.
\]

Only pairs containing `x` are created when `x` is inserted. Therefore

\[
\boxed{
\Delta(B\cup\{x\})-\Delta(B)
=
\omega(x)+\sum_{y\in B}\chi(x,y).
}
\]

The same expression, with the opposite sign, is the deletion marginal. This gives an exact local update rule for any genuine recurrence operation that inserts or removes one survivor point.

### CMR2766 — per-pivot convexity bound

Let `m=|B|`. For each pivot `p`, the pencil-class sizes form a partition of `m`, so

\[
0\le E_p(B)=\sum_L\binom{n_{p,L}}2\le\binom m2.
\]

The upper equality holds exactly when all background points lie in one pencil class through `p` (for `m>=2`). Consequently,

\[
0\le E_+(B),E_-(B)\le2\binom m2.
\]

Every legal point lies on at most one of the four relevant lines, because all pairwise intersections of those lines lie inside the forbidden response grid. Hence

\[
-5\le\omega(x)\le3
\]

and

\[
-5m\le W(B)\le3m.
\]

### CMR2767 — sharp global upper bound

Combining CMR2763 and CMR2766 gives

\[
\Delta(B)
\le
2\binom m2+3m-3
=
\boxed{(m-1)(m+3)}.
\]

For nonempty `B`, equality forces every point to have weight `3`, so every point lies on `K_-`. That line contains both positive pivots and neither negative pivot, so it also attains the two positive pencil maxima and zero negative energy.

Therefore

\[
\boxed{
\Delta(B)=(m-1)(m+3)
\iff
B\subseteq K_-
}
\]

for nonempty legal backgrounds. The empty background has `Delta=-3`, where the upper and lower formulas coincide.

### CMR2768 — sharp global lower bound

Similarly,

\[
\Delta(B)
\ge
-2\binom m2-5m-3
=
\boxed{-(m+1)(m+3)}.
\]

For nonempty `B`, equality forces every point to have weight `-5`, so every point lies on `K_+`. That line contains both negative pivots and neither positive pivot, attaining the two negative pencil maxima and zero positive energy.

Thus

\[
\boxed{
\Delta(B)=-(m+1)(m+3)
\iff
B\subseteq K_+
}
\]

for nonempty legal backgrounds.

### CMR2769 — exact cardinality interval and feasibility

Every legal background of size `m` satisfies the sharp interval

\[
\boxed{
-(m+1)(m+3)
\le
\Delta(B)
\le
(m-1)(m+3).
}
\]

Both endpoints are attained for every `m` by taking `m` distinct legal points on `K_+` or `K_-` respectively.

Consequently:

```text
m=0: Delta=-3 for the empty background
m=1: Delta<=0, so Q4 is impossible
m>=2: Q4 is realizable by any m legal points on K_minus
```

Hence the strict-`Q4` cardinality feasibility condition is exactly

\[
\boxed{Q_4\text{ is realizable at size }m\iff m\ge2.}
\]

This strengthens the earlier two-point witness into a sharp statement for every background cardinality.

### CMR2770 — executable exhaustive census and seal

The checker verifies:

```text
18 sharp extreme polynomial cases
284,274 exhaustive backgrounds of sizes zero through five
284,273 insertion/deletion marginal identities
22,159 strict-Q4 backgrounds in the bounded census
8 upper-equality cases and 4 lower-equality cases
8 rejected manifest corruptions
```

The exhaustive point set is

\[
[-2,4]^2\setminus\{0,1,2,3\}^2,
\]

which contains `33` legal points. Every subset of size at most five is checked against:

1. the direct pair-potential definition;
2. the pivot-line energy identity;
3. the sharp cardinality bounds;
4. the integer `Q4` pressure criterion;
5. the insertion/deletion marginal;
6. the equality-support characterization.

The sealed manifest digest is

```text
a88ddee378c70d2713734a836aa3c18683d6db193ebbb89d52921efa55efa4f3
```

The bounded census is regression evidence. CMR2762--CMR2769 are exact symbolic statements and are not restricted to the tested box.

### CMR2771 — T21 consequence and honesty boundary

The scalar side-four hard-core selector can now be evaluated for an arbitrary finite survivor background from four pivot-pencil partitions and four line occupancies. No collinearity assumption and no pair-by-pair response reconstruction are required.

For a genuine recurrence fibre, the remaining scalar work is reduced to proving its actual background point set and computing:

1. the two positive pivot energies;
2. the two negative pivot energies;
3. the four relevant-line occupancies.

The marginal identity also gives a direct way to propagate `Delta` through point insertions and deletions once those operations are proved to represent the genuine recurrence.

This does **not** identify any genuine recurrence background, prove that the documentary T03/T04 operations are mathematically correct, establish destroyed-threshold or labelled-child consequences, or prove return, interface or recurrent-contraction semantics. All twenty host-labelled T21 chamber arguments remain open, and the no-three-in-line conjecture remains open.
