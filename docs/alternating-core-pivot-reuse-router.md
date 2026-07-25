# Finite decorated-pivot reuse and saturation router

**Branch:** `research/alternating-core-chain`

AC3gg--AC3gm give every realized created-certificate rank the same union-safe pivot decoder. The remaining local recycling question is whether the same pivot transition can be used indefinitely after the parent configuration changes. This note gives a finite polynomial signature for every canonical pivot rectangle and an exact new-signature-or-saturation router. It also combines those exposures with AC2d support descent in one bounded integer potential.

## Canonical partner decoders

Fix a legal two-layer permutation state on an `n by n` grid, with `n>=3`. Let

$$
z=(c_0,r_0)
$$

be a current pivot in layer `ell`. For every partner column `c_1!=c_0`, let

$$
a=(c_1,r_1)
$$

be the unique cell of layer `ell` in that column. Apply the AC3fs rectangle switch to `z,a` and use the following deterministic opposite-layer repair.

1. If neither cross is blocked, use no auxiliary column.
2. If only the pivot-column cross is blocked, use the partner column as in AC3fs.
3. If only the partner-column cross is blocked, use the least column outside `{c_0,c_1}`.
4. If both crosses are blocked, use the least column outside `{c_0,c_1}` in the AC3fs oriented three-cycle.

Thus every partner column gives one canonical legal decoder which removes `z` from the full union.

## Decorated local signature

Fix a finite retained role alphabet `Lambda`, of size `L`. A canonical pivot signature records:

- the pivot layer `ell`;
- one role label `lambda in Lambda`;
- the pivot and partner columns `c_0,c_1`;
- the pivot-layer rows `r_0,r_1`;
- the opposite-layer rows in `c_0,c_1`;
- the occupancy case;
- when used, the canonical auxiliary column `c_2` and its opposite-layer row.

No cell outside these at most three columns affects the local transition.

## AC3gn -- finite exact pivot-signature alphabet -- PROVED

The decorated signature determines the complete canonical local pivot transition, including every removed and inserted cell in both layers.

For a fixed grid size `n` and role alphabet size `L`, the signature universe satisfies the safe polynomial bound

$$
\boxed{
|\Sigma_{\rm piv}(n,L)|
\le 2L n^8.
}
$$

For one fixed state, pivot and role label, the `n-1` partner columns give `n-1` distinct signatures.

### Proof

The recorded pivot-layer rows determine the switched diagonal. The two opposite-layer rows determine the occupancy case. In the two cases requiring an outside column, the deterministic least-column rule determines `c_2`, while its recorded opposite row determines the singleton transposition or three-cycle. Hence the complete local move is determined.

For the count, use at most two layers, `L` labels, `n^2` pivot cells, `n^2` ordered partner column/row choices, `n^3` possible opposite-layer row data on the support columns, and `n` possible auxiliary columns. This gives at most `2L n^8`. The partner column is part of the signature, so different partners give different signatures. QED.

## AC3go -- new signature or full partner saturation -- PROVED

Let `E` be the set of pivot signatures already exposed in the current closure attempt. Fix a current pivot `z` and one retained role label `lambda`. Let

$$
\Sigma(z,\lambda)
$$

be the `n-1` canonical signatures obtained from all partner columns in the pivot layer.

Exactly one of the following holds.

1. **New decorated pivot.** Some signature in `Sigma(z,lambda)` is outside `E`. Choosing its partner gives a legal paid pivot transition and strictly enlarges `E`.
2. **Full partner saturation.** Every signature in `Sigma(z,lambda)` already belongs to `E`.

The first alternative can occur at most `|Sigma_piv(n,L)|` times before a terminal, overload or saturation output.

### Proof

The two alternatives partition whether `Sigma(z,lambda)\setminus E` is empty. AC3fs gives legality and union-level destruction for every partner. Each first-alternative transition adds a previously absent element to the finite signature universe, so their total number is bounded by its size. QED.

## AC3gp -- weighted saturated-role output -- PROVED

Let one current pivot bucket have total paid certificate weight `W`, and let every certificate carry one of the `L` retained role labels. One role class has weight at least

$$
\boxed{W/L.}
$$

Apply AC3go using that label. The result is either:

1. a new-signature pivot transition destroying the entire bucket of weight `W`; or
2. a full partner-saturation record at `z` carrying current paid role weight at least `W/L`.

The saturation record retains the pivot, layer, all `n-1` partner columns, the exact local blocker rows for every current partner signature, and the complete arithmetic/geometric role label.

### Proof

Weighted pigeonhole gives the role class. The pivot decoder removes `z`, so it destroys every certificate in the bucket, not only the selected role class. If no new signature exists, AC3go gives saturation and the selected role class supplies the displayed paid mass. QED.

## AC3gq -- combined overload-descent and pivot-exposure potential -- PROVED

Fix one finite AC2d object universe `O`, with

$$
N=|\mathcal O|,
$$

and one pivot-signature universe `Sigma_piv`. During an epoch, let `U` be the current nonempty AC2d support and let `E` be the exposed pivot-signature set. Allow only:

1. a pure labelled AC2d descent `U' subsetneq U`, with `E` unchanged;
2. a new-signature pivot transition, with `|E'|>=|E|+1` and arbitrary nonempty `U' subseteq O`;
3. a terminal compatible bank, heavier object, broad same-label star, BDA/RI/carry output, improvement or full partner-saturation record.

Then

$$
\boxed{
\Xi_{\rm piv}(U,E)
=
N|E|+N-|U|
}
$$

increases by at least one on every nonterminal transition and satisfies

$$
0\le\Xi_{\rm piv}
\le
N|\Sigma_{\rm piv}|+N-1.
$$

Consequently every such epoch terminates after at most

$$
\boxed{N|\Sigma_{\rm piv}|+N-1}
$$

nonterminal steps.

### Proof

On a labelled descent, `|E|` is fixed and `|U|` decreases. On a new-signature transition, the first term increases by at least `N`, while replacing one nonempty support by another can decrease `N-|U|` by at most `N-1`. The net increase is at least one. The displayed ceiling is immediate. QED.

## Consequence and remaining frontier

Repeated decorated pivot rectangles are no longer an uncontrolled source of cycling. A mixed epoch of same-role AC2d recursion and pivot execution terminates unless it returns one of the already named structural outputs or a full partner-saturation record.

The remaining no-recycling work is now concentrated in the saturation alternative: classify a pivot whose complete current partner menu has already appeared with the same retained local decorations. That output is a finite exact local recurrence profile, suitable for carry/BDA/RI classification or a global fixed-centre fan argument. The five BDA affine chains and AC5 reverse-scale audit remain separate.

## Finite check

`scripts/verify_ac_pivot_reuse_router.py` exhausts normalized disjoint permutation states on grids three through six, constructs every canonical partner signature and repair, verifies signature determinism and partner distinctness, checks every exposed-subset dichotomy, weighted role localization, the `2Ln^8` bound and every transition inequality for `Xi_piv`.
