# Archived and public prime-seed provenance

Most compact row-pair codes in
`experiments/archived-prime-seed-codes.json` were transcribed or independently
retrieved on 2026-07-27 from Achim Flammenkamp's public no-three-in-line
configuration archive:

```text
https://wwwhomes.uni-bielefeld.de/~achim/no3in/download/configurations/
```

The retained Flammenkamp archive paths are:

```text
n16_rot4
n18_rot4
n22_rot4
n28_rot4
n30_rot4
n40_rot4
n42_rot4
n52_rot4
n60_rot4
n66_rot4
n72_rot4
```

The complete `n40_rot4`, `n42_rot4`, and `n52_rot4` byte streams were fetched
by the temporary GitHub Actions run `30243805031`. Their SHA-256 digests,
byte lengths, record counts, and first standard codes are retained in
`experiments/public-rot4-prime-certificates-p41-p43-p53.json`. The bulk files
are not copied into this repository.

The notation description is in the archive readme:

```text
https://wwwhomes.uni-bielefeld.de/~achim/no3in/readme.html
```

The `p=47` record has separate provenance. Its source is the first RLE line of

```text
repository: mvr/no-three-in-line
path:       results/c4-46.out
blob:       2b978710f7c315ad49020f449e81842e1c88fd06
```

The RLE is retained verbatim in
`experiments/p47-public-rle-certificate.json`.

The `p=59` record is derived from the complete coordinate description on

```text
https://commons.wikimedia.org/wiki/File:No-Three-In-Line_for_N=58.png
```

The page attributes the record to `Prellberg`, dated `2025-10-29`, under
`CC BY-SA 4.0`. The 116 coordinates and attribution metadata are retained in
`experiments/p59-wikimedia-coordinate-certificate.json`.

The standard row-pair codes in the shared suite are regenerated from the
independently decoded archive, RLE, or coordinate sets.

No proof claim is imported from any source. Repository checkers decode each
record, verify saturation, test every exact integer determinant, and derive
their own two-permutation decomposition and relative cycle partition.
