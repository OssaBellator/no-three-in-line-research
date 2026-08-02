# Atomic transposition strict-sign-or-child for all line certificates

PX319--PX322 close the packet residue by inspecting one correction at a time.
The same argument is not packet-specific.  Any admissible transposition which
moves an endpoint carrying assigned old line certificates has an exact
support-one creation ledger.  If its old destruction does not dominate, one of
its prospective cells has a clean-star obstruction or the two new cells lie on
a loaded line.

Bounded forbidden degree guarantees an admissible partner for every endpoint
outside the terminal range.

## 1. Every nonterminal endpoint has a transposition partner

Relabel the current matching as the diagonal on `[m]`.  Let `F` be the inherited
forbidden-position graph, of maximum row and column degree at most `Delta`, and
assume the current diagonal belongs to `F`.

For distinct labels `r,s`, call the transposition `r<->s` admissible when both
crossed cells

\[
(r,s),\qquad(s,r)
\]

lie outside `F`.

### Theorem PX323 -- PROVED

For every label `r`, at most `2Delta` partner labels `s` give an inadmissible
transposition.  Hence `r` has at least

\[
\boxed{m-1-2\Delta}
\]

admissible partners.

In particular, if

\[
\boxed{m\ge2\Delta+2,}
\]

every endpoint has an admissible transposition partner.

### Proof

At most `Delta` choices of `s` satisfy `(r,s) in F`, by the row-degree bound.
At most `Delta` choices satisfy `(s,r) in F`, by the column-degree bound.
Their union has size at most `2Delta`.  Remove the forbidden choice `s=r` from
the `m` labels to obtain the displayed lower bound. \(\square\)

The same proof in unrelabelled coordinates uses the bijection `s -> M(s)`.

## 2. Exact atomic destruction/creation inequality

Suppose row `r` carries at least one assigned old certificate of one of the
ancestor-safe line types from PX278: clean-star, loaded-line, radial,
coordinate-field, or mixed-shadow.  Choose an admissible partner `s`.

Let `d_e` be the number of assigned current-level certificates destroyed by
removing the two old selected cells on rows `r,s`.  Then `d_e>=1`.

Let `f_e^1,f_e^2` be the two new crossed cells and let `X_e` be the configuration
with the two old cells deleted.  Define

\[
c_e
=
\mu_e(f_e^1)+\mu_e(f_e^2)+\lambda_e
\]

as in PX307.

### Theorem PX324 -- PROVED

Executing only this admissible transposition satisfies

\[
\boxed{
\Phi(M^e)-\Phi(M)
\le
-d_e+c_e.
}
\]

If `d_e>c_e`, the transposition strictly lowers the full triple potential.

### Proof

All `d_e` assigned certificates disappear because their assigned old endpoint
cells are removed.  Ancestor safety gives uniqueness of the historical row
position, so the crossed cells cannot recreate those paid certificates.
PX307 lists every newly created triple containing one or both crossed cells,
and counts exactly `c_e` of them.  Other old triples destroyed by the switch
only improve the inequality. \(\square\)

## 3. Atomic sign failure creates a structured child

Assume the relevant line occupancy is at most `K`.

### Theorem PX325 -- PROVED

If the admissible transposition of PX324 is not certified strictly improving,
then after executing it there is either

1. a prospective clean star of order at least

   \[
   \boxed{
   \left\lceil\frac{d_e}{3K}\right\rceil,
   }
   \]

   centred at one new cell; or

2. a loaded line containing at least

   \[
   \boxed{
   \left\lceil\frac{d_e}{3}\right\rceil+2
   }
   \]

   points, including both new cells.

### Proof

Failure of `d_e>c_e` gives `c_e>=d_e`.  One of the three nonnegative terms in
`c_e` is at least `ceil(d_e/3)`.  A large `mu` term gives the clean star by
PX228.  A large `lambda` term counts fixed points on the line through the two
new cells and gives the loaded-line outcome. \(\square\)

All newly created certificates are assigned to the next causal level.  The
current unresolved coordinate falls by `d_e`, while PX278 prevents recurrence
of the paid parent certificates.

## 4. General strict-sign-or-child theorem

### Corollary PX326 -- PROVED

Consider a current matching block in which every unresolved clean-star,
loaded-line, radial, coordinate-field, or mixed-shadow certificate has been
injectively assigned to a moved endpoint as in PX240--PX243.

At least one of the following holds.

1. `m<=2Delta+1`, so the block is in the exact terminal range of PX273--PX293.
2. An admissible atomic transposition strictly lowers `Phi`.
3. An admissible atomic transposition lowers the shallowest unresolved
   coordinate and creates a deeper clean-star or loaded-line child quantified
   by PX325.

Consequently the diffuse unassigned linear line-certificate sector satisfies
the strict-sign-or-child interface of PX280 outside the exact terminal core.

### Proof

If `m>=2Delta+2`, choose an endpoint carrying an unresolved assigned
certificate and apply PX323.  Its admissible partner gives `d_e>=1`.
PX324--PX325 give items 2 or 3.  Otherwise item 1 holds. \(\square\)

This replaces the missing general Bernoulli first-order theorem by a stronger
atomic statement.  Large banks remain useful for quantitative direct descent,
but they are unnecessary for causal termination.

## 5. Verification

Run

```bash
python scripts/verify_product_atomic_line_child.py
```

The verifier exhausts diagonal-forbidden graphs through order four, checks the
`m-1-2Delta` partner bound row by row, and verifies the exact integer
strict-or-star-or-line ledger.
