# Alternating-core import of union-safe BDA products

**Branch:** `research/alternating-core-chain`

BDA5ai--BDA5ak corrected the local radial rectangle payment for the full two-layer union. BDA5al--BDA5ao now propagate that correction through heterogeneous products and rank-one suppression. This note imports the corrected product interface into the clean-pair and missing-support branches without changing their paid extraction constants.

## AC3gc -- canonical binary clean-pair menu -- PROVED

Every actual clean BDA pair entering AC3el has exactly two canonical union-safe local states, one for each radial role. Each state:

- changes blocker rows only in columns of the pair's five-column support;
- removes both endpoints of its selected role from the full union;
- destroys both private paid radial triples;
- preserves both permutation layers and their disjointness.

For a support-disjoint family, arbitrary choices from these binary menus form a legal product state.

### Proof

This is BDA5al--BDA5am. The AC3el support audit supplies the five distinct support rows and columns required there. Private paid sets and all protected scopes are included in the AC3v envelopes. QED.

## AC3gd -- exact corrected clean-product ledger -- PROVED

For a candidate triple meeting `r` clean-pair supports, `1<=r<=3`, let `m_C` be the number of binary local role tuples that create it. Its exact product probability is

$$
\boxed{\Pr(C)=m_C/2^r.}
$$

Thus the clean-pair product has the exact collateral decomposition

$$
F+T_1+T_2+T_3
$$

with the BDA5an definition of `T_r`. The private payment and AC2c extraction losses in AC3em--AC3eo are unchanged. In particular, the union-safe replacement changes only the local envelope, not the `1/K`, `1/128` or `1/256` paid-scale factors recorded before the later AC3fa rank split.

### Proof

Use AC3gc and BDA5an inside the scope-complete AC3v product. Payment is unchanged because every canonical role state destroys the same two private radial triples. QED.

## AC3ge -- corrected rank-one suppression import -- PROVED

After universal one-support triples are moved into `F`, each clean pair has two role-exclusive rank-one costs. The BDA floor/imbalance identity, cheaper-role assignment and higher-rank losses remain

$$
T_1=B_1+I_1/2,
$$

$$
C_2\le4T_2,\qquad C_3\le8T_3.
$$

If `D>F` but the suppressed product does not improve, one of

$$
B_1\ge(D-F)/3,
$$

$$
T_2\ge(D-F)/12,
$$

$$
T_3\ge(D-F)/24
$$

holds.

### Proof

This is BDA5ao. The proof uses only the exact binary menu and product legality, both supplied by AC3gc. QED.

## AC3gf -- propagation through missing-support composites -- PROVED

In AC3ep--AC3es, first perform the canonical active completion and its first blocker repair. The resulting clean five-cell support then uses the AC3gc binary union-safe decoder, not the old phase-flip menu.

Consequently:

1. every missing-support composite remains a legal paid decoder;
2. the private occupied-side payment and adjacent-scale ticket are unchanged;
3. the AC3fa created-cell-rank return remains `D/3`;
4. the corrected created-role alphabets and complete-envelope bounds remain
   $$
   \ell_{\rm clean}\le12,
   \qquad
   \ell_{\rm miss}\le36,
   $$
   $$
   e_{\rm clean}\le21,
   \qquad
   e_{\rm miss}\le53;
   $$
5. every clean or missing-support overload uses the AC3fp--AC3fr dictionary with those corrected envelope bounds.

### Proof

The completion stage and its payment precede the clean-pair decoder and are unchanged. Replace only the final BDA local menu by AC3gc and include every auxiliary blocker cell and replacement in the composite envelope. AC3v gives product legality, AC3w gives payment additivity, and AC3fa gives the rank return. The role and envelope bounds are AC3gb. QED.

## Consequence

The union-safe propagation frontier is closed for both actual-clean and missing-support BDA products. The remaining BDA outputs on the alternating branch are:

- the balanced rank-one floor after cheaper-role suppression;
- rank-two and rank-three created certificates;
- same-role AC2d overload stars;
- the five affine anchor chains;
- ordinary or reflected co-anchor outputs not yet passing through the AC3ec support audit.

The next note, AC3gg--AC3gj, orients every realized created certificate of ranks one through three to one new pivot cell and gives all three ranks the same union-safe paid local transition.

## Finite check

`scripts/verify_ac_bda_product_propagation.py` checks the binary probability denominators, the floor/imbalance and `4,8` suppression factors, the failed-router constants, the corrected role/envelope counts and the unchanged alternating-core paid-scale constants.
