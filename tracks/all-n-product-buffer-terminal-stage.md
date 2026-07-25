# All-n product track: actual buffer-terminal stage

**Branch:** `research/all-n-product-construction`

This stage continues
[`all-n-product-finite-obstruction-stage.md`](all-n-product-finite-obstruction-stage.md).
PX341--PX355 specialize the abstract terminal theory to the actual
two-permutation-layer construction.  The nonhistorical base degree is one, so
every acyclic trajectory residual has order at most two.  Two fresh ambient
labels give a quadratic buffer-cycle bank with no internal rank-three
collateral.

## Current ledger

| Item | Status | Current result |
|---|---|---|
| Actual base degree | **IDENTIFIED** | The diagonal is separate and the opposite layer is one partial matching, so `Delta_0=1`. |
| Acyclic trajectory residual | **ORDER AT MOST TWO** | PX341 replaces the abstract `Delta_0+1` bound by `s<=2`. |
| Order-one terminal core | **BUFFER-ESCAPABLE** | PX342 gives an ancestor-safe noncollinear three-cycle. |
| Order-two terminal core | **BUFFER-ESCAPABLE** | PX343 gives an ancestor-safe internally triple-free four-cycle. |
| Composite history release | **UNNEEDED ON ACTUAL BRANCH** | PX345 avoids all historical positions instead of releasing them. |
| Actual terminal templates | **EXACT CENSUS** | PX346 leaves one order-one template and two unlabelled order-two templates. |
| Buffer-bank size | **QUADRATIC** | PX347 gives at least `n^2/4` valid states above the divisor threshold. |
| Buffer spread | **SUPPORT-SENSITIVE** | PX348 gives `4/n` for one-variable and `4/n^2` for two-variable cylinders. |
| Direct terminal sign | **DICHOTOMY** | PX350 gives improvement or normalized one-/two-buffer concentration. |
| Nonimproving bank cover | **CLASSIFIED** | PX351--PX354 force one of four growing concentration sectors. |
| Coordinate/generic rank one | **STRUCTURAL INPUT AVAILABLE** | Feed into PX245--PX252 and the heavy-cell/star decoder. |
| Directed-path sector | **OPEN SIGN** | Candidate pairs share a core row/column; exact coupled destruction credit remains to be attached. |
| Mixed two-buffer shadow | **STRUCTURAL INPUT AVAILABLE** | Feed into PX253--PX262; exact return-to-buffer sign remains open. |
| Small `n` exceptions | **FINITE** | The divisor threshold leaves finitely many base orders for exact verification. |
| PX63 conversion | **OPEN** | Insert the actual buffer-terminal alternative into the product induction. |
| Infinite exact closure | **OPEN** | No all-side product closure follows yet. |

## 1. Actual terminal geometry

The ordinary forbidden graph in one active layer is

\[
F^{\rm ord}=D\cup P\cup H_1\cup\cdots\cup H_d,
\]

where `P` is the opposite-layer matching.  Thus the base graph outside the
diagonal has degree one.  An acyclic historical-union antichain has order at
most two.

For one core endpoint, use

\[
u\to a\to b\to u.
\]

For two core endpoints, use

\[
u\to a\to v\to b\to u.
\]

Divisor bounds exclude the finitely many buffers creating an internal triple.
Both cycles avoid the diagonal, opposite layer, and every historical position.

## 2. Buffer-bank hierarchy

Above

\[
n\ge4\Delta_{\rm ord}+10+8\mathfrak d(n),
\]

both valid banks have at least `n^2/4` states.  A certificate determining
`nu` buffer variables has probability at most

\[
\frac4{n^\nu}.
\]

Therefore a core of order `s` improves whenever

\[
s>
\frac{4W_1^{\rm buf}}n+
\frac{4W_2^{\rm buf}}{n^2}.
\]

If every state is nonimproving, the bank is covered by one- and two-variable
blocker cylinders.  At least one of the following holds:

1. `Omega(n)` first-buffer labels carry a coordinate rank-one or directed-path
   blocker;
2. `Omega(n)` second-buffer labels carry the symmetric blocker;
3. `Omega(n^2)` buffer pairs carry a generic rank-one or mixed rank-two
   blocker.

These are growing sectors, not constant terminal rays.

## Immediate frontier

1. **Directed-path return sign.** Couple the shared-core directed-path family
   to endpoint moves and compute exact destruction.
2. **Mixed-shadow return sign.** Feed the quadratic cross-buffer family into
   PX256--PX262 and retain the original core destruction in the causal ledger.
3. **Coordinate-field feedback.** Quantify how PX249--PX252 returns a child
   whose destruction pays the buffer cover.
4. **Finite base orders.** Enumerate the orders below the explicit divisor
   threshold.
5. **Closure conversion.** State PX63 with the large-block theorem and the
   actual buffer-terminal alternative.

## Verification

```bash
python scripts/verify_product_buffer_cycle_terminal_escape.py
python scripts/verify_product_buffer_cycle_spread.py
python scripts/verify_product_buffer_cover_concentration.py
```

All three verifiers pass locally.  Exact infinite product closure and the
classical no-three-in-line conjecture remain open.
