# Geometric-cleaning clean-height bank

This note records GC2ic--GC2ig. It converts the exact minimum clean-height loss into a cumulative paid resource.

## Contract

At epoch `t`, the complete cause/remedy transport system has an exact minimum additive clean-height loss `L_t`, obtained from the threshold transport theorem. The epoch is either infeasible, in which case it returns a cause/remedy Hall cut, or feasible with finite `L_t`.

Retain an initial nonnegative clean-height reserve `H_0` and exact nonnegative deposits `P_t`. No unrecorded height replenishment is allowed.

## Theorem block GC2ic--GC2ig

Across any feasible epoch sequence:

1. exact height preservation occurs precisely when `L_t=0`;
2. an epoch is paid whenever its minimum loss is debited from the current reserve;
3. cumulative paid loss is at most `H_0 + sum_t P_t`;
4. for every threshold `J>=1`, the number of paid epochs with `L_t>=J` is at most
   `floor((H_0+sum_t P_t)/J)`;
5. the first epoch with `L_t` larger than the available reserve returns an exact clean-height overload;
6. transport infeasibility is never charged to this bank and remains a Hall-cut obstruction.

## Consequence

Clean-height preservation need not hold at every step. It is enough to prove exact zero-loss on the main route and a finite physical reserve/deposit account for exceptional positive-loss remedies.

## Finite audit

Run:

`python scripts/verify_gc_clean_height_bank.py`

The audit solves small capacitated transport instances exactly, distinguishes infeasible Hall cuts from feasible minimum loss, and checks paid, zero-loss and overload epochs against a dynamic reserve.

## Scope

The theorem does not construct the concrete remedy graph, height costs or deposits. It does not prove GC5 or the global conjecture.
