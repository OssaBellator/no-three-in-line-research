# Public RLE p=47 certificate diagnostic

The first record of `results/c4-46.out` in the public
`mvr/no-three-in-line` repository is stored verbatim in
`p47-public-rle-certificate.json`, together with the independently derived
permutation, signed-pair, relative-cycle, and compact row-pair representations.
The source blob recorded by the diagnostic is
`2b978710f7c315ad49020f449e81842e1c88fd06`.

Run:

```bash
python scripts/check_p47_public_rle_certificate.py \
  experiments/p47-public-rle-certificate.json
```

The checker does not trust any derived field. It decodes the RLE, verifies 92
distinct points on `[46]^2`, checks exactly two points in every row and column,
tests quarter-turn invariance, constructs the swapped equivariant colouring,
reconstructs the signed pair cover and relative permutation, regenerates the
compact code, and evaluates all

```text
C(92,3)=125580
```

integer determinants. Every determinant is nonzero and the minimum absolute
value is one.

The external repository is used only as provenance for the finite RLE record.
No claim about its search programme is needed for the independent certificate
check, and this finite case does not prove the asymptotic seed theorem.
