# Archived and public prime-seed provenance

Most compact row-pair codes in
`experiments/archived-prime-seed-codes.json` were transcribed on 2026-07-27
from Achim Flammenkamp's public no-three-in-line configuration archive:

```text
https://wwwhomes.uni-bielefeld.de/achim/no3in/configurations/
```

The retained Flammenkamp archive paths are:

```text
n16_rot4
n18_rot4
n22_rot4
n28_rot4
n30_rot4
n60_rot4
n66_rot4
n72_rot4
```

The notation description is in the archive readme:

```text
https://wwwhomes.uni-bielefeld.de/achim/no3in/readme.html
```

The `p=47` record has separate provenance. Its source is the first RLE line of

```text
repository: mvr/no-three-in-line
path:       results/c4-46.out
blob:       2b978710f7c315ad49020f449e81842e1c88fd06
```

The RLE is retained verbatim in
`experiments/p47-public-rle-certificate.json`. The standard row-pair code in
the shared compact-code suite is regenerated from that independently decoded
cell set.

No proof claim is imported from either source. Repository checkers decode each
record, verify saturation, test every exact integer determinant, and derive
their own two-permutation decomposition and relative cycle partition.
