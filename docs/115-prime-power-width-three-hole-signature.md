# Width-three blockers reduce to seven-hole moment signatures

CMR285 extracts `t-9` pairwise disjoint full triples from every sufficiently
large sharp width-three Hall blocker. Since the large Hall side has size `t-2`,
those triples occupy all but seven Hall cells on each of the three small-side
slices. Collinearity imposes exact first- and second-moment relations on the
three omitted seven-sets. Thus the large width-three obstruction is a
constant-defect affine signature, independent of the parent block size.

Assume throughout this chapter that

\[
t\ge10.
\]

Smaller width-three parent blocks form a finite exceptional range. Assume first
that the smaller Hall side consists of three source coordinates

\[
x_1<x_2<x_3.
\]

The dual target-side statement follows by interchanging coordinates. Let `C` be
the large-side row set, so

\[
|C|=t-2.
\]

Put

\[
\lambda
=
\frac{x_3-x_2}{x_3-x_1},
\qquad
0<\lambda<1.
\]

## 1. Seven-hole extraction

### Theorem CMR288 — PROVED

Every sharp width-three blocker with `t>=10` contains a subfamily of exactly
`t-9` full available Hall lines which are pairwise disjoint as board cells.

For `i=1,2,3`, let `U_i` be the set of row coordinates used by this subfamily on
the slice `x=x_i`, and put

\[
R_i=C\setminus U_i.
\]

Then

\[
\boxed{|R_1|=|R_2|=|R_3|=7.}
\]

### Proof

CMR285 supplies at least `t-9` pairwise disjoint full triples. Retain exactly
`t-9` of them. On each of the three slices, disjointness gives `t-9` distinct
used cells from the common `(t-2)`-set `C`, leaving seven omitted coordinates.
Because `t>=10`, at least one retained line is present. ∎

## 2. Exact moment constraints

### Theorem CMR289 — PROVED

The seven-hole sets from CMR288 satisfy

\[
\boxed{
\sum_{r\in R_2}r
=
\lambda\sum_{r\in R_1}r
+(1-\lambda)\sum_{r\in R_3}r
}
\]

and

\[
\boxed{
\sum_{r\in R_2}r^2
\ge
\lambda\sum_{r\in R_1}r^2
+(1-\lambda)\sum_{r\in R_3}r^2.
}
\]

### Proof

For one retained line, let its three row coordinates be `a_1,a_2,a_3`. Since
the points are collinear,

\[
a_2
=
\lambda a_1+(1-\lambda)a_3.
\]

Sum over all retained lines. This gives

\[
\sum_{u\in U_2}u
=
\lambda\sum_{u\in U_1}u
+(1-\lambda)\sum_{u\in U_3}u.
\]

Since every `U_i` is the complement of `R_i` inside the same set `C`, the full
sum over `C` cancels and gives the first displayed identity.

Strict convexity of the square gives, line by line,

\[
a_2^2
\le
\lambda a_1^2+(1-\lambda)a_3^2.
\]

After summing and again subtracting from the common full second moment of `C`,
the inequality reverses on the omitted sets, proving the second statement. ∎

## 3. The hole signature is nonconstant

### Corollary CMR290 — PROVED

The three omitted sets cannot all be equal:

\[
\boxed{
(R_1,R_2,R_3)\ne(R,R,R)
}
\]

for every seven-set `R`.

### Proof

If all three hole sets were equal, then all three used sets would also be equal.
The second-moment inequality in the proof of CMR289 would be an equality. Since
it was obtained by summing nonnegative strict-convexity gaps, equality would
hold on every retained line. Thus every retained line would satisfy

\[
a_1=a_3,
\]

and would be horizontal. At least one retained line exists because `t>=10`.
Horizontal triples are incompatible with a matching board, a contradiction. ∎

## 4. Dual form and revised width-three endpoint

If the smaller Hall side consists of three target coordinates, interchange the
two board coordinates. The same seven-hole cardinality and moment constraints
hold for the omitted source coordinates.

A large sharp width-three blocker is therefore encoded by:

- three ordered Hall slices;
- three seven-element hole sets;
- one exact affine first-moment identity;
- one reverse second-moment inequality;
- and a nonconstant hole pattern.

The size-dependent part of the blocker has disappeared. The next width-three
conversion may treat the seven-hole signature by finite switching, inherited
prefix classification, or a carry charge attached to its moment discrepancy.
The range `t<10` remains finite and separate.

No all-`n` theorem is claimed here. The moment identities and an explicit
parallel-line family with seven holes per slice are checked in
[`scripts/verify_prime_power_width_three_holes.py`](../scripts/verify_prime_power_width_three_holes.py).
