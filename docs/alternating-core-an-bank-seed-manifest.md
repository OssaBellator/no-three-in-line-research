# Alternating-core AN-bank physical seed manifest

## Status

This note keeps AC as the sole active research focus and proves AC5kz--AC5le. It populates the first genuinely physical initial-state and operation records in the seven-section AC manifest. The input is exactly the proved AN2--AN4 alternating star-neutralization construction: one fixed rectangle switch, one inserted candidate, one endpoint-disjoint secant star, one selected opposite-layer endpoint type and the resulting forbidden-position matching bank.

The result does not prove that every later AC state is an AN seed, prove the AC1 concentration conversion on a failed bank, or prove AC6. It proves that every physical AN seed has a canonical finite schema and serializer record, an exact bank of `install` operations, an exact collateral census, and one canonical output: an improving state or the complete no-improvement ledger required by AC1.

## Physical AN seed record

Fix a current configuration decomposed into two permutation layers. A seed retains:

1. one admissible rectangle switch in the first layer;
2. its two removed cells and two inserted cells;
3. one inserted candidate point `z`;
4. endpoint-disjoint outside pairs
   \[
   \{P_j,Q_j\},\qquad 1\le j\le t,
   \]
   whose lines contain `z`;
5. a choice of the `Q_j` all in one fixed opposite permutation layer and one fixed channel;
6. their distinct column and row sets
   \[
   C=\{c_1,\ldots,c_t\},\qquad R=\{r_1,\ldots,r_t\};
   \]
7. the other-layer occupancy after the rectangle switch;
8. every current-star and certificate occurrence address;
9. the complete parent state and fixed witness orders.

For each source row and target column, the forbidden-position set `F` contains at most:

- the original diagonal position `(c_j,r_j)`;
- the cell occupied by the other permutation layer after the switch.

Thus every row and column of `F` has degree at most two.

## AC5kz -- canonical physical AN seed validation -- PROVED

A proposed seed is accepted only when:

1. `t>=7`;
2. the current layers are valid disjoint permutations;
3. the rectangle switch is physically legal and has the declared removed and inserted cells;
4. all `2t` star endpoints are physically present and pairwise distinct;
5. each triple `{z,P_j,Q_j}` is collinear;
6. the selected `Q_j` occupy distinct rows and columns in one fixed layer and channel;
7. `F` is exactly the union of the original positions and other-layer occupied positions;
8. every row and column of `F` has degree at most two.

The compiler returns the least malformed layer, switch, endpoint, collinearity, type, row/column or forbidden-position witness. On the accepted branch the complete seed is a valid `schema` record under AC5kn--AC5ks.

### Proof

All conditions are finite physical checks. Distinct rows and columns follow from membership in one permutation layer, while the two explicit forbidden sources give the degree-two bound. The fixed field order selects the first failure. QED.

## AC5la -- exact alternating installation bank and operation addresses -- PROVED

Let

\[
\Omega(F)=\{\pi\in S_t:(i,\pi(i))\notin F\text{ for all }i\}.
\]

For every `pi in Omega(F)`, define the replacement matching

\[
M_\pi=\{(c_i,r_{\pi(i)}):1\le i\le t\}
\]

and joint state

\[
S_\pi=Z\cup M_\pi,
\]

where `Z` is the parent state after deleting the chosen anchors and applying the fixed rectangle switch.

The canonical installation operation address is

\[
(\texttt{install},\text{seed},\pi,\text{switch},C,R,F,\text{epoch}).
\]

Every address has one exact successor. The bank size satisfies

\[
\boxed{|\Omega(F)|\ge t!/128},
\]

and every compatible prescribed rank-`r` partial matching obeys

\[
\boxed{
\Pr(Q\subseteq\pi)\le \frac{128}{(t)_r}
}
\qquad (r=1,2,3).
\]

### Proof

This is AN1 applied to the exact degree-two forbidden set. The operation address specifies every replacement edge, so the successor is deterministic. QED.

## AC5lb -- exact star destruction and physical collateral census -- PROVED

Every `install` operation in AC5la:

1. preserves the selected anchor row and column sets;
2. remains disjoint from the other layer;
3. moves every selected `Q_j` away from its original position;
4. destroys every original star triple `{z,P_j,Q_j}`.

Let `T_r` be the exact number of real collinear triples using exactly `r` mutually compatible nonforbidden anchor-block cells and `3-r` cells of `Z`. The seed compiler enumerates the finite incidence-token universe and computes `T_1,T_2,T_3` without replacing rich-line multiplicity by an unweighted line count.

