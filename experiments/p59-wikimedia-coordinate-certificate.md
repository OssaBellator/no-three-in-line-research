# Wikimedia coordinate p=59 certificate diagnostic

The coordinate list on the Wikimedia Commons file page
`File:No-Three-In-Line for N=58.png` is retained in
`p59-wikimedia-coordinate-certificate.json` together with its source metadata:
author `Prellberg`, date `2025-10-29`, and licence `CC BY-SA 4.0`.

Run:

```bash
python scripts/check_p59_wikimedia_coordinate_certificate.py \
  experiments/p59-wikimedia-coordinate-certificate.json
```

The checker begins from the 116 coordinate pairs. It independently verifies:

1. 116 distinct cells on `[58]^2`;
2. exactly two points in every row and column;
3. quarter-turn invariance and swapped-only equivariant colouring;
4. the two permutation layers and forced second-layer identity;
5. the signed pair cover, cycle parities, and relative lift;
6. the compact standard row-pair code; and
7. all
   ```text
   C(116,3)=253460
   ```
   integer determinants.

Every determinant is nonzero and the minimum absolute value is one. The exact
maximal-line system on `[58]^2` contains `476358` lines with at least three grid
cells and is therefore satisfied.

The source coordinates are attributed to Prellberg under CC BY-SA 4.0. The
independent verification establishes only this finite prime-minus-one seed; it
does not prove the asymptotic seed theorem.
