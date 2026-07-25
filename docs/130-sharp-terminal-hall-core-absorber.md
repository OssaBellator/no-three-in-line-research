# One-point absorption of the sharp terminal Hall core

PX271 classifies the unique nonexecutability obstruction at order

\[
m=2\Delta-1:
\]

a saturated forbidden `K_(Delta,Delta)` between `Delta` rows and `Delta`
columns. In a decoder block the row and column labels are identified by the
current endpoint matching. The two Hall-core sides must therefore share at
least one label.

Deleting one common label breaks the obstruction completely. The remaining
rows and columns split into two complete allowed cross-blocks, producing an
explicit principal rematching of all other endpoints.

## 1. Principal one-label trimming

Let the row and column label sets both be `[m]`. Let `F` have maximum row and
column degree at most `Delta`, put `G=K_(m,m) minus F`, and assume

\[
\boxed{m=2\Delta-1}
\]

and that `G` has no perfect matching.

PX271 supplies sets `S,B subseteq [m]` with

\[
|S|=|B|=\Delta,
\qquad
S\times B\subseteq F.
\]

### Theorem PX281 -- PROVED

For every label

\[
x\in S\cap B,
\]

the principal residual graph on

\[
J=[m]\setminus\{x\}
\]

has an allowed perfect matching.

More explicitly, the two allowed complete bipartite blocks

\[
\boxed{
(S\setminus\{x\})\times([m]\setminus B)
}
\]

and

\[
\boxed{
([m]\setminus S)\times(B\setminus\{x\})
}
\]

have equal side sizes `Delta-1`; choosing one perfect matching in each and
taking their union gives an allowed perfect matching on `J`.

### Proof

Since `|S|+|B|=2Delta=m+1`, the intersection `S cap B` is nonempty.
Every row of `S` already has its full forbidden degree `Delta` inside `B`, so
all edges from `S` to `[m] minus B` are allowed. Symmetrically, every column of
`B` is saturated inside `S`, so all edges from `[m] minus S` to `B` are
allowed.

After deleting `x`, the four relevant side sizes are

\[
|S\setminus\{x\}|=|[m]\setminus B|=\Delta-1
\]

and

\[
|[m]\setminus S|=|B\setminus\{x\}|=\Delta-1.
\]

The two complete cross-block matchings are disjoint and cover every label of
`J` on both sides. \(\square\)

## 2. Decoder consequence

### Corollary PX282 -- PROVED

Suppose an order-`m` terminal endpoint family carries one injectively assigned
clean-star, loaded-line, radial, coordinate-field, or mixed-shadow certificate
per endpoint, and its inherited forbidden graph is at the sharp nonexecutable
threshold `m=2Delta-1`.

Then one may leave a single endpoint `x in S cap B` fixed and rematch the other

\[
\boxed{m-1=2\Delta-2}
\]

endpoints while avoiding every inherited forbidden position. All designated
certificates assigned to the moved endpoints are destroyed and remain absent
under the causal ledger of PX278.

Thus the sharp Hall obstruction costs at most one unpaid designated endpoint;
it does not freeze the whole terminal block.

### Proof

Use the principal matching from PX281. Each moved endpoint leaves its unique
historical certificate position, so PX278 applies. \(\square\)

## 3. Strict designated decrease

### Corollary PX283 -- PROVED

If `m>=2`, the one-point sharp-core absorber strictly lowers the designated
coordinate of the causal vector by at least

\[
\boxed{m-1.}
\]

Consequently a sharp Hall core cannot be a terminal obstruction for the
**designated** recursion. Any remaining obstruction after PX281 is entirely
unassigned collateral involving the rematched `m-1` endpoints and can be sent
to the exact terminal optimizer PX273--PX276.

### Proof

All but one designated endpoint certificate are neutralized, while ancestor
coordinates remain zero by PX278. Apply PX277. \(\square\)

PX281--PX283 close the exact sharp Hall obstruction without a new probabilistic
estimate. The unresolved terminal cases are now either below the sharp order,
where PX272 has positive deficiency greater than one, or executable blocks
whose exact optimizer has no improving state.

## 4. Verification

Run

```bash
python scripts/verify_product_sharp_hall_absorber.py
```

The verifier exhausts every forbidden graph through order four, identifies all
sharp nonperfect instances, checks the saturated Hall core, and verifies the
explicit principal perfect matching after deleting every common Hall-core
label.
