# Old selected defects occupy only logarithmically many heavy product levels

PX221 refutes bounded packet count for unrestricted candidate support-four
energy. The obstruction uses every candidate cross in the packet grid. A repair
potential, however, is driven by defects present in the current selected
matching.

For one current perfect matching, selected crosses from a fixed product packet
are much sparser: they form disjoint transpositions. This gives an exact defect-
weighted decomposition and proves that every low-syndrome block has only
logarithmically many linearly heavy product levels.

Work in a packet subgrid of order `h`. Let `M` be the current selected perfect
matching. For an anchor-product level `alpha=(z,p)`, let `P_alpha` be its product
packet and let

\[
d_\alpha(M)
\]

be the number of packet-certified rank-two cross events contained in `M`.

## 1. Selected crosses inside one packet are disjoint

### Theorem PX223 -- PROVED

For every product packet `P_alpha`, the selected certified crosses contained in
`M` form a matching on the arcs of `P_alpha`. Consequently

\[
\boxed{
d_\alpha(M)
\le
\left\lfloor\frac{|P_\alpha|}{2}\right\rfloor
\le
\frac h2.
}
\]

Moreover, the old selected support-four collision count decomposes exactly as

\[
\boxed{
D_{2,4}(M)
=
\sum_\alpha d_\alpha(M),
}
\]

where the sum is anchor weighted: the same selected pair is counted once for
every background anchor completing it.

### Proof

Let two packet arcs be

\[
r\to a,
\qquad
s\to b.
\]

Their certified cross is selected exactly when

\[
M(r)=b,
\qquad
M(s)=a.
\]

Suppose two selected certified crosses shared the packet arc `r->a`. Pair it
first with `s->b` and then with `t->c`. The two cross events would require

\[
M(r)=b
\qquad\text{and}\qquad
M(r)=c.
\]

Since packet target columns are distinct, `b=c` forces the second packet arc to
be the same. Thus distinct selected crosses share no packet arc. They form a
matching and have size at most `floor(|P_alpha|/2)`.

Every old support-four collision through an anchor has one unique cross-product
value and hence belongs to one unique packet level for that anchor. Summing over
anchors and product values gives the decomposition. \(\square\)

This is the exact old-defect analogue of the candidate packet identity PX210.

## 2. Heavy-level concentration

For a threshold `tau>0`, call a product level `tau`-heavy when

\[
d_\alpha(M)\ge\tau.
\]

### Theorem PX224 -- PROVED

The number `k_tau` of `tau`-heavy product levels satisfies

\[
\boxed{
k_\tau
\le
\frac{D_{2,4}(M)}{\tau}.
}
\]

If

\[
D_{2,4}(M)
\le
C h\log h
\]

and `tau=eta h`, then

\[
\boxed{
k_\tau
\le
\frac C\eta\log h.
}
\]

Every joint release containing all `tau`-heavy packets removes all old defects
carried by those levels. The remaining old support-four defects are distributed
over product levels of load strictly less than `tau`.

### Proof

The heavy levels contribute at least `k_tau tau` to the exact sum in PX223.
Therefore

\[
k_\tau\tau
\le
D_{2,4}(M).
\]

Substitute the low-syndrome bound and `tau=eta h` for the logarithmic statement.
A joint release forbids every certified cross from every included packet, so no
old defect carried by a released heavy level survives. \(\square\)

### Corollary PX224a -- PROVED

Assume

\[
D_{2,4}(M)
\le
C h\log h
\]

and release every `eta h`-heavy packet. Then PX222 applies with

\[
\kappa=\frac C\eta.
\]

The joint release has polynomial density and polynomial fixed-rank cylinder
loss. In any support-excess sector `(r,u)`, square-root thinning still gives an
unconditioned power saving provided

\[
\boxed{
\frac C\eta<\frac{u-r}{8},
}
\]

or a conditioned power saving provided

\[
\boxed{
\frac C\eta<\frac{u-r}{16}.
}
\]

The inequalities are quantitative and may be too strong with the present crude
spread constants, but they give an exact interface between defect concentration
and packet release.

## 3. Heavy-versus-diffuse dichotomy

PX223--PX224 replace the false candidate-energy target by a correct selected-
defect dichotomy.

1. **Heavy regime.** Linearly loaded old-defect levels are only logarithmically
   numerous and can be included in one polynomial-spread release family.
2. **Diffuse regime.** Every remaining product level carries fewer than `eta h`
   old defects. A different decoder must exploit this dispersion.

The diffuse regime is now the genuine packet frontier. It may support:

- an averaging improvement over many low-load packets;
- a transposition decoder across packet levels;
- a potential charging each defect to a distinct anchor-product resource;
- extraction of a loaded line or clean star from cross-level overlap.

## 4. Improvement interface

Let `D_heavy` be the number of old defects carried by the released heavy packets.
Let `W_r^ext` be the remaining external rank-`r` candidate weights. PX218 and
PX224 imply strict improvement whenever

\[
\boxed{
D_{\rm heavy}
>
e^{4\Delta+4k_\tau}
\sum_{r=1}^3\frac{W_r^{\rm ext}}{(h)_r}.
}
\]

After exposure, use the conditioned `e^(4Delta+8k_tau)` constant. Thus all
probability and destruction terms are explicit; the remaining issue is geometric
control of the diffuse external weights.

## 5. Verification

Run

```bash
python scripts/verify_product_defect_heavy_packets.py
```

The verifier enumerates packet-certified crosses in random current permutations,
checks that selected crosses form disjoint packet-arc matchings, verifies the
exact anchor-product decomposition, tests the heavy-level counting inequality,
and confirms that joint release removes every selected cross from every included
heavy packet.
