# Full-selector normal form and universal `2 x 3 -> 6` closure

PX49 closes the arbitrary-map one-inner-layer route through base side eight.  The
next larger state space is the complete four-layer factor-product host with an
arbitrary spanning degree-two selector.

For the canonical side-two outer factor, arbitrary block maps admit a concise
normal form.  Unlike PX39, the selected inner layer is no longer fixed; the full
host remembers one conjugacy class of the inner factor.

## 1. Block permutation notation

Let the inner factor be

\[
(\tau_0,\tau_1)
\]

on `[n]`.  Let `alpha_0,alpha_1` be the fine-row digit permutations in the two
coarse row blocks, and let `beta_0,beta_1` be the corresponding fine-column digit
permutations.

Inside coarse block `(i,j)`, inner layer `s` is the graph of

\[
g_{ijs}
=
\beta_j\tau_s\alpha_i^{-1}.
\]

Define four permutations

\[
T=\beta_0\tau_0\alpha_0^{-1},
\]

\[
P=\alpha_0\alpha_1^{-1},
\qquad
Q=\beta_1\beta_0^{-1},
\]

and

\[
H=\alpha_0\tau_0^{-1}\tau_1\alpha_0^{-1}.
\]

Composition is read from right to left.

## Theorem PX50 -- PROVED

For every choice of factor and block maps,

\[
\boxed{
 g_{ijs}=Q^j T H^s P^i
}
\qquad(i,j,s\in\{0,1\}).
\]

Conversely, fix the inner factor and let

\[
h=\tau_0^{-1}\tau_1.
\]

Every quadruple `(T,P,Q,H)` with `T,P,Q` arbitrary and `H` conjugate to `h` is
realized by suitable block maps.  Consequently, under arbitrary blockwise digit
permutations, the scalar geometry of the complete four-layer host depends on the
inner factor only through the conjugacy class, equivalently the cycle type, of
its relative permutation `h`.

### Proof

The four displayed identities follow by substitution.  For example,

\[
THP
=
\beta_0\tau_0\alpha_0^{-1}
\alpha_0\tau_0^{-1}\tau_1\alpha_0^{-1}
\alpha_0\alpha_1^{-1}
=
\beta_0\tau_1\alpha_1^{-1}
=
g_{101}.
\]

Left multiplication by `Q` gives the corresponding `j=1` blocks.  The other
cases are immediate.

For the converse, choose `gamma` with

\[
H=\gamma h\gamma^{-1}.
\]

Set

\[
\alpha_0=\gamma,
\qquad
\alpha_1=P^{-1}\gamma,
\]

\[
\beta_0=T\gamma\tau_0^{-1},
\qquad
\beta_1=Q\beta_0.
\]

These maps recover the prescribed `T,P,Q,H`. \(\square\)

## Corollary PX50a -- PROVED

Two inner factors whose relative permutations have the same cycle type have
exactly the same family of scalar four-layer hosts after arbitrary blockwise
digit permutations.  Any degree-two selector certificate for one factor
therefore transports literally to the other.

This reduces a factor-by-factor full-selector closure problem to one problem per
relative cycle type.

## 2. The side-three relative class

Take the canonical side-three factor

\[
\tau_0=(0,2,1),
\qquad
\tau_1=(1,0,2).
\]

Its relative permutation is

\[
H_*=\tau_0^{-1}\tau_1=(2,0,1),
\]

a 3-cycle.  Use identity block maps and orientation `cf`.  The resulting host
contains the spanning degree-two state

```text
(0,1) (0,3) (1,1) (1,5) (2,3) (2,5)
(3,0) (3,2) (4,0) (4,4) (5,2) (5,4)
```

It decomposes into the permutation layers

\[
\pi_0=(1,5,3,0,4,2),
\]

\[
\pi_1=(3,1,5,2,0,4).
\]

Every row and column contains exactly two points, and every one of the

\[
\binom{12}{3}=220
\]

integer determinants is nonzero.

## Theorem PX51 -- PROVED

Every saturated no-three side-three factor composes with the saturated side-two
factor to the displayed saturated no-three side-six configuration, using
arbitrary blockwise digit permutations and the exact full degree-two selector.
Equivalently,

\[
\boxed{2\times3\longrightarrow6}
\]

is a factor-independent full-selector closure statement.

### Proof

Let `(tau_0,tau_1)` be any saturated side-three factor.  Rowwise disjointness
implies that

\[
h=\tau_0^{-1}\tau_1
\]

has no fixed point.  Every derangement of three symbols is a 3-cycle, so `h` is
conjugate to `H_*`.

Choose `gamma` satisfying

\[
\gamma h\gamma^{-1}=H_*.
\]

Let

\[
T_*=(0,2,1)
\]

and choose the same row map in both coarse row blocks,

\[
\alpha_0=\alpha_1=\gamma,
\]

and the same column map in both coarse column blocks,

\[
\beta_0=\beta_1=T_*\gamma\tau_0^{-1}.
\]

Theorem PX50 gives

\[
T=T_*,
\qquad
P=Q=\operatorname{id},
\qquad
H=H_*.
\]

Hence the transported scalar host is literally the canonical host above.  The
same twelve selected scalar cells therefore give the same no-three degree-two
state. \(\square\)

## 3. Algorithmic form

Given a side-three factor:

1. compute `h=tau_0^{-1} tau_1`;
2. enumerate the six permutations `gamma` until
   `gamma h gamma^{-1}=H_*`;
3. set both row maps to `gamma`;
4. set both column maps to `T_* gamma tau_0^{-1}`;
5. output the twelve fixed scalar cells above.

The map search is constant-size and the output is explicit.

## 4. Verification

Run

```bash
python scripts/verify_product_full_host_normal_form.py
```

The verifier:

- checks the PX50 identity for all `6^6=46,656` side-three tuples of two factor
  permutations and four block maps;
- enumerates all four ordered saturated side-three factors;
- constructs the transporting maps for each factor;
- checks literal equality with the canonical scalar host;
- verifies degree two in every row and column and all 220 nonzero determinants.

## 5. Updated closure boundary

The branch now has factor-independent special products

\[
2\times2\to4,
\qquad
2\times3\to6,
\qquad
2\times4\to8,
\qquad
2\times5\to10.
\]

The side-three result is qualitatively different from the side-four and
side-five results: PX49 proves that no one-inner-layer template exists at base
three, while PX51 succeeds by selecting both inner layers nontrivially in the
full host.

The next full-selector target is to classify relative cycle types that occur in
side-six, side-seven, and side-eight factors and determine whether each type has
a successful `(T,P,Q,H)` host and degree-two selector.  This remains finite and
structural progress, not an infinite multiplicative closure theorem.
