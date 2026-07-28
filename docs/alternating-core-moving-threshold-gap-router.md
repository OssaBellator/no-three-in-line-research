# Co-moving threshold gap router

**Branch:** `research/alternating-core-chain`

AC3wf--AC3wj permit arbitrary absolute behaviour below a fixed threshold and periodic control above it. This note allows the threshold itself to move. The key coordinate is the exact gap between the additive balance and the moving threshold.

## Tail contract

Fix a finite control set `Q` and modulus `M>=2`. A tail state is

\[
(q,x,h),\qquad y=x-h\ge0.
\]

For `y>=0`, the legal transition and its increments depend only on

\[
(q,y\bmod M).
\]

Write the balance and threshold increments as `Delta_x` and `Delta_h`, and put

\[
g=\Delta_x-\Delta_h.
\]

The next gap is `y+g`. Every payment-sensitive field not encoded by `q`, the residue, or the decorated transition edge is an outer reset.

## AC3wk -- exact co-moving reduction -- PROVED

The moving-threshold tail is exactly equivalent to a one-sided additive gap process

\[
y\mapsto y+g
\]

with lower guard `y>=0` and finite phase `(q,y mod M)`.

### Proof

Subtract the threshold update from the balance update. The legality condition `x>=h` becomes `y>=0`, and the tail contract makes the control and gap increment functions of the finite phase alone. QED.

## AC3wl -- eventual finite phase cycle -- PROVED

Every deterministic tail history enters a repeated phase after at most `|Q|M` phase states. The repeated segment contains a simple phase cycle of length at most `|Q|M`.

### Proof

There are exactly `|Q|M` phases. Apply pigeonhole and erase internal closed subwalks. QED.

## AC3wm -- cycle drift is a modulus multiple -- PROVED

Let `D` be the sum of the gap increments around one phase cycle. Then

\[
D\equiv0\pmod M.
\]

### Proof

The cycle returns to the same gap residue, so the total gap change is divisible by `M`. QED.

## AC3wn -- moving-threshold phase router -- PROVED

Let `p_min` be the minimum prefix gap increment of the phase-cycle word.

1. If `D>0`, every legal complete traversal raises the gap by `D`; exact recurrence is impossible.
2. If `D=0`, one legal traversal returns the exact gap and complete tail state.
3. If `D<0`, a traversal started at gap `y` is legal exactly while `y+p_min>=0`, and the number of complete legal traversals is

\[
\boxed{\left\lfloor\frac{y+p_{\min}}{-D}\right\rfloor+1}.
\]

### Proof

The `j`-th traversal starts at gap `y+jD`, and its least internal gap is `y+jD+p_min`. Solve the resulting inequality. The positive and zero cases follow from the exact block increment. QED.

## AC3wo -- interface to AC4 -- PROVED UNDER THE COMPLETE MOVING-THRESHOLD CONTRACT

A recurrent moving-threshold tail with finite residue control has one continuation:

- strict gap escape;
- finite lower-headroom exhaustion;
- exact zero-drift return into the existing finite-state restoration router;
- current payment or a declared source debit on a cycle edge;
- or an explicit reset caused by a changed threshold rule, residue dictionary, absolute-value regime, legality interpretation or omitted physical field.

Thus moving thresholds create no new diffuse recurrence whenever their relative tail dynamics is finite-phase.

## Finite check

`scripts/verify_ac_moving_threshold_gap.py` enumerates deterministic finite phase systems, extracts every eventual phase cycle, verifies the modulus-divisibility law and checks the exact negative-drift execution budget.