# Exact lattice capacity sharpens the cross-line pair envelope

Define for primitive height `h>=1`

\[
q_n(h)=\left\lfloor\frac{n-1}{h}\right\rfloor,
\qquad
c_n(h)=\max\{q_n(h)-1,0\}.
\]

A line through a fixed owner has at most `q_n(h)` other board cells.

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
\frac12
\sum_{\substack{b\in E_a(R)\\a,b\text{ nonaxis}}}c_n(h(a,b)).
}
\]

### Proof

On a line of height `h`, use CMR1438 and CMR1446 with
`q=q_n(h)`, then sum the exact line formula CMR1422. ∎

## Exact conditional capacity star

Define

\[
\mathscr C_e(a)=
\sum_{\substack{b\in O\\a,b\text{ nonaxis}}}c_n(h(a,b))
+
\frac1{p_e(a)}
\sum_{\substack{b\in E(H_e)\setminus\{a\}\\
                 \{a,b\}\text{ compatible}\\a,b\text{ nonaxis}}}
p_e(a,b)c_n(h(a,b)).
\]

### Theorem CMR1448 -- PROVED

Conditioned on `a in R`,

\[
\boxed{
\mathbb E\left[
\sum_{\substack{b\in(O\cup R)\setminus\{a\}\\a,b\text{ nonaxis}}}
 c_n(h(a,b))\ \middle|\ a\in R
\right]=\mathscr C_e(a).}
\]

### Proof

The fixed part is deterministic; each response partner has conditional
probability `p_e(a,b)/p_e(a)`. ∎

### Theorem CMR1449 -- PROVED

\[
\boxed{g_e(a)\le\Gamma_e^{\rm cap}(a):=\frac12\mathscr C_e(a).}
\]

### Proof

Condition CMR1447 on `a`, enlarge to all selected partners, and apply CMR1448.
∎

### Theorem CMR1450 -- PROVED

\[
\boxed{\Gamma_e^{\rm cap}(a)\le\Gamma_e^{\rm harm}(a).}
\]

### Proof

Termwise,

\[
c_n(h)\le\frac{n-1}{h}.
\]

Compare the two exact conditional pair sums. ∎

### Theorem CMR1451 -- PROVED

If

\[
h>\frac{n-1}{2},
\]

then `c_n(h)=0`.  Hence the capacity envelope has no contribution from such
pairs.

### Proof

The hypothesis gives `floor((n-1)/h)<=1`. ∎

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

### Proof

Apply CMR1449 in CMR1426--CMR1427. ∎

For a dyadic band `H<=h<2H`, set

\[
c_{n,H}=\max\left\{\left\lfloor\frac{n-1}{H}\right\rfloor-1,0\right\}.
\]

### Theorem CMR1453 -- PROVED

For every pair in that band,

\[
0\le c_n(h)\le c_{n,H}.
\]

Thus exact pair counts multiplied by `c_{n,H}/2` give an honest owner upper
quotient.  Only bands with `H<=(n-1)/2` are nonzero.  This lattice-capacity
quotient strictly sharpens the harmonic relaxation.  No all-`n` theorem is
claimed.

Checked by
[`scripts/verify_prime_power_cross_line_lattice_capacity.py`](../scripts/verify_prime_power_cross_line_lattice_capacity.py).
