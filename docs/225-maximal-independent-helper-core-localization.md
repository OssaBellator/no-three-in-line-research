# Maximal-independent helper sets localize residual support

PP3ang--PP3anm remove every finite collection of already extracted pencils,
sunflowers, and disjoint support banks under residual slack.  The remaining source
or positive-insertion support need not initially arrive in one of those forms.
This chapter gives a deterministic reduction for the complete residual support
union.

Choose a maximal set of helper indices containing no residual positive support.
If it has the required filler size, it is already a support-free marked host.  If
it is too small, every outside helper completes a forbidden support with a bounded
subset of the maximal set.  Pigeonholing the bounded support rank gives one fixed
core with almost linearly many variable extensions.

With an adaptive subpolynomial filler size, the extension family has size
`N^(1-o(1))`, far above the patch width.  Thus diffuse residual support cannot be
the reason a marked host fails.  Failure is a near-linear fixed-core pencil, a
residual weight carried on support-free states, or an external endpoint-host
condition.

## 1. Residual helper-support hypergraph

Fix a marked centre `c` in a tied pool of `N` indices.  After fixing the typed role
of `c`, let

```text
H_res
```

be the simple family of all nonempty helper-index supports of residual positive
source-invalid or insertion signatures.  Count each support once, regardless of
weight or witness multiplicity.

Assume every support has size at most the absolute constant `k_0`.  In the current
marked single-cycle normal form one may take `k_0<=5`.

A helper set `I` is **support-independent** when it contains no member of `H_res`.
If `I` is support-independent, then every marked state whose helper block is
contained in `I` avoids the complete residual positive support.

## 2. Maximal independent-set completion records

Let `I` be an inclusion-maximal support-independent helper set and put `t=|I|`.
For every helper index `v` outside `I`, maximality supplies at least one support

```text
E_v in H_res
```

such that

```text
v in E_v subseteq I union {v}.
```

Put

```text
F_v=E_v\{v} subseteq I.
```

Then `|F_v|<=k_0-1`.

### Proposition PP3ann -- PROVED

There are an integer `s` with `1<=s<=k_0`, a fixed set

```text
F subseteq I,
|F|=s-1,
```

and at least

```text
(N-1-t) /
[sum_(r=0)^(k_0-1) binom(t,r)]
```

distinct outside helper indices `v` for which

```text
F union {v} in H_res.
```

#### Proof

Assign every outside index `v` one completion record `F_v`.  There are at most

```text
sum_(r=0)^(k_0-1) binom(t,r)
```

possible records.  Pigeonhole one record `F`; all assigned outside indices are
distinct extensions of that fixed core. ∎

This is a simple fixed-core singleton-petal pencil.  The case `F=empty` is a set
of forbidden individual helpers.

## 3. Required-size dichotomy

Fix a desired helper count `b-1`.

### Theorem PP3ano -- PROVED

Exactly one of the following is available.

1. A support-independent helper set of size `b-1`.
2. A fixed residual support core `F` of size at most `k_0-1` with at least

   ```text
   (N-b) /
   [sum_(r=0)^(k_0-1) binom(b-2,r)]
   ```

   distinct variable extensions.

#### Proof

Take an inclusion-maximal support-independent set `I`.  If `|I|>=b-1`, retain any
`b-1` of its indices.  Otherwise `t<=b-2`; apply PP3ann and bound the number of
possible completion records using `t<=b-2`.  Also `N-1-t>=N-b`. ∎

No density, regularity, or random selection hypothesis is used.

## 4. Adaptive subpolynomial filler size

The marked filler size may be chosen to diverge more slowly than every prescribed
positive power of `N`; this only improves the source-thinning, selected-credit
trace, and final binary-support estimates.

Take

```text
b=N^(o(1)),
b->infinity.
```

### Corollary PP3anp -- PROVED

In the second alternative of PP3ano, the fixed-core extension family has size

```text
N^(1-o(1)).
```

At the slab scale

```text
N=m^(19/20+o(1)),
W=m^(19/40+o(1)),
```

this is `omega(W)`.

#### Proof

For fixed `k_0`,

```text
sum_(r=0)^(k_0-1) binom(b-2,r) <= k_0 b^(k_0-1)=N^(o(1)).
```

Insert this into PP3ano.  Since `19/20>19/40`, the extension family dominates
`W`. ∎

Thus failure of a support-free helper block is an almost-linear pencil, not a
moderate-density core.

## 5. Support-free single-cycle host

Assume the first alternative of PP3ano.  Choose any support-independent set `I_0`
of size `b-1`, adjoin the marked centre, and choose a uniform single-cycle state
on

```text
I={c} union I_0.
```

### Theorem PP3anq -- PROVED / CONDITIONAL RESIDUAL-WEIGHT INTERFACE

Every positive residual source or insertion signature represented in `H_res` is
absent from every state on `I`.  If the remaining support-free source-invalid
expectation plus normalized insertion weight is below one, some single-cycle
state is source-valid and has insertion cost below the marked removal credit.

#### Proof

A selected residual signature would have all its helper indices in `I_0`,
contradicting support independence.  The paid conclusion is the usual nonnegative
first-moment argument followed by PP3kx. ∎

Support multiplicity has disappeared completely; only weight on deterministic or
support-free residual terms remains.

## 6. Near-linear pencil interpretation

In the second alternative, after pigeonholing the finite canonical source/paid
class, the typed role of the fixed core, and the arc orientation, there are

```text
N^(1-o(1))
```
positive signatures sharing one fixed helper core and differing in one variable
helper index.

### Proposition PP3anr -- PROVED

The resulting family is one of the following.

1. A near-complete unary helper exclusion when `F=empty`.
2. A fixed-resource positive pencil when `|F|=1`.
3. A nested fixed-resource pencil of depth at most `k_0-1` when `|F|>=2`.

Its variable extension set has size `N^(1-o(1))`; all event weight or retained-
witness multiplicity is attached to these distinct positive supports and is not
part of the support count.

#### Proof

The fixed completion record supplies the core, and the outside indices supplied
by PP3anp are distinct singleton petals.  Pigeonholing finitely many canonical
classes and typed roles loses only a constant factor. ∎

This is substantially sharper than the `omega(W)` sunflower output PP3amv.

## 7. Revised residual-support endpoint

### Corollary PP3ans -- PROVED

For an adaptive marked filler size `b=N^(o(1))`, residual positive support at a
free or punctured marked centre has exactly one of the following forms.

1. A support-independent helper block gives complete positive-support avoidance
   and reduces the trade to support-free residual weight.
2. A near-linear fixed or nested helper pencil with `N^(1-o(1))` distinct variable
   extensions exists.
3. An external controller-pool, distinguished-endpoint, Hall, alternating, or
   source-host condition prevents use of the selected helper block.

Diffuse residual support and an intermediate-density exceptional-centre table are
no longer separate cases.

### Corollary PP3ant -- PROVED

The marked-centre frontier after PP3anm is narrowed to:

1. geometric conversion or algebraic exclusion of a near-linear terminal pencil;
2. insertion or deterministic source weight remaining after complete positive-
   support avoidance;
3. external endpoint-host failure;
4. controller-puncture reserve exhaustion or branches requiring one-step monotone
   potential descent.

The no-three-in-line conjecture remains unproved.