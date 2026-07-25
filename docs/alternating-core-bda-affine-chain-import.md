# Alternating-core import of fixed-cell BDA affine chains

**Branch:** `research/alternating-core-chain`

BDA5ap--BDA5ar collapse every high-row or high-column affine-chain output to one exact current cell and one fixed radial line. In the BDA4f parity family, adjacent radial pairs are slot-disjoint, so the selected current triples through that cell are factor-conservative paid resources. This note imports the collapse directly into the all-rank pivot transition.

## AC3hf -- fixed-cell localization of a BDA high-load output -- PROVED

Let an exact BDA profile on the alternating branch have a high row or column with incident paid pair-record weight `H`. One exact support role and one current union cell `Q` retain weight at least

$$
\boxed{
H/10.
}
$$

The retained records satisfy one of the anchor identities

$$
P=Q
$$

or

$$
P(h)=Q-(h+s q)w\,d,
\qquad
s\in\{0,1\},
\quad
w\in\{u,v\},
$$

and every cell in every retained radial-pair support lies on

$$
\boxed{
\ell_Q=Q+\mathbb R d.
}
$$

### Proof

This is BDA5ap--BDA5ar, with the exact denominator, scalar, direction, residue, blocker and decoder fields retained by the AC3an profile localization. QED.

## Selected current payment through `Q`

For a retained root-role record, both adjacent radial triples contain `Q=P`. For a retained role `(s,w)`, select the radial triple at scale `h+s q`; its role-`w` endpoint is exactly `Q`.

The paid weight of an adjacent pair is bounded by the weight of each of its two radial triples. Therefore the selected `Q`-containing triple can carry the full pair-record payment.

## AC3hg -- factor-conservative fixed-cell payment -- PROVED

Assume the retained records come from one BDA4f parity family and exact duplicate occurrences have been aggregated. Then the selected `Q`-containing radial triples are distinct current certificates, all contain `Q`, and have total paid weight at least

$$
\boxed{
H/10.
}
$$

Hence they form one private pivot bucket at `Q`.

### Proof

At one anchor, a BDA4f parity family uses every radial slot at most once. A retained role chooses one of the two slots in its adjacent pair, so no selected radial occurrence is reused at that anchor. Exact occurrence aggregation removes repeated copies of the same canonical record. Distinct anchors give distinct root-role occurrences in the fixed arithmetic profile. Each selected triple contains `Q` by the preceding role audit and has available weight at least the pair-record weight. Summing gives the bound. QED.

The parity and exact-occurrence hypotheses are essential. Without them, record weight must not be silently counted as distinct certificate payment.

## AC3hh -- affine-chain pivot transition -- PROVED

Apply the union-safe pivot rectangle decoder at `Q` to the private bucket from AC3hg. Every local pivot state removes `Q` from the full two-layer union and destroys certified payment

$$
\boxed{
D\ge H/10.
}
$$

Exactly one of the following holds.

1. One legal pivot state strictly improves the union-triple potential.
2. The pivot comparison fails and one next-generation created-cell rank has expected weight at least
   $$
   \boxed{
   H/30.
   }
   $$
3. The pivot recurrence router returns a new decorated signature, a full line-partner saturation, a cross-arm continuation, an old-axis saturation or an explicit AC3fr overload, all with the fixed BDA arithmetic role attached.

### Proof

AC3hg gives one current pivot bucket with private payment at least `H/10`. AC3gh supplies a union-safe local decoder. The exact product comparison for one pivot menu is AC3gj; failure splits its created collateral into three ranks and therefore returns at least `D/3>=H/30`. Recurrence and overload outputs are AC3gn--AC3he. QED.

## Consequence

The five BDA affine anchor chains are no longer open terminal states on the alternating branch. High row or column load gives, at total loss `1/10`, one exact fixed current cell, one radial line and one factor-conservative paid pivot bucket. The remaining BDA frontier consists of:

- ordinary or reflected co-anchor outputs not yet passing through the support audit;
- finite-profile recurrence after the resulting pivot outputs;
- and the remaining bounded-denominator cycle assembly.

## Finite check

`scripts/verify_ac_bda_affine_chain_import.py` checks all five role choices, selected-triple containment of `Q`, parity-slot injectivity, the `H/10` payment transfer and the `H/30` failed-pivot constant.