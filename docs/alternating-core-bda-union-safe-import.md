# Alternating-core import of union-safe BDA rectangle repairs

**Branch:** `research/alternating-core-chain`

The source BDA branch now proves BDA5ai--BDA5ak. The old fully blocked phase flip is a legal two-layer matching exchange but preserves the rectangle union and cannot certify destruction for the no-three-in-line union potential. This note replaces every AC clean-pair use of that phase flip by the union-safe auxiliary blocker repair.

## AC3fz -- union-safe clean-pair support contract -- PROVED FROM BDA5ai--BDA5ak

Every actual-clean-partner record of AC3ec has the clean five-cell radial support. For either radial role, switch its two active endpoints to the opposite rectangle diagonal and use:

1. no blocker change when the diagonal is empty;
2. one carefully chosen outside blocker cell when exactly one cross is blocked;
3. two outside blocker cells and the BDA5ai four-row repair when both crosses are blocked.

The final union contains neither old endpoint of the selected role. Therefore both radial triples are absent from the final union, even when their context anchor or the other-role endpoints lie in the opposite layer.

The old AC3el support statement remains correct after replacing its local menu `Omega(R)` by this union-safe menu. A phase flip alone is not an admissible paid state for the union ledger.

### Proof

AC3ec supplies five distinct active rows and columns. BDA5ai gives a legal repair for every blocker occupancy and excludes both old endpoints from both layers. Each paid radial triple contains one selected-role endpoint, so both are destroyed in the union. QED.

## AC3ga -- corrected heterogeneous product interface -- PROVED

Enlarge every clean-pair decoder envelope by the auxiliary blocker cells and replacements used by BDA5ai. Then AC3em--AC3eo and AC3fa--AC3fd remain valid with the following interpretation:

- every local state is a union-safe BDA5ai decoder;
- private occupied-side payment is destroyed in every product state;
- AC3v includes all auxiliary row, column, replacement, protected and potential scopes;
- the executable-bank bounds `W_clean/K` are unchanged;
- the universal failed-bank rank returns remain
  $$
  \frac{W_x}{96KR\rho L}
  \quad\text{or}\quad
  \frac{W_x}{192KR\rho L}.
  $$

The older four-term source labels `F,T1,T2,T3` and stage masks remain available after their scopes are recomputed using the enlarged envelopes.

### Proof

The replacement changes only the finite local menu and envelope. AC2c, AC3v, AC3w and AC3fa depend on legality, complete scopes and private payment, all supplied by AC3fz. The quantitative extraction constants do not depend on the number of auxiliary cells. QED.

## AC3gb -- corrected finite role inventories -- PROVED

The union-safe BDA menu requires larger safe role alphabets.

### Created-cell roles

For clean pairs, the union over both radial roles uses at most:

- four active cross roles;
- eight blocker replacement roles, four per selected radial role.

Thus

$$
\boxed{\ell_{\rm clean}\le12.}
$$

For missing-support install-then-decode composites, replace the old ten-role decoder suffix by these twelve roles:

$$
\boxed{\ell_{\rm miss}\le36.}
$$

The rank-one, rank-two and rank-three role-multiset counts become

$$
\boxed{12,78,364}
$$

for clean pairs and

$$
\boxed{36,666,8436}
$$

for missing-support composites.

### Complete envelope roles

A safe clean-pair envelope inventory has at most twenty-one roles:

- five radial support cells;
- four active cross cells;
- four auxiliary blocker-source roles across the two radial choices;
- eight blocker replacement roles.

Hence

$$
\boxed{e_{\rm clean}\le21.}
$$

A safe missing-support composite inventory has at most fifty-three roles after adding active completion, first-stage repair and the union-safe clean decoder:

$$
\boxed{e_{\rm miss}\le53.}
$$

Therefore the AC3fp core overload dictionaries satisfy

$$
\boxed{T_{\rm core}(21)=168903}
$$

and

$$
\boxed{T_{\rm core}(53)=2693831.}
$$

The direct and absent-companion bounds `ell=8,16` and `e=13,24` remain safe under AC3fw because their previous inventories already allowed six final blocker-repair roles.

### Proof

The BDA5ai full repair has four blocker replacement positions for one selected role and uses two auxiliary source cells. Taking the union over the two radial choices gives the displayed clean inventory. The missing-support count adds two decoder replacement roles to the previous alphabet and thirteen envelope roles to the previous safe envelope bound. The multiset and `T_core` values follow from AC3fb and AC3fp. QED.

## Correction notice

The following older wording is superseded for the union potential:

- BDA5a's claim that a full phase flip destroys the paid radial triples;
- AC3el's use of that phase flip inside `Omega(R)`;
- any clean-pair verifier which checks only colour-layer removal rather than absence from the full union.

BDA5ai--BDA5ak and AC3fz--AC3gb are the canonical union-safe interfaces.

## Finite check

`scripts/verify_ac_bda_union_safe_import.py` checks the corrected role inventories, role-multiset counts, overload dictionary values and unchanged rank-return constants. The source geometric repair is exhaustively checked by `scripts/verify_bda_union_safe_rectangle_repair.py` on `research/bounded-denominator-absorbers`.
