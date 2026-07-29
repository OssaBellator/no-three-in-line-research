# Alternating-core main-focus consolidation

## Status

This note makes AC the sole active research focus and proves AC5hn--AC5hr by importing the reusable contracts from RI, BDA, GC, OP, SRR and SAS into one synchronized AC interface. The side-track branches are treated as frozen source libraries: no new side-track theorem dependency is created here.

The imported source mechanisms are:

- RI5ay--RI5bc: finite blocker-profile recurrence gates;
- BDA5bl--BDA5bp: canonical least-field restoration gates;
- GC2ge--GC2gi: bounded capacity-one donor matching and Hall cores;
- OP4ad--OP4ah: component displacement and finite cycle-holonomy clocks;
- SRR2n--SRR2r: threshold-local conditioned endpoint-cost drift;
- SAS5hd--SAS5hh: commuting disjoint-swap legality squares.

This note does not construct the six physical side evaluators, prove the remaining numerical capacities, prove AC6, or prove the no-three-in-line conjecture.

## AC-only working policy

All future continuation is routed through the AC branch. A side theorem may be used only as an immutable import certificate with its exact source label, hypotheses, physical address, epoch and capacity identity. New side calculations belong in an AC import adapter, not on a new RI, BDA, GC, OP, SRR or SAS branch.

The current AC pipeline already supplies synchronized Hall concentration, free-token repair gains, footprint-local commutation, typed repair cost, reserve queues, support-local revalidation, repeated-touch amortization and fail-closed schema checking. The purpose of this pass is to replace six parallel continuations by one AC-native typed record and one progress router.

## AC5hn -- tagged full-record address space -- PROVED

For each track `s` let `F_s=(f_{s,1},...,f_{s,d_s})` be its ordered retained logical fields:

- AC: physical source, certificate, defect, epoch, repair class;
- RI: repair type, field-element data, host/context, secant/line address, coherence, collateral class, epoch;
- BDA: physical source, numerator weight, rational gain, damping factor, restoration class, epoch;
- GC: physical source, donor, remedy, height, cause, local geometry, epoch;
- OP: repair type, physical source, unit class, valuation vector, holonomy, action kernel, epoch;
- SRR: candidate, witness atom, conditioned threshold, physical source, tensor cylinder, epoch;
- SAS: repair type, sign, boundary profile, neutral move, legality class, physical source, epoch.

Define the AC-native address space as the tagged disjoint union

\[
\mathcal L_{\rm AC}
=
\bigsqcup_s
\{s\}\times\{v_s\}\times
\prod_{i=1}^{d_s} A_{s,i},
\]

where `v_s` is the schema version. Its canonical serialization is

\[
\operatorname{Enc}_{\rm AC}
\bigl(s,(a_i)_i\bigr)
=
\bigl(s,v_s,((f_{s,1},a_1),\ldots,(f_{s,d_s},a_{d_s}))\bigr).
\]

This encoder is injective and has an explicit decoder by construction. It does not compress RI, OP or SAS into the inadequate old 120-state alphabets, and it does not require unrelated tracks to share one coordinate layout.

Removing any retained field gives a canonical collision: two records differing only in that field have the same omitted-field projection. A changed field order, version or track tag is an exact schema witness.

The old four-coordinate verifiers remain useful deterministic regression models, but they are no longer the AC address representation.

## AC5ho -- track-separated compatibility interface -- PROVED

For tagged incidence and token records define

\[
\operatorname{Compat}_{\rm AC}((s,r),(t,u))
=
\begin{cases}
\operatorname{Compat}_s(r,u),&s=t,\\
0,&s\ne t.
\end{cases}
\]

Every physical `Compat_s` must be supplied as a deterministic evaluator on the complete tagged record. Shared physical fields also carry declared projections into one global shared-state registry; two track records referring to the same primitive must agree under those projections.

Therefore AC accepts a compatibility edge only when:

1. the track and schema version match;
2. every retained field is present;
3. the track-local evaluator returns true;
4. shared-state projections are consistent;
5. the token is live and occurrence-faithful in the current epoch.

The least missing evaluator, omitted field, stale version, cross-track pair or shared-state disagreement is returned. This discharges the artificial alphabet-capacity obstruction at the representation level, but not the physical compatibility obligation.

## AC5hp -- immutable side-import registry -- PROVED

Every imported side certificate is normalized to one AC record

\[
C=(s,\theta,e,o,x,k,a,\gamma),
\]

where `s` is the track, `theta` the exact source theorem, `e` the epoch, `o` the unmatched owner, `x` the physical primitive, `k` the normalized outcome kind, `a` its nonnegative amount, and `gamma` its unique capacity or obstruction address.

