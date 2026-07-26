# New-cell propagation of AC5 anchored event inventories

**Branch:** `research/alternating-core-chain`

AC5o reduces the current and protected band expectations to three explicit
inventories.  The unresolved term `A_{2,J}` is the anchored assignment-pair
inventory.  L3 bounds it by `8n` times the maximum possible-cell pair-shadow,
but a multistep installation can change the possible-cell set between steps.

This note propagates the pair-shadow cap through those changes.  The only new
input is the number of target--partner assignments which become newly possible.
Every such assignment contributes at most two possible inserted cells, while a
height-`H` line contains only `ell_H` grid cells.

## Band notation

For one line band `J`, let every line in the band contain at most `ell_J` grid
cells and put

\[
m_J=(\ell_J-2)_+.
\]

Let `Z_0` be the initial possible-cell set.  Assume every unchanged selected
anchor satisfies

\[
\lambda_J(a;Z_0)\le\Theta_{J,0}.
\]

A complete installation path has intermediate possible-cell inventories

\[
Z_0,Z_1,\ldots,Z_s.
\]

Before adding genuinely new cells at step `i`, arbitrary targets, partners and
possible cells may be deleted.  Let `k_i` be the number of target--partner
assignments newly possible at that step, and write

\[
K_j=\sum_{i=1}^j k_i.
\]

Every new assignment has at most two inserted cross-cells.  Duplicates only
reduce the genuinely new cell set.

## AC5q -- pathwise pair-shadow propagation -- PROVED

For every unchanged anchor and every intermediate inventory,

\[
\boxed{
\lambda_J(a;Z_j)
\le
\Theta_{J,0}+3m_JK_j.
}
\]

In particular, an initial reserve

\[
\boxed{
\Theta_J-\Theta_{J,0}
\ge
3m_JK_s
}
\]

keeps the pair-shadow at most `Theta_J` throughout the entire installation
path.

### Proof

Pure deletion cannot increase pair-shadow.  At step `i`, at most `2k_i`
genuinely new cells are added.  Fix an anchor.  Each new cell forms at most
`m_J` old--new anchored pairs and contributes at most `m_J/2` new--new pairs
after double counting.  Hence the increase is at most `3m_Jk_i`.  Sum over the
first `j` steps. QED.

No bound is claimed on `K_j` here.  The theorem converts that geometric
quantity into the exact pair-shadow loss.

## AC5r -- propagated anchored assignment-pair inventory -- PROVED

Assume the standard cell-realisation multiplicity: every possible inserted cell
is produced by at most two target--partner assignments.  Let `A_{2,J}^{(j)}` be
the complete anchored two-assignment event inventory formed from `Z_j`.  Then

\[
\boxed{
A_{2,J}^{(j)}
\le
8n\bigl(\Theta_{J,0}+3m_JK_j\bigr).
}
\]

### Proof

For one unchanged anchor, every compatible possible-cell pair has at most four
assignment-pair realisations.  There are at most `2n` selected anchors.  Thus
L3 gives

\[
A_{2,J}^{(j)}
\le
8n\max_a\lambda_J(a;Z_j).
\]

Apply AC5q. QED.

The inventory may overcount one created triple through several anchors or
assignment representations; AC5l permits that overcounting.

## AC5s -- explicit band expectation after inventory growth -- PROVED UNDER THE AC5o EVENT CONTRACT

Retain AC5o's notation: the spread law is `K/p`-spread, the certified batch has
size `t`, and the nonanchored two- and three-choice inventories obey

\[
U_{2,J}^{(j)}\le4\ell_Jtp,
\qquad
U_{3,J}^{(j)}\le8\ell_Jt^2p^2.
\]

Then the expected number of newly created triples in band `J` at intermediate
step `j` is at most

\[
\boxed{
\Gamma_J^{(j)}
=
\frac{8K^2n}{p^2}
\bigl(\Theta_{J,0}+3m_JK_j\bigr)
+
\frac{4K^2\ell_Jt}{p}
+
\frac{8K^3\ell_Jt^2}{p}.
}
\]

### Proof

Use AC5r for the anchored part of `M_{2,J}` and the two displayed AC5o
inventories for the remaining rank-two and rank-three events.  Multiply by the
spread probabilities `(K/p)^2` and `(K/p)^3` as in AC5l. QED.

The first `K` in the formula is the spread constant; `K_j` is the cumulative
new-assignment count.  They are deliberately distinct quantities.

## Current and protected bands

At scale `H`, one may use

\[
\ell_{\rm cur}
=
1+\left\lfloor\frac{n-1}{H}\right\rfloor,
\qquad
\ell_{\rm high}
=
1+\left\lfloor\frac{n-1}{2H}\right\rfloor,
\]

and

\[
m_{\rm cur}=(\ell_{\rm cur}-2)_+,
\qquad
m_{\rm high}=(\ell_{\rm high}-2)_+.
\]

Use separate initial caps and cumulative newly possible assignment counts for
the two bands when their admissibility filters differ.

## AC5t -- new-assignment sufficient criterion for multistep safety -- PROVED UNDER THE COMPLETE INVENTORY HYPOTHESES

Let `Gamma_cur` be AC5s's bound for the final current-band inventory.  At each
installation step `j`, let `Gamma_high,j` be AC5s's protected-band bound using
the protected possible-cell inventory present at that step.  If

\[
\boxed{
\Gamma_{\rm cur}
+t\sum_{j=1}^s\Gamma_{{\rm high},j}
<t,
}
\]

then one complete installation path preserves every settled higher band at
every intermediate step and creates at most `t-1` final current-band triples.
Consequently it strictly decreases `Psi_H`.

### Proof

AC5s supplies the complete expectation bounds required by AC5p.  Substitute
them into AC5p's augmented-badness criterion. QED.

## Corrected AC5 frontier

For every concrete BDA, RI, phase, petal or owner-repair menu, the anchored
pair-shadow part of the AC5 audit is now reduced to the following explicit
inputs:

1. the initial band caps `Theta_{J,0}`;
2. the cumulative counts `K_j` of assignments which become newly possible;
3. the line-length factors `m_J`;
4. the spread and remaining rank-two/rank-three event inventories already used
   by AC5o.

Thus “uniform intermediate-state stability” is no longer a qualitative field.
Either prove the required bound on `K_j`, show that most newly possible
assignments produce duplicate cells or pair events, or route a large `K_j`
class to current paid incidence.  The latter is exactly the GC3 new-pair/reuse
frontier.

## Finite check

`scripts/verify_ac5_new_cell_inventory.py` exhausts old/new possible-cell
partitions on small grids, verifies the per-step `3m_Jk_i` increase, checks
cumulative path propagation and audits the substitution into the AC5o and AC5p
formulas over a finite parameter grid.
