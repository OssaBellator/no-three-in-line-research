# Rational-inverse compatibility perturbation stability

This note records RI5cq--RI5cu.  It quantifies how the owner-collateral Hall deficit changes when a reference arithmetic compatibility graph is perturbed.

## Contract

Let owners `O` have integer demands `d_o` and collateral sources `S` have integer capacities `c_s`.  Let `N_0(o)` be a complete reference compatibility graph and `N(o)` the actual graph after exact arc deletions and additions.  Retained owner, host, context and coherence fields are fixed throughout the comparison.

For `X subseteq O`, define

`def_N(X)=(sum_{o in X} d_o-sum_{s in N(X)} c_s)_+`

and let `Phi(N)=max_X def_N(X)`.

## Results

### RI5cq — subsetwise perturbation inequality

For every owner subset `X`,

`def_N(X) <= def_{N_0}(X)+cap(N_0(X)\N(X))`.

Only collateral capacity that becomes unreachable from the complete subset can worsen its deficit.

### RI5cr — global deficit stability

`Phi(N) <= max_X [def_{N_0}(X)+cap(N_0(X)\N(X))]`.

A canonical maximizing subset is an exact perturbed owner/collateral cut.

### RI5cs — monotonicity under added compatibility

Adding compatibility arcs cannot increase any owner-subset deficit or the global deficit.

### RI5ct — local deletion corollary

If each owner loses access to at most `kappa` sources and every source capacity is at most `C`, then

`def_N(X) <= def_{N_0}(X)+|X| kappa C`.

Sharper bounds use the exact union of lost sources rather than the ownerwise sum.

### RI5cu — transport composition

When the right-hand side is zero for every subset, RI5cg--RI5ck gives full integral payment.  Otherwise the least maximizing subset is retained for the owner-collateral bank and cross-bank comparison.

## Proof

The actual neighborhood contains every reference source except those in `N_0(X)\N(X)`, and may contain additional sources.  Hence

`cap(N(X)) >= cap(N_0(X))-cap(N_0(X)\N(X))`.

Subtracting from the demand of `X` and taking positive parts proves the subset inequality.  Maximization and the local deletion estimate are immediate.

## Finite audit

Run:

`python scripts/verify_ri_compatibility_perturbation.py`

The deterministic audit checks:

- 7,500 owner-collateral systems;
- 10,258 deleted compatibility arcs;
- 4,907 added compatibility arcs;
- 1,283 systems with increased deficit;
- 6,217 nonworsened systems;
- 16,648 reference and 18,650 actual deficit units;
- 31,997 units in the exact perturbation envelope.

## Scope

This theorem does not prove that the concrete RI arithmetic graph is close to a chosen reference graph, nor does it create collateral capacity.  Changed retained fields, free owner sources and omitted compatibility arcs return reset.  RI6 and the no-three-in-line conjecture remain open.
