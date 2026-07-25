# Sub-target cascade termination at a target-scale alternating cycle

PP3ais--PP3aix give an exact monotone coordinate for the canonical marked
source-star cascade: the number of rows on which the active permutation layer
differs from its original reference. A single-cycle seed creates one defect
cycle, and every fresh-helper generation lengthens that same cycle by `q-1`.

This chapter combines the defect growth with the controller-domain scale

```text
R=m^(19/20+o(1)),
W=sqrt(R)=m^(19/40+o(1)).
```

The consequence is a finite-horizon termination theorem. For any divergent
`q=o(W)`, the cascade either completes or encounters a marked-host/base-domain
obstruction within `O(W/q)=o(W)` generations, or it reaches one explicit
alternating cycle of length `Theta(W)`. Thus unbounded generation count is no
longer independent of the alternating-host frontier.

## 1. Exact hitting time for a defect threshold

Fix a constant `alpha>0`. Start with a single-cycle seed of size `q` and continue
with fresh-helper single-cycle moves of the same size. Let

```text
S_t=|D(M_t)|=q+(t-1)(q-1).
```

### Proposition PP3aiy -- PROVED

Let `t_alpha` be the first generation with

```text
S_t >= alpha W.
```

If `q=o(W)`, then

```text
t_alpha <= 1+alpha W/(q-1)=O(W/q)=o(W)
```

and

```text
alpha W <= S_(t_alpha) < alpha W+q
                         =(alpha+o(1))W.
```

#### Proof

The defect grows by exactly `q-1` after the seed. Solve the displayed arithmetic
progression for the first crossing. Minimality gives the overshoot bound. ∎

Hence the canonical process reaches every fixed sub-square-root defect fraction
in sub-target many generations.

## 2. Binary final shadow still fits a fixed margin

Fix a controller-domain margin `xi R`, with `xi>0`, and choose

```text
0<alpha<min{sqrt(xi/8),xi/4}.
```

### Proposition PP3aiz -- PROVED

At the first `alpha W` crossing,

```text
S_t(S_t-1) <= (alpha^2+o(1))R < xi R/4.
```

Thus all final binary insertion shadow of the defect state consumes less than one
quarter of the available robust domain margin.

#### Proof

Use `S_t=(alpha+o(1))W`, `W^2=R`, and the chosen bound on `alpha`. Apply the final
binary support estimate PP3aic. ∎

No sum of intermediate binary costs appears.

## 3. Direct completion or a target-size final star

Assume the final retained-original base domains have size at least
`(gamma+xi)R`, satisfy the global allocation criterion, and include all nonshadow
source, transition, and anchor exclusions.

### Theorem PP3aja -- PROVED / CONDITIONAL DIRECT-ALLOCATION INTERFACE

At the first `alpha W` crossing, at least one of the following occurs.

1. Final unary support together with the binary term fits `xi R`, and the patch
   completes directly.
2. A final paired domain falls below `gamma R`. Then some point of the defect
   cycle is the centre of a final source-star fibre of size

   ```text
   C > 3 xi R/(8S_t)=Omega(W).
   ```

   With the displayed choice `alpha<xi/4`, the fibre contains more than one
   target-width substar for all sufficiently large `m`.
3. The nonshadow base margin or global allocation criterion fails.
4. A marked source, transition, anchor, conditional-Hall, alternating-host, or
   distinguished endpoint-host obstruction prevents construction of the path.

#### Proof

PP3aiz reserves at most `xi R/4` for binary support. If a margin-compatible
domain still fails, more than `3xi R/4` unary values were removed. Split them
among movement/refill type and the `S_t` final new points. PP3aho gives one fibre
larger than `3xi R/(8S_t)`. Since `S_t=(alpha+o(1))W` and `R=W^2`, this is
`(3xi/(8alpha)+o(1))W`, which exceeds `W` under `alpha<xi/4`. The direct case is
PP3aie. ∎

The next-generation star is supported by the final source and every one of its
centres is free by PP3aiv.

## 4. The boundary is one alternating cycle

### Proposition PP3ajb -- PROVED

Under the canonical single-cycle cascade, the relative permutation at the first
`alpha W` crossing has one nontrivial cycle `Gamma` of length

```text
|Gamma|=S_t=(alpha+o(1))W.
```

The symmetric difference `M_0 triangle M_t` is therefore one alternating cycle
of length `2S_t=Theta(W)`.

#### Proof

The seed has one nontrivial relative cycle by PP3ait, and PP3aiu preserves the
number of nontrivial cycles while adding `q-1` vertices to that cycle. Apply
PP3aiy for its final length. ∎

Thus a cascade that does not complete or expose a host failure reaches a concrete
target-scale alternating object, not an undefined long iteration.

## 5. Exact two-state reference-oscillation variable

On the rows of `Gamma`, define two matching states:

```text
state 0: use the original edges of M_0,
state 1: use the current edges of M_t.
```

Outside `Gamma`, the two layers agree.

### Proposition PP3ajc -- PROVED

The two states use the same row and column margins and are the two perfect
matchings of the cycle graph `M_0 union M_t` on `Gamma`.

If the cascade changed no other permutation layer, state zero restores the
original source and state one is the current source; both extreme states are
source-valid. Every hybrid obstruction involving additional allowed host edges
is an exact alternating finite-state source/anchor/shadow condition of rank at
most three.

#### Proof

An even cycle has exactly its two alternating perfect matchings. The source
claims are the definitions of the original and current states. Any forbidden
triple uses at most three selected matching edges, while a blocker-pair shadow
uses at most two. ∎

This is the minimal **reference-oscillation core**. If the ambient endpoint host
contains more alternating cycles or chords, it feeds the cycle-bank,
mobility-hub, and theta-state localizations PP3um--PP3vf. Without those extra
states it remains an explicit two-state alternating obstruction rather than an
unbounded cascade.

## 6. Finite-horizon cascade endpoint

### Theorem PP3ajd -- PROVED / CONDITIONAL FRESH-HELPER CASCADE INTERFACE

Fix `alpha` as above and a divergent marked size `q=o(W)`. Suppose the canonical
fresh-helper single-cycle host can be prepared successively while the defect is
below `alpha W`.

Within `O(W/q)=o(W)` generations, one of the following occurs.

1. Robust final allocation completes the patch.
2. A marked source, transition, anchor, Hall, alternating-host, or distinguished
   endpoint-host certificate prevents the next move.
3. The nonshadow base-domain margin or global allocation criterion fails.
4. The active layer reaches a single alternating defect cycle of length
   `Theta(W)` and final unary failure supplies another free target-size source
   star on that cycle.
5. The same target-scale cycle is a reference-oscillation core requiring an
   alternating-cycle/chord conversion.

#### Proof

Use PP3aiy for the horizon, PP3aiz--PP3aja for the final domain dichotomy, and
PP3ajb--PP3ajc for the exact boundary object. ∎

## 7. Revised termination frontier

### Corollary PP3aje -- PROVED

Under fresh-helper single-cycle preparation, proving an a priori termination
bound for an abstract source-star cascade is no longer a separate task. The
cascade has an exact increasing defect coordinate and reaches its complete
finite-horizon endpoint after `o(W)` generations.

The remaining work is now one of:

1. uniform preparation of the fresh-helper marked hosts;
2. nonshadow base-domain/global-allocation failure;
3. direct treatment of the target-scale reference-oscillation cycle;
4. conversion of that cycle through additional alternating host states, hubs, or
   theta paths;
5. a branch that cannot preserve the original reference layer or cannot choose
   untouched original helpers.

No completion of the no-three-in-line conjecture is claimed.
