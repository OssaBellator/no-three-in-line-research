# Exact lattice capacity sharpens the cross-line pair envelope

CMR1398--CMR1405 bound owner collateral by harmonic pair energy.  The proof
used the real-valued estimate `(n-1)/h` for the number of possible cells beyond
an owner edge.  Retaining the integer board capacity gives a strictly sharper
pairwise envelope and removes all directions which cannot contain a third
board cell.

For a primitive height `h>=1`, define

\[
q_n(h)=\left\lfloor\frac{n-1}{h}\right\rfloor
\]

and

\[
\boxed{c_n(h)=\max\{q_n(h)-1,0\}.}
\]

Thus a line through a fixed owner contains at most `q_n(h)` other board cells,
and `c_n(h)=0` exactly when it cannot contain two such cells.

## One-line capacity inequality

### Theorem CMR1406 -- PROVED

For integers `0<=z<=q`,

\[
\boxed{
\binom z2\le\frac{q-1}{2}z.
}
\]

### Proof

`z-1<=q-1`, so `z(z-1)/2<=z(q-1)/2`. ∎

The bound is exact at `z=0`, `z=1` and `z=q` when `q=1` or `z=q`.

## Realized owner bound

Use the eligible set `E_a(R)` from CMR1399.

### Theorem CMR1407 -- PROVED

For every entering owner `a`,

\[
\boxed{
\gamma_e(a,R)
\le
\frac12
\sum_{\substack{b\in E_a(R)\\a,b\text{ nonaxis}}}
c_n(h(a,b)).
}
\]

### Proof

On a line of height `h`, CMR1398 gives `z_L<=q_n(h)`.  Apply CMR1406 with
`q=q_n(h)` and sum over the lines through `a`.  Each eligible cell contributes
once with coefficient `c_n(h)`. ∎

Unlike the first harmonic envelope, a singleton-capacity line contributes
zero.

## Exact conditional capacity star

Define

\[
\mathscr C_e(a)
=
\sum_{\substack{b\in O\\a,b\text{ nonaxis}}}
c_n(h(a,b))
+
\frac1{p_e(a)}
\sum_{\substack{b\in E(H_e)\setminus\{a\}\\
                 \{a,b\}\text{ compatible}\\
                 a,b\text{ nonaxis}}}
p_e(a,b)c_n(h(a,b)).
\]

### Theorem CMR1408 -- PROVED

Conditioned on `a in R`,

\[
\boxed{
\mathbb E
\left[
\sum_{\substack{b\in(O\cup R)\setminus\{a\}\\a,b\text{ nonaxis}}}
 c_n(h(a,b))
\ \middle|\ a\in R
\right]
=
\mathscr C_e(a).
}
\]

### Proof

The fixed `O` part is deterministic.  A response edge `b` has conditional
probability `p_e(a,b)/p_e(a)`.  Sum its capacity coefficient. ∎

All probabilities are exact rook values.

## Closed lattice-capacity owner weight

### Theorem CMR1409 -- PROVED

\[
\boxed{
 g_e(a)
\le
\Gamma_e^{\rm cap}(a)
:=\frac12\mathscr C_e(a).
}
\]

### Proof

Condition CMR1407 on `a in R`, enlarge the eligible set to all selected cells,
and use CMR1408. ∎

## Comparison with the harmonic envelope

### Theorem CMR1410 -- PROVED

For every allowed edge,

\[
\boxed{
\Gamma_e^{\rm cap}(a)
\le
\Gamma_e^{\rm harm}(a).
}
\]

### Proof

For every height `h`,

\[
c_n(h)
=\max\left\{\left\lfloor\frac{n-1}{h}\right\rfloor-1,0\right\}
\le\frac{n-1}{h}.
\]

Compare the fixed and conditional pair sums term by term, then multiply by
one half. ∎

The inequality is often strict, especially near the high-height cutoff.

## Exact height cutoff

### Theorem CMR1411 -- PROVED

If

\[
h>\frac{n-1}{2},
\]

then

\[
\boxed{c_n(h)=0.}
\]

Hence the lattice-capacity owner envelope has no contribution from such
pairs.  Every unresolved pair direction satisfies

\[
\boxed{h\le\left\lfloor\frac{n-1}{2}\right\rfloor.}
\]

### Proof

The hypothesis gives `floor((n-1)/h)<=1`, so `q_n(h)-1<=0`. ∎

This removes the high-height tail entirely rather than merely bounding it.

## Assignment certificate

### Theorem CMR1412 -- PROVED

If rational potentials satisfy

\[
\alpha_x+\beta_y\ge\Gamma_e^{\rm cap}(x,y)
\]

on every allowed edge, then

\[
\boxed{
\mathbb E N(R)\le\sum_x\alpha_x+\sum_y\beta_y.
}
\]

If this sum is below `D_S(e)`, a strict improvement exists.  The exact host
penalty of CMR1396 applies in a restricted host.

### Proof

Use CMR1409 in the assignment theorem CMR1386--CMR1387. ∎

## Dyadic capacity bands

For dyadic `H`, define

\[
c_{n,H}=\max\left\{\left\lfloor\frac{n-1}{H}\right\rfloor-1,0\right\}.
\]

### Theorem CMR1413 -- PROVED

For every pair with `H<=h<2H`,

\[
0\le c_n(h)\le c_{n,H}.
\]

Thus exact pair counts in one height/signature band multiplied by `c_{n,H}/2`
give an honest owner-weight upper quotient.  Only bands with
`H<=(n-1)/2` are nonzero.

### Proof

The floor function `floor((n-1)/h)` is nonincreasing in `h`.  Apply the class
maximum and CMR1329. ∎

## Lattice-capacity endpoint

The complete owner envelope now uses only:

1. exact rank-one and rank-two rook probabilities;
2. primitive heights of owner--partner pairs;
3. the integer coefficient `c_n(h)`;
4. one bipartite assignment dual.

It strictly dominates the previous harmonic relaxation and has finite support
in primitive height.  The remaining low-height task is to exploit first
separation, projective direction, prefix and carry structure inside these
nonzero capacity bands.  No all-`n` theorem is claimed.

The capacity inequalities and exact conditional envelopes are checked in
[`scripts/verify_prime_power_cross_line_lattice_capacity.py`](../scripts/verify_prime_power_cross_line_lattice_capacity.py).
