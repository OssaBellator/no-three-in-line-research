# Bounded-path certificates for shell cycle rates

`docs/421` identifies the optimal finite shell-state rate with the maximum
directed-cycle geometric mean.  This chapter makes the criterion finitely
certifiable without enumerating arbitrary closed walks.  Every failure has a
simple cycle of bounded length, while every successful rational threshold has
a rational potential built from paths of length at most `|V|-1`.

The statements are general.  They do not provide the required shell-state
quotient for prime patching.

## 1. Short cycle witnesses

Let a finite directed graph have `n` states and positive rational edge gains
`p_e`.  Fix a proposed rate `q>0`.

### Theorem PP3bzt -- PROVED / SIMPLE-CYCLE RATE WITNESS

If some closed directed walk `W` satisfies

```text
product_(e in W) p_e>q^|W|,
```

then there is a simple directed cycle `C` of length at most `n` with

```text
product_(e in C) p_e>q^|C|.
```

#### Proof

Repeatedly split a non-simple closed walk at a repeated vertex.  The walk
becomes a multiset of simple directed cycles.  If every resulting cycle had
geometric mean at most `q`, their product would also satisfy the proposed
bound, contradicting the hypothesis. ∎

Thus every failed finite-state shell certificate has a witness using at most
one visit to each state.

## 2. Rational bounded-path potentials

Normalize each edge by

```text
g_e=p_e/q.
```

Assume every simple directed cycle has product at most one.  For a state `u`,
define

```text
a(u)
 =max product_(e in P) g_e,
```

where the maximum is over all simple directed paths starting at `u`, including
the empty path.

### Theorem PP3bzu -- PROVED / BOUNDED-PATH SHELL POTENTIAL

The maximum defining `a(u)` uses paths of length at most `n-1`, is positive and
rational, and satisfies every edge inequality

```text
p_(u,v) a(v)<=q a(u).
```

Hence `a` is an exact rational `q`-potential.

#### Proof

There are finitely many simple paths, so the maximum is rational and attained.
For an edge `u->v`, prepend it to a maximizing simple path from `v`.  If this
creates a repeated vertex, delete the enclosed directed cycle.  Its normalized
product is at most one, so deletion does not decrease the product.  The
resulting simple path starts at `u`, proving

```text
a(u)>=g_(u,v)a(v).
```

Multiply by `q`. ∎

This is a direct finite certificate: no logarithms or irrational eigenvectors
are needed.

## 3. Strongly connected localization

### Theorem PP3bzv -- PROVED / SCC-LOCAL SHELL AUDIT

Every directed cycle lies in one strongly connected component.  Therefore the
optimal cycle rate of the whole graph is the maximum of the optimal rates of
its cyclic strongly connected components.

For any rational `q` strictly above that maximum, the bounded-path construction
in `PP3bzu` gives a global rational strict potential.  If the graph is acyclic,
the infimum cycle rate is zero and every positive rational `q` admits such a
potential.

#### Proof

The cycle statement is immediate from strong connectivity along a directed
cycle.  Apply `PP3bzu` after checking the cycle condition componentwise; edges
between components form an acyclic condensation and create no new cycles. ∎

The shell audit can therefore be split into small recurrent components plus
acyclic transient transitions.

## 4. Revised shell frontier

A finite shell quotient now has a compact exact audit protocol.

1. Compute strongly connected components.
2. Search only simple cycles of length at most the component size, or construct
   the bounded-path potential directly.
3. Return either one rational strict potential or one explicit short
   noncontracting cycle.

This is suitable for machine-generated proof ledgers.

## 5. Exact diagnostic

Run

```bash
python scripts/check_bounded_path_shell_potentials.py
```

The checker enumerates all simple cycles of a rational shell graph, extracts a
short witness below the optimum rate, constructs the exact bounded-path
potential above it, and verifies the SCC localization.

The next theorem identifier after this chapter is `PP3bzw`.
