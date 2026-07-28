# Superregular cumulative conditioned atom bank

This note records SRR2ck--SRR2co. It extends the conditioned threshold atom-budget theorem through repeated low-cost resampling epochs with exact named capacity deposits and burden debits.

## Contract

Fix one complete witness-atom dictionary during each epoch. Atom `a` has current nonnegative capacity balance `K_a`. At the selected endpoint-cost threshold, reference burden `B_a`, conditioning removal `R_a`, and new-conflict addition `A_a` are retained exactly, giving actual burden

`L_a = B_a - R_a + A_a >= 0`.

Named deposits are applied to exact atom classes before the epoch. Candidate weight is `W`.

## Theorem block

### SRR2ck — current atom account

The complete state retains the current atom-capacity vector and every named deposit. Conditioning removal cannot increase burden; new conflicts are charged to their exact atoms.

### SRR2cl — exact epoch debit

If `L_a <= K_a` for every atom, debit `L_a` from atom `a`. Cumulative accepted burden on each atom is at most its initial capacity plus named deposits.

### SRR2cm — executable low-cost weight

For a paid epoch, the conditioned threshold system retains an executable subfamily of weight at least

`W^2 / (W + sum_a L_a)`.

The debit and the executable-weight guarantee use the same actual threshold and atom dictionary.

### SRR2cn — first overload

If some `L_a > K_a`, return the least exact overloaded atom and overload `L_a-K_a`. No accepted epoch is recorded.

### SRR2co — reset boundary

Changed witness support, omitted conflicts, nonadditive capacity, hidden deposits, capacity reuse or a different threshold family returns reset rather than cumulative payment.

## Proof

The coordinate identity for `L_a` is the conditioned perturbation theorem. Coordinatewise debit gives the cumulative bank by induction. The weighted conflict-burden theorem gives SRR2cm at the same actual burden vector. Failure is exactly a negative next balance.

## Finite audit

Run `python scripts/verify_srr_cumulative_conditioned_atom_bank.py`.

## Scope

This theorem does not construct the geometric witness atoms or prove their capacities. It does not prove SRR2, SRR4 or the no-three-in-line conjecture.