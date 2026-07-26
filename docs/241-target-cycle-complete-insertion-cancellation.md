# Target cycles admit complete two-step insertion cancellation

PP3uw--PP3ux leave insertion cost on an alternating cycle as the paid quantity to
control.  PP3ajf--PP3ajl likewise leave chord and backbone geometry when robust
final allocation is unavailable.  The critical separated-helper theorem PP3arp--
PP3arw gives a direct composite route.

After a first endpoint-cycle trade, every newly created controller-shadow incidence
contains at least one newly inserted cycle cell.  A second source-valid trade moving
all those cells destroys the entire first insertion cost.  If the second trade is a
complete-support strictly alternating host, its own insertion cost is zero.  Thus
all first-step insertion multiplicity cancels, not merely one local atom or one
bounded table.

## 1. Every insertion incidence meets the inserted set

Let a source-admissible endpoint trade `T_1` replace a set of old source cells by a
set

```text
D={d_1,...,d_s}
```

of newly inserted cells.  Let its exact controller-shadow insertion and removal
terms be

```text
I_1,R_1.
```

### Proposition PP3arx -- PROVED

Every incidence counted in `I_1` has blocker pair containing at least one member of
`D`.

#### Proof

The dynamic potential difference compares source pairs before and after the trade.
A pair present after but not before contains at least one newly inserted source
point.  The insertion term is precisely the weighted count of such new blocker
pairs. ∎

The statement is independent of unary/binary multiplicity and of the canonical
support decomposition.

## 2. Moving the whole inserted set removes all first-step cost

Let `T_2` be any source-admissible trade from the post-`T_1` source that deletes
every member of `D`.  Write its insertion and removal terms as `I_2,R_2`.

### Proposition PP3ary -- PROVED

One has

```text
R_2>=I_1.
```

Consequently

```text
Xi(S_2)-Xi(S_0)
<=
I_2-R_1.
```

#### Proof

Immediately before `T_2`, every incidence counted by `I_1` is present in the
potential and contains a point of `D` by PP3arx.  Deleting all of `D` destroys every
such incidence, with its full candidate-entry multiplicity.  Hence `R_2>=I_1`.
Adding the two exact dynamic identities gives

```text
(I_1-R_1)+(I_2-R_2)<=I_2-R_1.
```

∎

This is complete insertion cancellation: no part of the first insertion table needs
to be localized before the second move.

## 3. Zero-cost second cycle

Assume the cells of `D` lie in one current permutation layer.  Puncture those members
of `D` that are active controllers, and choose an ordinary controller-disjoint
helper reservoir `H` in that layer.

### Theorem PP3arz -- PROVED / CONDITIONAL CRITICAL SEPARATED-HOST INTERFACE

Suppose `H` contains a subset of size `Theta(s^2)` to which PP3aru applies with
marked set `D`.  Then either:

1. there is a strictly alternating source-valid second cycle moving all of `D` with

   ```text
   I_2=0;
   ```

2. there is an `Omega(s)` canonical source/support star, matching, endpoint bank, or
   fixed-core petal bank;
3. a genuinely external source-clean, transition, anchor, Hall, alternating,
   matching, distinguished-endpoint, common-layer, or controller-density condition
   fails.

#### Proof

Restrict the linear helper reservoir to any `Theta(s^2)` subset and apply PP3aru
with `W` replaced by `s`.  The proof of PP3arr is scale-exact. ∎

If the ambient reservoir has size `Theta(W^2)` and `s<=W`, such a restricted subset
is available whenever the external constraints leave the required helpers.

## 4. Strict composite payment

### Theorem PP3asa -- PROVED / CONDITIONAL COMMON-LAYER AND EXTERNAL-HOST INTERFACES

Suppose alternative 1 of PP3arz holds.  Then the two-step package satisfies

```text
Xi(S_2)-Xi(S_0)<=-R_1.
```

In particular every first trade with positive removal credit becomes a strict paid
composite trade, regardless of the size or multiplicity of `I_1`.

#### Proof

Substitute `I_2=0` into PP3ary. ∎

No robust final allocation, self-recapture estimate, foreign-support first moment,
or local atomization is used.

## 5. Alternating-cycle states

Let `Gamma` be a directed alternating cycle in a source-safe endpoint host.  Switch
`Gamma` in the first trade.  Its moved reference endpoints form `D`, and in the
fully credited setting

```text
R_1>=|V(Gamma)|.
```

### Corollary PP3asb -- PROVED / CONDITIONAL ONE-LAYER COMPLETE-SUPPORT INTERFACE

Every alternating-cycle state of length `s` has one of the following outcomes.

1. A two-step source-valid package decreases `Xi` by at least `s`.
2. An `Omega(s)` canonical source/support structure is extracted.
3. An explicit external host condition fails.

#### Proof

Apply PP3arz--PP3asa.  Cycle switching preserves the endpoint matching by PP3um,
so the inserted cells form one current permutation layer. ∎

This upgrades PP3ux: average cycle insertion cost is no longer the internal paid
quantity when the complete-support second host is available.

## 6. Mobility hubs, chord cycles, and target Hamilton states

### Corollary PP3asc -- PROVED / CONDITIONAL EXISTING GEOMETRIC INTERFACES

The cycle geometries in PP3uy and PP3ajl have the following revised endpoint.

1. Every cycle-star petal can be paid by a zero-cost second cycle, or yields a
   canonical support structure at its own length scale.
2. A resource-disjoint alternating-cycle bank can be processed petal by petal; every
   internally supported petal makes strict composite progress.
3. A target-scale Hamilton defect cycle of length `Theta(W)` is strictly paid in two
   steps, or produces a target-size canonical support structure.
4. Sparse chord hubs, rooted chord stars, and distinct-signature banks remain
   relevant only when they certify an external second-host failure or when the
   required cycle cells are not co-layered.

#### Proof

Apply PP3asb to each cycle state.  In the target case take `s=Theta(W)` and use the
`Theta(W^2)` slab reservoir.  For shorter petals restrict to `Theta(s^2)` helpers.
The chord localizations identify candidate first cycles but do not alter the
composite identity. ∎

For bounded `s`, the state space is finite and can be checked directly; the
asymptotic support extraction is needed only for growing petals.

## 7. Complete insertion tables are not a noncanonical frontier

### Corollary PP3asd -- PROVED

For any source-admissible first endpoint trade whose newly inserted cells are
co-layered and admit the critical separated second host, the full first-step
insertion table cancels automatically.  It need not first be represented as a
single `A_2`, `B_3`, or `B_4` atom.

Thus insertion concentration in a first cycle or bounded endpoint package is no
longer an independent noncanonical endpoint.  The remaining alternatives are:

1. external erosion of the helper reservoir;
2. absence of a common current permutation layer;
3. inability to puncture marked controllers while preserving the required margin;
4. branches not expressible as endpoint replacement trades.

The no-three-in-line conjecture remains unproved.
