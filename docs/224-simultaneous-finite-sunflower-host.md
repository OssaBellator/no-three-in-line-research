# Simultaneous finite-family sunflower host preparation

PP3amz--PP3anf give an exact transversal law for one fixed-core sunflower or
resource-disjoint signature bank.  A marked centre may carry several exceptional
support classes at once.  Because the number of canonical source and paid classes
is absolute, all their extracted pencils, sunflowers, and disjoint banks can be
removed simultaneously.

The argument has two parts.

1. A nonempty optional helper core is killed by omitting one core index.
2. After those omissions, every empty-core family is a matching of support sets of
   size at least two.  A uniform marked filler block contains a target support with
   total expectation `O(b^2/N)=o(1)`.

Thus one does not need a separate prepared host for each exceptional class.
Uniform marked single-cycle sampling already avoids every extracted geometry at
once, up to residual source or insertion load outside the chosen target families.

## 1. A finite collection of target families

Let `c` be the forced marked endpoint in a pool of `N` tied indices.  Let

```text
G_1,...,G_L
```

be target positive-support families, where `L` is bounded by an absolute constant.
For each `ell`, assume that all signatures in `G_ell` contain

```text
{c} union F_ell union P_(ell,j),
```

where:

1. `F_ell` is an optional fixed helper core, possibly empty;
2. the nonempty petals `P_(ell,j)` are pairwise disjoint as `j` varies;
3. if `F_ell` is empty, every petal has size at least two.

Different families may overlap arbitrarily.  Within one empty-core family, every
helper index belongs to at most one petal.

These hypotheses include:

- all fixed and nested partner pencils from PP3ame and PP3amh;
- all fixed-core high-support source sunflowers from PP3amv;
- all empty-core resource-disjoint binary or source-signature banks;
- any constant number of such families at the same marked centre.

## 2. Optional-core deletion

For every `ell` with `F_ell` nonempty, choose one index

```text
f_ell in F_ell.
```

Let `D` be the set of chosen indices, so `|D|<=L`.

### Proposition PP3ang -- PROVED

Every target signature belonging to a family with nonempty fixed core is absent
from every filler block contained in

```text
V\D.
```

#### Proof

The chosen index `f_ell` belongs to the support of every signature in `G_ell`.
Excluding it from the filler block makes every such signature impossible. ∎

Only empty-core disjoint-petal families remain.

## 3. Uniform marked-block support probability

Choose a uniform `(b-1)`-subset `I_0` of

```text
V\({c} union D),
```

and put `I={c} union I_0`.  Write

```text
N'=N-1-|D|.
```

### Proposition PP3anh -- PROVED

For a fixed empty-core petal `P` of size `s>=2`,

```text
Pr(P subseteq I_0)=(b-1)_s/(N')_s.
```

If one empty-core family has `H_s` petals of size `s`, its expected number of
fully selected target supports is

```text
H_s (b-1)_s/(N')_s.
```

#### Proof

This is the exact hypergeometric containment probability.  Sum the support
indicators inside one family. ∎

Because the petals in one family are disjoint,

```text
sum_s s H_s <= N'.
```

### Theorem PP3ani -- PROVED

The expected total number `X_tar` of selected target supports over all empty-core
families satisfies

```text
E X_tar
<=
L N' ((b-1)_2/(N')_2)
<=
2L b^2/N
```

for all sufficiently large `N` with `|D|=O(1)` and `b=o(N)`.

#### Proof

For `s>=2`, the containment probability is at most `(b-1)_2/(N')_2` after
forgetting the additional required vertices.  Each family has at most `N'`
petals, and there are at most `L` families.  This gives the first bound.  The
second is the elementary comparison `N'=N-O(1)`. ∎

The estimate does not require different exceptional classes to be disjoint from
one another.

## 4. Active marked-filler scale

Use

```text
N=m^(19/20+o(1)),
b=m^(kappa+o(1)),
0<kappa<19/80.
```

### Corollary PP3anj -- PROVED

For every fixed `L`,

```text
E X_tar=O_L(b^2/N)=o(1).
```

#### Proof

The exponent of `b^2/N` is

```text
2kappa-19/20 < 19/40-19/20 = -19/40.
```

Apply PP3ani. ∎

Thus all empty-core target banks are simultaneously absent with probability
`1-o(1)` after the optional cores have been omitted.

## 5. Joint single-cycle paid criterion

After choosing the marked block, choose a uniform single-cycle state on its `b`
indices.  Let `R_c>0` be the exact marked removal credit.  Let `Z_res` be the
nonnegative objective consisting of:

1. every remaining source-invalid event outside the target families;
2. every remaining insertion cost divided by `R_c`.

### Theorem PP3ank -- PROVED / CONDITIONAL RESIDUAL-LOAD INTERFACE

Suppose

```text
E Z_res <= 1-tau
```

for one fixed `tau>0`.  For all sufficiently large `m`, one marked single-cycle
state:

1. contains none of the target pencil, sunflower, or disjoint-bank signatures;
2. is source-valid;
3. has insertion cost below `R_c`;
4. gives a strict paid improvement.

#### Proof

By PP3anj, eventually `E X_tar<tau`.  The nonnegative objective

```text
Z_res+X_tar
```

then has expectation below one.  In an outcome of value below one, the integer
target-support count and source-invalid count both vanish, while normalized
insertion cost is below one.  Apply PP3kx. ∎

No independence between the target classes is used.

## 6. Exact failure interpretation

### Corollary PP3anl -- PROVED

At a free or one-controller-punctured marked centre, a finite collection of
fixed/nested pencils, fixed-core source sunflowers, and resource-disjoint positive
signature banks has exactly one of the following outcomes.

1. Simultaneous marked single-cycle avoidance and strict paid completion.
2. Residual source-invalid expectation outside the target families reaches a fixed
   positive scale.
3. Residual insertion expectation outside the target families reaches the marked
   removal-credit scale.
4. A controller-pool, distinguished-endpoint, Hall, alternating, or other external
   host condition fails.

The support geometries themselves cannot be the reason the marked host fails.

#### Proof

Apply PP3ang--PP3ank.  Negating the residual-slack hypothesis produces items 2 or
3; any failure before the source/paid calculation is item 4. ∎

## 7. Revised marked-host frontier

### Corollary PP3anm -- PROVED

The first live object in PP3amy is removed: fixed-resource and nested-resource
pencils and fixed-core source-invalid sunflowers admit one uniform simultaneous
host law.  The remaining marked-centre frontier is now:

1. residual source or insertion collateral outside the extracted target families
   already at the marked credit scale;
2. external endpoint-host or controller-pool compatibility failure;
3. controller-puncture reserve exhaustion;
4. branches requiring one-step monotone potential descent rather than the paid or
   robust final-state alternatives.

The no-three-in-line conjecture remains unproved.