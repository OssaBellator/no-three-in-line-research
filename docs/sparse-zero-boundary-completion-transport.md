# Sparse zero-boundary completion transport

This note records SAS5jl--SAS5jp. It gives the conditional implication from an exact zero boundary profile to final balanced completion.

## Contract

Assume the signed boundary router has returned the exact zero boundary vector. Retain a finite dictionary of internal residual task classes with integral demands `d_t`.

Let `M` be a finite dictionary of physically executable completion moves. Move `m` has integral capacity `c_m`, is boundary-neutral, and the complete compatibility graph records exactly which task classes it can complete. One move unit completes one task unit and consumes one capacity unit.

## SAS5jl — zero-boundary completion network

The remaining internal tasks and boundary-neutral moves form the capacitated network

`source -> tasks -> completion moves -> sink`.

Every integral flow preserves the zero boundary vector.

## SAS5jm — capacitated Hall criterion

All residual tasks are completed if and only if every task subset `X` satisfies

`sum_{t in X} d_t <= sum_{m in N(X)} c_m`.

The number of uncompleted task units equals the maximum positive Hall deficiency.

## SAS5jn — final balanced completion

When all Hall inequalities hold, executing the matched boundary-neutral moves clears every retained internal task and leaves the boundary vector exactly zero. Under the complete-task contract this is a final balanced algebraic compression.

## SAS5jo — canonical incomplete cut

When completion fails, the least maximizing task subset and its reachable move capacities form the canonical exact incomplete-compression cut.

## SAS5jp — reset boundary

A move with nonzero boundary output, omitted task class, omitted compatibility constraint, shared capacity without debit, changed algebraic interpretation or an unrecorded new task returns reset rather than being called a completion.

## Finite audit

Run:

`python scripts/verify_sas_zero_boundary_completion_transport.py`

The deterministic audit checks 7,500 systems, 26,220 task classes, 26,285 move classes, 55,289 compatibility arcs and 157,302 Hall-subset tests.

## Scope

The theorem is conditional on a complete residual-task dictionary and genuinely boundary-neutral physical completion moves. It does not prove that the concrete sparse algebraic system satisfies those contracts. SAS6 and the no-three-in-line conjecture remain open.