The permitted normalized kinds and source routes are:

- `supply`: GC full donor assignment, SRR robust Hall supply, SAS legal commuting square, or any imported repair that AC's free-token theorem converts to deficit descent;
- `payment`: RI physical payment, BDA restoration payment, GC occurrence-faithful donor restoration, OP zero-holonomy payment, or SRR threshold-local neighbourhood loss;
- `descent`: RI scale/denominator/margin/rank descent, BDA monotone field descent, or OP path/phase rank descent;
- `ticket`: RI occurrence/field return, BDA restoration edge, GC donor edge, or OP nonzero-holonomy orbit position;
- `reset`: a declared owner, context, legality, source, conditioning or schema reset with a funded token;
- `shortage`: a numerical AC key shortage, GC Hall-deficient donor core, or SRR threshold shortage;
- `obstruction`: an impossible restoration, failed guard atom, failed incidence bound, stale schema, hidden field or compatibility failure.

A source outcome not in the immutable registry is rejected. A certificate may not change track, theorem label, owner, epoch or capacity identity during queue revalidation.

## AC5hq -- one synchronized progress router -- PROVED UNDER THE IMPORT CONTRACTS

Let `Delta` be synchronized matching deficit. AC processes one accepted import certificate as follows.

1. `supply` executes through the existing footprint-local repair interface and lowers `Delta` by at least its certified amount.
2. `payment` deposits its amount in the typed track ledger, subject to occurrence capacity.
3. `descent` lowers a declared nonnegative integer rank by its amount.
4. `ticket` consumes a previously unused finite ticket address.
5. `reset` consumes a funded reset token and installs the declared new version.
6. `shortage` or `obstruction` terminates the current route with its exact witness.

No certificate can be charged to two cases. No payment, rank, ticket or reset capacity moves between tracks.

The six useful side mechanisms now have one AC interpretation:

- RI recurrence is finite unless it pays, descends, consumes a profile ticket or resets;
- BDA recurrence is localized to one restoration edge which is impossible, paid, descending, ticketed or reset;
- GC bounded reservoirs either supply donors, consume finite donor tickets or return a Hall shortage;
- OP internal shifts collapse to path displacements and finite holonomy clocks;
- SRR conditioning cost is charged only to threshold-local neighbourhood loss;
- SAS disjoint repairs require two base legality checks, after which the whole operation square commutes.

## AC5hr -- consolidated finite-interval envelope -- PROVED UNDER FINITE CAPACITY CONTRACTS

Fix a macro interval. Let

- `U` be total support-local matching disturbance;
- `C_pay` be total accepted paid-touch capacity;
- `C_rank` be total available rank units;
- `C_ticket` be the complete finite ticket stock;
- `C_reset` be the funded reset stock.

Every nonterminal AC episode either lowers deficit by at least one or consumes at least one unit from exactly one of those four finite resources. Since total deficit reductions are funded by initial deficit and disturbance, the number `E` of nonterminal episodes satisfies

\[
\boxed{
E
\le
\Delta_0+U
+
C_{\rm pay}
+
C_{\rm rank}
+
C_{\rm ticket}
+
C_{\rm reset}.
}
\]

For RI and BDA, the ticket terms include the finite profile/restoration-edge stocks. For GC they include target-donor edges. For OP they include nonzero-holonomy orbit positions. SRR local-loss units are included in `C_pay`. SAS legality either enables a deficit-lowering commuting repair or returns a guard obstruction.

Thus the side branches are no longer independent recurrence directions. Under complete tagged schemas and finite typed capacities, every side event is consumed by the single AC bound above or returns one exact obstruction.

## Finite check

`scripts/verify_ac_main_focus_consolidation.py` checks:

- round-trip encoding for all seven tagged schemas;
- cross-track separation;
- canonical omission witnesses for every generated record;
- every immutable side-import route;
- the exact finite-interval episode bound.

The deterministic run checks 2,500 systems, 17,500 tagged-record round trips, 17,500 omission witnesses, 52,500 cross-track separations, 72,500 import routes and 86,390 bounded nonterminal episodes.

## Main AC frontier

Only AC remains active. The next work is:

1. implement the six physical `Compat_s` evaluators on tagged full records;
2. define shared-state projections and consistency checks;
3. instantiate the imported finite ticket and rank capacities;
4. attach every side payment to one AC typed ledger;
5. prove that the consolidated finite-interval envelope forces a strict finite macro-state descent or completion;
6. close AC6.

The global no-three-in-line conjecture remains open.
