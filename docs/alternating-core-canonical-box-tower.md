# Alternating-core canonical box and nested-tower closure

## Status

This note keeps AC as the sole active research focus and proves AC5ix--AC5jc. It continues the bounded physical epoch serializer AC5is--AC5iw by choosing the least cap profile forced by the historical AC contracts, classifying the complete current frontier, resolving the current overflow queue by one exact least enlargement, and identifying the precise uniformity condition under which a nested tower of bounded AC certificates closes globally.

The result remains contract-qualified. It does not supply the missing geometric exclusion sets, prove that the physical AC dictionaries are finite and complete, prove the required uniform tower bounds, prove AC6, or prove the no-three-in-line conjecture.

## Canonical finite data

Fix one schema version and the finite dictionaries of AC5is--AC5iw. For each nonnegative resource coordinate `m_i`, let

\[
\beta_i=C_i+q\max(B,1)
\]

be its certified low-buffer threshold from the positive-circulation contract. For every globally addressed source, certificate, payment, ticket or reset balance `a`, let

\[
S_a=S_a^{\rm init}+S_a^{\rm dep}
\]

be the initial stock plus all named deposits admitted in the fixed epoch. For the one-counter tail, let `Q` be the finite control set, `M` the residue modulus, `H_abs` the exceptional absolute threshold and

\[
G=\max_{(q,r)}|\delta(q,r)|.
\]

Put

\[
S_{\rm phase}=|Q|M,
\qquad
H_{\rm obs}=H_{\rm abs}+G S_{\rm phase}.
\]

The remaining finite coordinates--partial installations, repair queues, active recreation atoms, owners, zones, phases and restart fields--use their complete finite dictionaries exactly as in AC5is.

## AC5ix -- canonical least historical cap profile -- PROVED

Define the first cap profile by

\[
K_i^{(0)}=\beta_i,
\qquad
C_a^{(0)}=S_a,
\qquad
H^{(0)}=H_{\rm obs}.
\]

This is the componentwise least profile satisfying all three requirements:

1. every low-buffer face `0<=m_i<beta_i` and its first buffer-rich level `m_i=beta_i` occur in the box;
2. every balance allowed by source/certificate conservation, from zero through the full initial-plus-deposited stock, occurs in the box;
3. every tail segment entering at balance at most `H_abs` can be observed for `|Q|M` tail steps without exceeding the box solely from the increment bound `G`.

For the tail requirement, after `s<=|Q|M` steps,

\[
b_s\le H_{\rm abs}+Gs\le H_{\rm obs}.
\]

If the segment stays in the tail, a residue-control phase repeats within that window. The resulting phase block has drift divisible by `M` and is routed as positive escape, zero return or negative finite headroom. If it drops below `H_abs`, it has returned to the finite exceptional strip.

Lowering one `K_i^(0)` omits the first rich level, lowering one positive `C_a^(0)` omits a physically permitted conserved balance, and lowering `H^(0)` fails the extremal `+G` observation word of length `|Q|M`. Hence the profile is componentwise minimal under the displayed requirements.

### Proof

The low-buffer theorem requires all levels below `beta_i` and distinguishes the first level outside the low face, so `beta_i` is necessary and sufficient. Source/certificate conservation permits every integral balance up to its full named stock and forbids larger source-less mass, so `S_a` is the least complete cap. The deterministic phase space has `|Q|M` states; bounded increments give the observation inequality and the phase pigeonhole argument. The extremal records show componentwise necessity. QED.

## AC5iy -- complete frontier partition and canonical work queue -- PROVED

Run the AC5iu operation compiler on the canonical box and the AC5iv recognizers on its interior objects. Every unresolved object belongs to exactly one of the following ordered classes:

1. `terminal`: a complete installation or another declared terminal AC state;
2. `shortage`: a physical resource, source, certificate, payment, ticket or reset deficit with its exact cut or coordinate;
3. `amplification`: a balance above its physical initial-plus-deposited stock;
4. `monotone escape`: a certified positive-drift or other one-way AC route;
5. `reset`: a changed schema, dictionary, infrastructure, owner, occurrence interpretation or omitted payment-sensitive field;
6. `zero-neighbourhood`: an interior pair, state or edge recognized by no complete historical template;
7. `overflow`: an otherwise legal operation whose exact successor requires one or more upper caps to be enlarged.

The classes are disjoint because AC5iu stops at the first boundary condition and AC5iv is applied only to legal interior objects. Their union is the complete non-certified frontier.

The canonical work queue is ordered first by class, then by the complete physical address. Terminal, shortage, amplification, escape and reset records are final routes for the current schema. Zero-neighbourhood records are physical construction obligations. Overflow records are the only records eligible for cap enlargement.

### Proof

AC5iu is exhaustive and mutually exclusive on state-operation pairs. AC5iv partitions interior objects according to whether at least one complete template recognizes them. The fixed class and physical-address orders make the queue canonical. QED.

## AC5iz -- exact least enlargement for the current overflow queue -- PROVED

Let `R` be the finite set of current overflow records. Every `r in R` names one capped coordinate `z(r)` and the exact successor value `v(r)` required by its operation. Let the current cap be `L_z` and define

\[
L_z^+=\max\bigl(L_z,\max_{r:z(r)=z}v(r)\bigr),
\]

where an empty inner maximum leaves `L_z` unchanged.

Then `L^+` is the unique componentwise least cap vector resolving every record in `R`. Any resolving cap vector `L'` satisfies

\[
L'_z\ge L_z^+
\]

for every coordinate.

Let `N(L)` be the exact ambient product count of AC5is. The exact new shell required to resolve the current queue is

\[
\boxed{N_{\rm shell}(R)=N(L^+)-N(L).}
\]