For uniform `pi in Omega(F)`,

\[
\boxed{
\mathbb E[\Phi(S_\pi)-\Phi(Z)]
\le
128\left(
\frac{T_1}{t}+
\frac{T_2}{t(t-1)}+
\frac{T_3}{t(t-1)(t-2)}
\right).
}
\]

### Proof

The forbidden diagonal moves every old anchor occurrence and therefore removes every old pair `{P_j,Q_j}`. A new triple with `r` anchor cells appears only when its compatible rank-`r` partial matching is contained in `pi`. AC5la supplies the probability bound, and summing exact certificate occurrences gives the display. QED.

## AC5lc -- canonical improving selector or exact AC1 failure ledger -- PROVED

Put

\[
D_\star=\Phi(S)-\Phi(X),
\qquad
F_\star=\Phi(Z)-\Phi(X)
\]

and

\[
\mathcal N=
128\left(
\frac{T_1}{t}+
\frac{T_2}{t(t-1)}+
\frac{T_3}{t(t-1)(t-2)}
\right).
\]

Enumerate `Omega(F)` in the fixed lexicographic order and evaluate every exact physical successor.

Exactly one output is returned:

1. the lexicographically least `pi` satisfying
   \[
   \Phi(S_\pi)<\Phi(S);
   \]
2. if no such state exists, the complete failure ledger
   \[
   (S,Z,F,t,D_\star,F_\star,T_1,T_2,T_3,\Omega(F))
   \]
   with the assertion that every listed state is nonimproving.

If

\[
D_\star>F_\star+\mathcal N,
\]

then the first route must occur. On the second route the ledger is exactly the physical input required by AC1 second-order concentration; no normalized count is detached from its certificate occurrences.

### Proof

The finite ordered bank either contains an improving state or not. AN4 proves existence under the strict displayed inequality. Failure records every quantity and physical state used by the expectation argument. QED.

## AC5ld -- AN seed schema and serializer manifest population -- PROVED

For every accepted seed:

1. AC5kz populates the prime-minus-one schema fields, physical layer records, bank dictionary and current-star occurrences;
2. AC5la populates a finite `install` operation registry;
3. every operation has a complete precondition, footprint, replacement matching and exact successor;
4. AC5lb populates the direct and layered collateral rows needed to audit the bank;
5. AC5lc supplies either a terminal improving transition or one exact nonterminal concentration input.

Thus the `schema` section and the AN-seed portion of the `serializer` and `frontier` sections of AC5kh are complete. Missing later repair, source-flow, recurrence or rank data are not hidden inside the seed record.

### Proof

AC5kz--AC5lc provide the listed finite records, and AC5ks/AC5ky identify them as accepted schema and operation inputs. QED.

## AC5le -- first physical initial-state-class compiler -- PROVED

Let `I_AN` be the class of all physical alternating-star seeds satisfying AC5kz. There is a uniform finite compiler which, for every member of `I_AN`, returns exactly one of:

1. a canonical improving installation operation;
2. a complete no-improvement AC1 ledger;
3. the first malformed physical seed field.

Therefore the first initial-state class used by the alternating-core chain is no longer an abstract placeholder. Every valid AN bank enters the main manifest through a concrete finite physical record.

This does not assert that every AC restart remains in `I_AN`. Later target, repair, arithmetic and recurrence states require their own manifest population or a proved return to an AN seed.

### Proof

AC5kz decides membership in `I_AN`; AC5la--AC5lc decide the two accepted outputs. All sets are finite and canonically ordered. QED.

## Deterministic audit

`scripts/verify_ac_an_bank_seed_manifest.py` checks 2,500 degree-two forbidden-position banks and 80 complete physical seed instances. It verifies the exact bank count, rank-one through rank-three cylinder probabilities, deterministic installation operations, destruction of every designated star pair, the exact collateral-certificate census, canonical improving selectors and complete no-improvement ledger records.

## Main AC frontier

Only AC remains active. The next physical tasks are:

1. populate AC1's certificate labels on the exact no-improvement ledger;
2. compile the four AC1 structural outputs into physical operation records;
3. instantiate the repair/source and arithmetic rows required after those outputs;
4. connect every later restart either to another manifested seed class or to a permanent boundary certificate;
5. run the reachable manifest from the selected seed.

AC6 and the global no-three-in-line conjecture remain open.
