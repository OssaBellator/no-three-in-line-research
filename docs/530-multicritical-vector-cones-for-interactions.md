# Multi-critical vector cones for interactions

`docs/524` proves eventual vector translation when one interaction block has
strictly smallest mean work. If several blocks tie, the minimum-work frontier
can grow with the side length. The correct replacement is a finite residue
corrector joined to a Minkowski power of the critical vector set.

A macro block `i` has positive integer length `ell_i`, rational work `w_i`, and
nonnegative rational secondary vector `v_i`. Assume all critical blocks have a
common length `L` and common mean work `mu`, while every noncritical block has
strictly positive reduced work `w_i-mu ell_i`.

## 1. Scalar residue stabilization with ties

### Theorem PP3clq -- PROVED / MULTI-CRITICAL WORK QUASIPOLYNOMIAL

For every attainable residue `r mod L`, there are a finite reduced-work excess
`eta_r` and threshold `N_r` such that

```text
W(N)=mu N+eta_r
```

for every sufficiently large attainable `N` in residue `r`.

#### Proof

Every noncritical block has positive reduced work, so a minimum-excess residue
corrector contains only a bounded number of them. Critical blocks have zero
reduced work and common length `L`; they can be removed while searching the
finite corrector set and appended afterward without changing the residue or
excess. ∎

## 2. Exact Minkowski-power frontier

### Theorem PP3clr -- PROVED / TIED-CRITICAL VECTOR FRONTIER

Let `A={v_i : i critical}`. For each residue `r`, let `C_r` be the finite set of
minimum-excess correctors. For sufficiently large `N=Lk+r`, the complete
minimum-work secondary frontier is

```text
Pareto union_(C in C_r)
    (v_C + A^(oplus (N-ell_C)/L)),
```

where `A^(oplus m)` is the `m`-fold Minkowski sum of the critical vectors.

#### Proof

The scalar argument bounds all noncritical content and leaves a corrector plus
critical blocks. Every such concatenation has minimum work, and every
minimum-work schedule has this form. Secondary vectors add under
concatenation, giving the stated union; Pareto pruning removes exactly the
irrelevant tradeoffs. ∎

## 3. Critical vector polytope and finite audit

### Theorem PP3cls -- PROVED / MULTI-CRITICAL CONE CERTIFICATE

After division by `N`, the frontiers in `PP3clr` converge to the convex hull of
`{v_i/L : i critical}` with `O(1/N)` residue and lattice error. A finite dynamic
program on length, reduced work, and Pareto vectors certifies the corrector sets
and reconstructs every extremal word.

#### Proof

An `m`-fold Minkowski average of the finite set `A` lies in its convex hull, and
rational convex combinations are approximated by integer multiplicities with
bounded rounding error. The corrector contributes only a bounded vector, hence
`O(1/N)` after normalization. Positive noncritical reduced work makes the
corrector search finite. ∎

## 4. Stored exact fixture

The audit `scripts/check_multicritical_interaction_cones.py` uses

```text
P: length 2, work 2, vector (2,0),
Q: length 2, work 2, vector (0,2),
R: length 1, work 2, vector (1,1).
```

`P` and `Q` tie at mean work one. Through length 200,

```text
W(N)=N     for even N,
W(N)=N+1   for odd N.
```

For `N=2k`, the frontier is

```text
{(2i,2(k-i)) : 0<=i<=k};
```

for `N=2k+1`, it is

```text
{(2i+1,2(k-i)+1) : 0<=i<=k}.
```

Thus the frontier has size `floor(N/2)+1` and converges to
`conv((1,0),(0,1))`. It cannot be represented by translating one fixed finite
residue set, demonstrating the necessity of `PP3clr`.

## 5. Prime-patching consequence

The integration layer can now preserve all secondary tradeoffs even when
several periodic correction modes are equally efficient. The asymptotic object
is a finite critical polytope, while every finite side is recovered by exact
Minkowski powers and residue correctors.