For one resource or capacity coordinate enlarged from `L_z` to `L_z+d`, while all other coordinates remain fixed, the exact shell contribution is

\[
N(L)\frac{d}{L_z+1}.
\]

For the tail cap the identical formula holds with denominator `H+1`.

### Proof

Record `r` is internal after enlargement exactly when the new cap on its named coordinate is at least `v(r)`. Taking the coordinatewise maximum is therefore sufficient, and every resolving vector must dominate it. The shell identities are direct differences of the product formula. QED.

## AC5ja -- shell-efficient frontier drain and telescoping proof reuse -- PROVED

For each coordinate `z` touched by the current overflow queue, let

\[
g_z=|\{r in R:z(r)=z\}|,
\qquad
c_z=N(L^{(z)})-N(L),
\]

where `L^(z)` raises only coordinate `z` to `L_z^+`. Process coordinates in the deterministic order

\[
(-g_z,c_z,-(L_z^+-L_z),z).
\]

At the step for coordinate `z`, raise it directly to `L_z^+`. This resolves every currently known overflow on `z` and never invalidates an old interior record. The process terminates after exactly the number of coordinates touched by `R`, and its shell increments telescope:

\[
\sum_j\bigl(N(L^{j+1})-N(L^j)\bigr)
=N(L^+)-N(L).
\]

After the drain, the only new work is:

1. the exact new shell;
2. old overflow records that refined to internal edges and therefore need template recognition;
3. old boundary records that remain boundary records;
4. genuinely new boundary records exposed by shell states.

Every old interior compatibility value, state record, edge, template certificate and physical capacity address is reused unchanged.

### Proof

Each coordinate is raised once to the maximum required by all current records on that coordinate. AC5iw gives no regression for every old interior object. The final vector is `L^+` independently of processing order, and finite differences telescope. QED.

## AC5jb -- direct-limit AC graph of a cofinal nested box tower -- PROVED

Let

\[
\mathcal B_0\subseteq\mathcal B_1\subseteq\cdots
\]

be boxes with one fixed schema, dictionaries and physical interpretation. Assume every cap is nondecreasing, every named physical capacity address preserves its identity, and every old interior object is retained exactly as in AC5iw.

The direct unions

\[
V_\infty=\bigcup_n V_n,
\qquad
\Omega_\infty=\bigcup_n\Omega_n,
\qquad
E_\infty=\bigcup_n E_n
\]

are well-defined physical records. If the tower is **cofinal**--for every finite coordinate vector occurring in a physical AC state or transition, some box dominates it--then every finite physical AC trajectory is contained in one box.

Likewise, compatible template atlases and capacity quotients form direct unions. A boundary record either remains a permanent terminal/shortage/amplification/escape/reset witness or eventually refines to its exact interior successor.

### Proof

No-regression makes all overlap maps literal inclusions. A finite trajectory uses finitely many finite coordinate values, so cofinality supplies one common box containing every state and transition in the trajectory. The boundary refinement statement is AC5iw applied along the tower. QED.

## AC5jc -- uniform tower closure criterion -- PROVED UNDER UNIFORM PHYSICAL BOUNDS

Assume the cofinal tower of AC5jb and, for every box, a complete selected atlas satisfying AC5ir. Assume the schedulers agree on overlaps and there are uniform finite constants

\[
\Psi_*,\quad C_{\rm reset},\quad U,\quad W_{\rm dist},
\quad C_{\rm pay},\quad C_{\rm ticket}
\]

bounding the corresponding exact quantities in every box after global physical-address deduplication.

Put

\[
E_*
=(C_{\rm reset}+1)\Psi_*
+UW_{\rm dist}
+C_{\rm pay}+C_{\rm ticket}.
\]

Then every nonterminal physical AC trajectory in the direct-limit graph has length at most `E_*`. In particular no infinite nonterminal trajectory exists.

If the criterion cannot be applied, the tower compiler returns the least of:

1. a noncofinal coordinate;
2. an overlap disagreement or scheduler mismatch;
3. an unbounded mixed-radix potential maximum;
4. an unbounded reset, disturbance, payment or ticket ledger;
5. a source/capacity address whose physical identity changes along the tower;
6. a bounded-box atlas failure already returned by AC5ir.

### Proof

Suppose a nonterminal trajectory had more than `E_*` steps. Its first `E_*+1` steps form a finite trajectory, hence lie in one box by AC5jb. The complete atlas certificate in that box gives the uniform bound `E_*`, a contradiction. The failure list is the ordered negation of the hypotheses. QED.

## Deterministic audit

`scripts/verify_ac_canonical_box_tower.py` checks 2,500 generated systems. It verifies:

- the canonical low-buffer, conserved-balance and tail-observation caps;
- finite phase repetition and drift divisibility by the modulus;
- exact frontier partitioning;
- the componentwise least overflow-resolving vector;
- exact one-coordinate and total shell formulas;
- shell-priority drainage and telescoping;
- preservation of all old interior transitions;
- uniform-tower certificates and explicit divergent-ledger cases.

## Main AC frontier

Only AC remains active. The next concrete tasks are now sharply separated:

1. instantiate the canonical cap profile with the actual AC thresholds, named deposits, controller table and tail increments;
2. serialize and classify the resulting physical frontier;
3. discharge zero-neighbourhood interior objects by completing one of the six historical template records;
4. discharge shortages, amplification and reset witnesses physically;
5. prove every claimed monotone escape;
6. resolve the finite overflow queue by AC5iz--AC5ja;
7. construct a cofinal nested physical tower;
8. prove the uniform potential and globally deduplicated capacity bounds required by AC5jc, or retain the first diverging ledger as the exact AC6 obstruction.

AC6 and the global no-three-in-line conjecture remain open.
