# Typed-kernel load composition for frontier integration

The current prime-patching frontier uses several source-target kernels: direct-
clean repair policies, component-local recleaning choices, strict-repair words,
and adjacent clean-macro shell transitions.  Their relevant analytic quantity is
the maximum reverse-column load.  This chapter records the exact composition,
conditioning, and bounded-type-overlap calculus needed to combine the new
finite-type localizations without automatically paying for every type.

The statements are general interfaces.  They do not construct the required
prime-patching kernels.

## 1. Composition and mixtures

For a nonnegative row-stochastic kernel `P:X->Y`, write

```text
lambda(P)=max_(y in Y) sum_(x in X) P(x,y).
```

### Theorem PP3bwz -- PROVED / REVERSE-LOAD KERNEL CALCULUS

If `P:X->Y` and `Q:Y->Z` are row-stochastic, then

```text
lambda(PQ)<=lambda(P)lambda(Q).
```

If `P_i:X->Y` are row-stochastic and `alpha_i>=0` with `sum_i alpha_i=1`, then

```text
lambda(sum_i alpha_i P_i)
 <= sum_i alpha_i lambda(P_i).
```

#### Proof

For one target `z`,

```text
sum_x (PQ)(x,z)
 =sum_y [sum_x P(x,y)]Q(y,z)
 <=lambda(P) sum_y Q(y,z)
 <=lambda(P)lambda(Q).
```

Take the maximum over `z`.  The mixture bound follows by summing the column
loads and then taking the maximum. ∎

The first inequality is the abstract form of shellwise charge multiplication;
the second permits randomized selection among repair mechanisms.

## 2. Conditioning loss

Let `P:X->Y` be substochastic after deleting some actions.  Suppose every source
retains row mass

```text
g(x)=sum_y P(x,y)>=p>0.
```

Normalize the retained kernel by

```text
P^G(x,y)=P(x,y)/g(x).
```

### Theorem PP3bxa -- PROVED / UNIFORM CONDITIONING AMPLIFICATION

One has

```text
lambda(P^G)<=lambda(P)/p.
```

#### Proof

For every target,

```text
sum_x P^G(x,y)
 =sum_x P(x,y)/g(x)
 <=(1/p)sum_x P(x,y).
```

Take the maximum. ∎

Thus imposing pair-safety, a fixed dyadic chord type, or a clean boundary event
costs only the reciprocal of its uniform retained row mass.

## 3. Bounded overlap between type reservoirs

Partition the source set into classes

```text
X=X_1 disjoint_union ... disjoint_union X_K.
```

For each class let `P_i:X_i->Y` be row-stochastic and let `Y_i` be its target
support.  Combine them into the row-stochastic kernel `P` on all of `X`.

### Theorem PP3bxb -- PROVED / TYPE-OVERLAP LOAD BOUND

If every target belongs to at most `h` of the supports `Y_i`, then

```text
lambda(P)<=h max_i lambda(P_i).
```

More sharply, for every target `y`, its column load is at most the sum of the
`lambda(P_i)` over the classes whose support contains `y`.

#### Proof

The column load at `y` is

```text
sum_(i:y in Y_i) sum_(x in X_i) P_i(x,y).
```

Each inner sum is at most `lambda(P_i)`, and at most `h` classes occur. ∎

In particular, target-disjoint type reservoirs have `h=1`: splitting the source
family into as many as 510 fixed boundary signatures or `O(log^2 m)` dyadic
support-chord types causes no analytic loss when their repair targets are
separated.

## 4. Integrated finite-type closure criterion

### Corollary PP3bxc -- PROVED / TYPED MULTISTAGE CONTRACTION

Suppose a repair procedure has stages `1,...,s`.  At stage `j`, sources are
partitioned into types whose target supports overlap with multiplicity at most
`h_j`, every type kernel has reverse load at most `rho_j`, and any conditioning
retains row mass at least `p_j`.  Then the composed procedure has reverse load at
most

```text
product_(j=1)^s (h_j rho_j/p_j).
```

Hence it is a strict contraction whenever this product is below one.

#### Proof

Apply `PP3bxa` to each conditioned type kernel, `PP3bxb` to combine its types,
and `PP3bwz` to compose the stages. ∎

This gives a concrete integration target for the active frontiers:

- fixed-signature boundary hubs or disjoint banks from `docs/399`;
- dyadic support-chord classes from `docs/402`;
- fractional direct-clean layer kernels from `docs/401`;
- finite-depth Hall kernels from `docs/400`;
- multiscale shell factors from `docs/403`.

The number of structural types matters only through actual target-reservoir
overlap, not through a crude union bound over all types.

The next theorem identifier after this chapter is `PP3bxd`.
