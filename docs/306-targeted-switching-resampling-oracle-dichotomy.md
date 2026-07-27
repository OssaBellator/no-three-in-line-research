# Targeted switching and the exact resampling-oracle dichotomy

The Hamilton switching kernel has two attractive but incompatible properties in
its present form.  Without flaw-dependent targeting it preserves the uniform
signed Hamilton measure exactly.  When targeted at a present strongly generic
bad triple it removes that triple with certainty.  This chapter records why the
same targeted rule cannot also be a standard exact resampling oracle.

## 1. Guaranteed deletion versus exact measure restoration

Let `mu` be a probability measure on a finite state space and let `A` be an event
with `mu(A)>0`.  A standard exact resampling oracle for `A` is required to map an
input distributed as `mu` conditioned on `A` back to the unconditional measure
`mu`.

### Proposition PP3bju -- PROVED

No randomized map `R_A` can simultaneously satisfy

```text
X distributed as mu conditioned on A  =>  R_A(X) distributed as mu
```

and

```text
R_A(x) not in A for every x in A and every internal random choice.
```

#### Proof

The second property gives

```text
Pr(R_A(X) in A)=0.
```

The first property gives

```text
Pr(R_A(X) in A)=mu(A)>0,
```

a contradiction. ∎

The observation is elementary, but it distinguishes exact resampling from
guaranteed flaw elimination.

## 2. Application to the Hamilton repair kernel

### Corollary PP3bjv -- PROVED / ORACLE BARRIER

Fix a strongly generic selected collinear triple `T` in the uniform signed
Hamilton measure.  The targeted support-three successor rotation of PP3bjk,
with any distribution on the eight new sign choices, is not a standard exact
resampling oracle for the event

```text
A_T = {T is selected}.
```

#### Proof

PP3bjk proves that every targeted outcome removes all three old orbit blocks and
therefore lies outside `A_T`.  PP3bjc gives `mu(A_T)>0`.  Apply PP3bju. ∎

Thus an algorithm using certain deletion must be analysed as a flaw walk,
switching process, partial rejection scheme, or nonstationary repair process,
not by directly asserting the usual exact-oracle restoration axiom.

## 3. Stationarity-targeting dichotomy

### Theorem PP3bjw -- PROVED / FRONTIER SHARPENED

For the current support-three kernel:

1. choosing the source triple independently of the current defects and choosing
   fresh signs uniformly yields the symmetric reversible kernel of PP3bjj;
2. this unconditioned kernel has zero stationary drift for every potential by
   PP3bjm;
3. choosing a present bad triple as the source set destroys that flaw by PP3bjk;
4. the targeted kernel is not an exact resampling oracle by PP3bjv and may
   increase every natural raw defect potential by PP3bjo.

Hence measure preservation, guaranteed single-flaw deletion, and pointwise
potential descent are not simultaneously supplied by the present rule. ∎

## 4. Remaining resampling routes

The barrier is specific to an oracle that both restores the exact base measure
and guarantees deletion.  It leaves several viable alternatives:

1. permit the resampled flaw to recur with controlled probability, restoring an
   exact or approximate stationary measure;
2. use a nonexact flaw-walk theorem based on charges or witness sequences;
3. enlarge the resampled block so that collateral defects are included in the
   flaw definition;
4. alternate targeted and unconditioned switchings to combine deletion with
   mixing;
5. analyse a deliberately biased stationary measure rather than the uniform
   Hamilton measure.

The next oracle-level task is therefore not to relabel the current targeted move
as an exact resampler, but to prove a charge, commutativity, regeneration, or
approximate-restoration property strong enough for termination.
