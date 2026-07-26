# Captive controller-star partner-bank conversion

A controller-shadow star may have a centre `p` that is itself a fixed controller,
so moving `p` would change the controller universe.  The other endpoints provide
a controller-preserving alternative.

Suppose the witness graph contains distinct blocker pairs

```text
{p,s_1},...,{p,s_C}.
```

Each pair was selected for at least one bad candidate entry.

## 1. Distinct partners and credit

### Proposition PP3ajy -- PROVED

The partners `s_1,...,s_C` are distinct.  One can choose distinct bad entries
`z_1,...,z_C` such that `{p,s_j}` witnesses `z_j`.  Deleting `s_j` while retaining
`p` removes the corresponding incidence.

#### Proof

Distinct graph edges through `p` have distinct other endpoints.  Distinct witness
pairs have disjoint nonempty preimages under the chosen-witness map; select one
entry from each preimage. ∎

Thus every partner carries at least one designated credit unit.

## 2. Free-partner or controller-partner split

Call a partner free when it is not a fixed controller point.  Write the saturated
source as the disjoint union of its two permutation layers `P_0,P_1`.

### Theorem PP3ajz -- PROVED

At least one of the following holds.

1. At least `C/4` free partners lie in one permutation layer.
2. At least `C/2` partners are fixed controller points.

In case 1 the selected partners have distinct rows and columns, are disjoint from
all controllers, and carry total designated credit at least their cardinality.

#### Proof

Either at least half the partners are controllers, or at least half are free.
Pigeonhole the free partners between the two permutation layers.  Apply PP3ajy. ∎

## 3. Partner permutation with the centre fixed

Let `B` be the free one-layer bank from case 1 and put `Q=|B|`.

### Proposition PP3aka -- PROVED

Every source-admissible derangement of `B` preserves all fixed controllers,
preserves saturation, destroys the `Q` selected incidences through `p`, and has
exact dynamic change

```text
Xi(S_pi)-Xi(S)=I(pi)-C(B),
C(B)>=Q.
```

#### Proof

The bank is controller-disjoint and lies in one permutation layer, so the standard
endpoint-permutation identities apply.  A derangement moves every selected
partner, while `p` remains fixed.  PP3ajy gives `Q` distinct removed incidences. ∎

### Theorem PP3akb -- PROVED / CONDITIONAL ENDPOINT-HOST INTERFACE

If the bank has a source-regular endpoint host, then the recapture-free and
ambient-support thinning chain PP3afn--PP3agg gives one of:

1. a strict paid improvement;
2. an ambient unary, rank-three, or rank-four support star;
3. a source, transition, anchor, Hall, alternating, or endpoint-host failure;
4. a source-valid trade handled by final-state direct allocation.

No recapture term involving `p` occurs because `p` is neither moved nor inserted.

## 4. Genuine captive residual

### Corollary PP3akc -- PROVED

A captive controller-shadow star of degree `C` yields either:

1. a controller-preserving free-partner credited bank of size at least `C/4`; or
2. a controller--controller blocker star of degree at least `C/2`.

At `C>=W`, both alternatives have target order.  Only the second remains a
genuinely captive object.

### Corollary PP3akd -- PROVED / CONDITIONAL CONVERSION INTERFACE

Combining PP3hu with PP3akc, positive-density initial movement/refill shadow
failure yields one of:

1. a free-centre target-size star feeding the fresh-helper cascade;
2. a captive centre with a free-partner target-size bank;
3. a target-size controller--controller star;
4. an endpoint-disjoint blocker bank of size `Omega(m^(21/40))`;
5. an explicit endpoint-host obstruction during conversion.

An unspecified captive centre is therefore no longer an independent frontier.

The no-three-in-line conjecture remains unproved.
