# Physical source-atom capacity and realized amplification overload

**Branch:** `research/alternating-core-chain`

AC3qa--AC3qe close realized multi-output amplification under an assumed total stock cap.
This note derives that cap whenever every source unit is an occurrence-faithful use of one
atom from a finite physical capacity universe.  Crossing physical feasibility is not an
unstructured large number: it creates one canonical overloaded physical atom, and the
first such atom must receive a realized output in the crossing transition.

The contract is deliberately private and additive.  Shared or nonadditive source objects,
fresh unregistered atoms and recreated capacity remain outside the theorem.

## Finite physical source universe

Fix one cyclic source component `S`.  Let `P` be a finite totally ordered set of physical
source atoms.  Atom `p` has fixed integer capacity

`b_p in Z_(>=0)`.

Every live source unit in the component carries one exact atom address `p`.  Write `n_p(t)`
for the number of live units using `p` at time `t`, and put

`S_tot(t)=sum_(p in P)n_p(t)`,

`B_phys=sum_(p in P)b_p`.

A state is **physically feasible** when `n_p(t)<=b_p` for every atom.  Every certified
realized output unit must name its atom before the transition is accepted.  Changing the
atom universe, one capacity, or the atom-address rule is an outer reset.

## AC3qf -- exact physical stock ceiling -- PROVED

Every physically feasible state satisfies

`S_tot(t)<=B_phys`.

### Proof

Sum the coordinate inequalities `n_p(t)<=b_p` over `P`. QED.

Thus the cap in AC3qe is reconstructed from exact physical capacity data rather than
introduced as an independent scalar field.

## AC3qg -- canonical physical overload atom -- PROVED

For an arbitrary nonnegative occupancy vector define

`E_phys=(S_tot-B_phys)_+`,

`O_phys=sum_(p in P)(n_p-b_p)_+`.

Then

`O_phys>=E_phys`.

If `E_phys>0`, the least atom with `n_p>b_p` is a canonical overload address.  Moreover one
atom has overload at least

`ceil(E_phys/|P|)`.

### Proof

For every coordinate, `n_p-b_p <= (n_p-b_p)_+`.  Summing gives
`S_tot-B_phys<=O_phys`.  Positive excess therefore forces a nonempty overloaded set, whose
least member is canonical.  Pigeonhole over at most `|P|` positive overload coordinates
gives the final bound. QED.

The overload is physical occurrence excess, not merely equality of symbolic source names.

## AC3qh -- first feasibility crossing is a realized-output overload -- PROVED

Suppose an alpha-pure transition starts from a physically feasible occupancy vector and
ends in a physically infeasible vector.  Then at least one atom becomes overloaded in that
transition.  Every newly overloaded atom has positive net occupancy increment and hence
receives at least one of the transition's certified realized output units.

The least newly overloaded atom is the canonical first-crossing certificate.  If the final
total also satisfies `S_tot'>B_phys`, AC3qg supplies the additional quantitative total-
excess bound.

### Proof

Physical infeasibility of the final vector gives an atom that was feasible before and is
overloaded after.  A coordinate with nonpositive net increment cannot cross upward through
its fixed capacity, so each newly overloaded coordinate has positive increment.  Under
alpha-purity the only positive component increments come from certified realized outputs.
The final statement is AC3qg. QED.

In particular, a transition cannot hide a local or total cap crossing in a declared but
unrealized slot.

## AC3qi -- physical capacity bounds realized surplus -- PROVED

For any alpha-pure history whose every state is physically feasible, let

`A=sum_t(h_t-1)_+`,

`L=sum_t(1-h_t)_+`

as in AC3qb.  Then

`A<=L+B_phys-S_tot(0)`.

For binary realizations, the number of fully realized amplifications is at most the number
of zero-output losses plus the initial unused physical capacity.

### Proof

Apply AC3qb and use the derived ceiling `S_tot(T)<=B_phys` from AC3qf. QED.

This is the same sharp gain/loss inequality as AC3qb, but its headroom is now the exact sum
of occurrence capacities.

## AC3qj -- physical-capacity amplification router -- PROVED UNDER THE PHYSICAL-SOURCE CONTRACT

Inside one fixed source epoch assume:

1. every live component unit and every realized output has an exact atom in the fixed
   finite universe `P`;
2. occupancy above `b_p` is impossible, terminal, strictly descending, or consumes one
   unit from a finite exact overload-ticket stock for `p`;
3. loss units are impossible, terminal, descending or finitely ticketed;
4. conservative transitions are quotient-stuttering, descending or finitely ticketed;
5. non-alpha-pure changes and changes of atoms or capacities are outer resets.

Then the cyclic multi-output address cannot sustain an infinite nonterminal internal
history.

### Proof

As long as physical feasibility is preserved, AC3qi bounds realized surplus by finite
physical headroom plus the finite paid loss stock.  A transition leaving feasibility has
the canonical physical overload address AC3qh and closes by assumption 2.  Conservative
and lossy transitions close by assumptions 3--4, while every forbidden data change exits
the epoch. QED.

## Corrected AC4 source frontier

Unbounded realized amplification is no longer an obstruction when source units range over
a fixed finite physical atom universe with fixed additive capacities.  The live growth
cases are now:

- fresh or unbounded physical atom creation;
- capacities that can be replenished or recreated without a higher ledger;
- shared/nonadditive source units not represented by occupancy coordinates;
- outputs without occurrence-faithful atom addresses;
- unpaid loss units or payment-relevant unticketed conservative circulation.

The other AC4 interfaces remain genuinely unbounded structural semantics, nonfactoring
continuations, recreatable gate capacities, unresolved availability/conflict/reverse gates,
nonadditive owners and scalar/arithmetic macro cycles.

## Finite check

`scripts/verify_ac_physical_source_capacity_overload.py` exhausts small capacity and
occupancy vectors and samples alpha-pure atom-addressed histories.  It checks the physical
ceiling, quantitative overload localization, first-crossing output incidence and the
derived gain/loss bound.