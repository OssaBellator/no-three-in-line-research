# Canonical affine full-selector obstruction

The blockwise reversal of PX25 removes the unmodified `2 x 5` defect gap for
selected side-five factors.  PX31 shows that, inside the explicit one-inner-layer
family, normalized affine block maps produce only the already known side-ten
witness.

This note tests the larger exact full selector against the canonical factor used
for the 35-line unsatisfiable core PX27.

## 1. Normalized affine hosts

Use the canonical outer factor

\[
\sigma_0=(0,1),
\qquad
\sigma_1=(1,0),
\]

and the canonical inner factor

\[
\tau_0=(0,1,3,4,2),
\qquad
\tau_1=(2,0,4,1,3).
\]

Fix the first coarse row and column digit maps to the identity.  In the second
coarse row and column blocks independently choose

\[
\alpha_1(u)=au+b\pmod5,
\qquad
\beta_1(u)=cu+d\pmod5,
\]

with nonzero multipliers `a,c`.  Test all four global radix orientations and
allow **every** spanning degree-two state in the resulting four-regular host.
There are

\[
20\cdot20\cdot4=1600
\]

such hosts.

## Theorem PX32 -- PROVED FINITE

None of the 1600 normalized affine hosts for the canonical factor pair contains
a no-three spanning degree-two state.

Equivalently, the exact full-selector width-three CNF is unsatisfiable for every
pair of normalized affine second-block maps and every orientation.

### Proof

For each host, expose scalar rows in order and enumerate every two-element subset
of its four incident cells.  Track scalar column degrees and prune when the
remaining rows cannot complete degree two.  Whenever a new cell is inserted,
reject the branch if it completes a real-collinear triple with two previously
selected cells.  The exact search returns no model in all 1600 cases. \(\square\)

## 2. Interpretation

PX32 prevents an overly optimistic conclusion from the side-ten witness.

- Blockwise affine maps are genuinely useful for some side-five factors.
- They are not universal even when combined with the full degree-two selector.
- The canonical 35-line obstruction is not removed by merely choosing a better
  normalized affine slope or translation in the second blocks.

The theorem does not say that the same 35 line clauses remain an unsatisfiable
core after every affine relabelling.  It only proves that the complete exact
selector remains unsatisfiable.

A successful universal enlargement must therefore go beyond this normalized
affine family, for example by allowing:

1. independent maps in all coarse blocks;
2. non-affine block permutations;
3. additional factor-compatible cells or offsets;
4. maps chosen jointly from the secant structure of both factor layers.

## 3. Verification

Run

```bash
python scripts/verify_product_canonical_affine_full_selector.py
```

The script imports the independently checked blockwise-host and exact-selector
routines and exhausts all 1600 hosts using only the standard library.  PX32 is a
finite obstruction, not a symbolic classification of all affine product hosts.
