# Exact lattice capacity sharpens the cross-line pair envelope

Fix an inherited owner with matching side `d` and ambient coordinate span
`W_omega` from CMR1438.  For primitive height `h>=1`, define

\[
q_\omega(h)=\left\lfloor\frac{W_\omega}{h}\right\rfloor,
\qquad
c_\omega(h)=\max\{q_\omega(h)-1,0\}.
\]

A line through a fixed owner contains at most `q_omega(h)` other cells of the
inherited coordinate set.

### Theorem CMR1446 -- PROVED

For integers `0<=z<=q`,

\[
\boxed{\binom z2\le\frac{q-1}{2}z.}
\]

### Proof

Use `z-1<=q-1`. ∎

### Theorem CMR1447 -- PROVED

For every entering owner,

\[
\boxed{
\gamma_e(a,R)
\le
\frac12\sum_{\substack{b\in E_a(R)\\a,b\text{ nonaxis}}}
c_\omega(h(a,b)).}
\]

### Proof

On a line of height `h`, CMR1438 gives `z<=q_omega(h)`.  Apply CMR1446 and sum
CMR1422. ∎

Define

\[
\mathscr C_e(a)=
\sum_{\substack{b\in O\\a,b\text{ nonaxis}}}c_\omega(h(a,b))
+
\frac1{p_e(a)}
\sum_{\substack{b\in E(H_e)\setminus\{a\}\\
\{a,b\}\text{ compatible}\\a,b\text{ nonaxis}}}
p_e(a,b)c_\omega(h(a,b)).
\]

### Theorem CMR1448 -- PROVED

Conditioned on `a in R`,

\[
\boxed{
\mathbb E\left[
\sum_{\substack{b\in(O\cup R)\setminus\{a\}\\a,b\text{ nonaxis}}}
 c_\omega(h(a,b))\ \middle|\ a\in R
\right]=\mathscr C_e(a).}
\]

### Proof

The fixed part is deterministic and a response partner has conditional
probability `p_e(a,b)/p_e(a)`. ∎

### Theorem CMR1449 -- PROVED

\[
\boxed{g_e(a)\le\Gamma_e^{\rm cap}(a):=\frac12\mathscr C_e(a).}
\]

### Proof

Condition CMR1447 on `a`, enlarge to all selected partners, and use CMR1448.
∎

### Theorem CMR1450 -- PROVED

\[
\boxed{\Gamma_e^{\rm cap}(a)\le\Gamma_e^{\rm harm}(a).}
\]

### Proof

Termwise,

\[
c_\omega(h)\le\frac{W_\omega}{h}.
\]

Compare the exact conditional pair sums. ∎

### Theorem CMR1451 -- PROVED

If

\[
h>\frac{W_\omega}{2},
\]

then `c_omega(h)=0`.  Thus the capacity envelope has no contribution from such
directions.

### Proof

The hypothesis gives `floor(W_omega/h)<=1`. ∎

### Theorem CMR1452 -- PROVED

If rational potentials satisfy

\[
\alpha_x+\beta_y\ge\Gamma_e^{\rm cap}(x,y),
\]

then

\[
\boxed{\mathbb E N(R)\le\sum_x\alpha_x+\sum_y\beta_y.}
\]

A dual sum below `D_S(e)` forces improvement, with the CMR1436 host penalty in
a restricted host.

For a dyadic band `H<=h<2H`, put

\[
c_{\omega,H}=
\max\left\{\left\lfloor\frac{W_\omega}{H}\right\rfloor-1,0\right\}.
\]

### Theorem CMR1453 -- PROVED

For every pair in the band,

\[
0\le c_\omega(h)\le c_{\omega,H}.
\]

Exact pair counts multiplied by `c_{omega,H}/2` give an honest owner upper
quotient.  Only bands with `H<=W_omega/2` are nonzero.  The result applies to
scattered inherited factors because `W_omega`, not the matching side `d`,
controls geometry.  No all-`n` theorem is claimed.

Checked in the full-grid specialization by
[`scripts/verify_prime_power_cross_line_lattice_capacity.py`](../scripts/verify_prime_power_cross_line_lattice_capacity.py).
