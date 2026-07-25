# Canonical completion of missing BDA partner supports

**Branch:** `research/alternating-core-chain`

AC3ed--AC3ee leave one exact one-sided-front output: one or both formal adjacent partner cells are absent from the active layer. This note proves that absence is not a denominator-descent obstruction. The current active permutation canonically completes any one- or two-cell partner target by cycles and boundary paths of length at most two. Every blocker intersection with the completed active support—including closure cells—is then repaired by the exact RI5h--RI5m zero/singleton/derangement menu. The original paid radial triple is untouched, so the completed state contains the clean five-cell support of AC3ec and immediately enters the BDA5a--BDA5e decoder.

## Setup

Let `M_0` and `M_1` be the current active and blocker permutation matchings. Fix one paid radial triple

$$
T_h(P)=\{P,P+hu\,d,P+hv\,d\}
$$

and a positive formal adjacent scale

$$
H=h+\sigma q>0.
$$

Assume the mixed collisions of AC3ec do not occur. Put

$$
U_H=P+Hu\,d,
\qquad
V_H=P+Hv\,d.
$$

The five intended support cells have distinct rows and columns. Let

$$
Z\subseteq\{U_H,V_H\},
\qquad
1\le |Z|\le2,
$$

be the cells absent from `M_0`. Cells of `Z` may be empty or may lie in `M_1`.

Write `z_i=(c_i,r_i)` and define its current row-owner column

$$
y_i=M_0^{-1}(r_i).
$$

Since `z_i` is not active, `y_i\ne c_i`. Distinct desired rows give distinct owner columns.

## AC3ep -- canonical one- and two-cell active completion -- PROVED

The partial map

$$
c_i\longmapsto y_i
$$

has exactly the following component types.

1. If `|Z|=1`, there is one boundary path
   $$
   c_1\longrightarrow y_1,
   \qquad y_1\notin\{c_1\}.
   $$
2. If `|Z|=2`, there is exactly one of:
   - one directed 2-cycle;
   - one length-two boundary path;
   - two disjoint length-one boundary paths.

For every directed cycle, replace the current matching cells on its target columns by the desired cells. For every boundary path

$$
c_1\longrightarrow\cdots\longrightarrow c_k\longrightarrow y,
$$

install the desired cells on `c_1,...,c_k` and add the closure cell

$$
q=(y,M_0(c_1)).
$$

The resulting active set `M_0^+` is a permutation matching on exactly the same global rows and columns as `M_0`, contains every cell of `Z`, changes at most four active columns, and uses zero, one, or two closure cells.

### Proof

The owner columns are distinct, so the partial functional digraph has indegree and outdegree at most one. With at most two target columns, the listed components are exhaustive. Along a cycle, desired rows are exactly the old rows on the cycle. Along a boundary path, desired rows are the old rows of the next columns, and the closure cell returns the first removed row at the outside endpoint. Distinct components have disjoint target rows and owner columns, so their union is a matching. QED.

## AC3eq -- paid-support preservation and full blocker repair -- PROVED

The completion `M_0^+` leaves all three cells of `T_h(P)` unchanged. Every active closure cell also lies outside the five intended radial-support rows and columns.

Let

$$
N^+=M_0^+\setminus M_0
$$

be the new active cells, including targets and closure cells, and put

$$
t=|N^+\cap M_1|.
$$

Since `|N^+|\le4`, we have `0\le t\le4`. There is a legal repaired blocker permutation `M_1^+` disjoint from `M_0^+`:

1. `t=0`: leave `M_1` unchanged;
2. `t=1`: choose any other blocker cell and transpose the two blocker rows;
3. `t\ge2`: apply any fixed-point-free permutation to the rows of the `t` selected blocker cells.

Hence the completed two-layer state is legal and contains the full clean five-cell support

$$
P,
\quad P+hu\,d,
\quad P+hv\,d,
\quad U_H,
\quad V_H.
$$

### Proof

The target columns and rows of `U_H,V_H` are distinct from all rows and columns of `T_h(P)`. If an owner column `y_i` were a paid-support column, then its current active row `r_i` would be a paid-support row, contradiction. A closure row is the old active row of a target column and cannot be a paid-support row because that target column is not a paid-support column. Thus the paid triple and all five support cells survive completion.

Every cell in `N^+\cap M_1` is both a desired active cell and a current blocker cell. In the singleton case, transposing it with any other blocker cell replaces the two blocker cells by opposite rectangle corners. Neither replacement can be active: one uses the selected active column with a different row, and the other uses the selected active row in a different column. For `t\ge2`, a fixed-point-free row permutation has the same property on every selected column. Rows and columns are preserved, and unselected blocker cells are unchanged. This is exactly the RI5h--RI5m repair argument. QED.

## AC3er -- install-then-decode composite menu -- PROVED

Apply the nonempty BDA5a--BDA5e decoder menu to the clean pair in `(M_0^+,M_1^+)`. Every composite state obtained by

1. the canonical active completion;
2. one legal blocker repair from AC3eq; and
3. one local BDA decoder state

is a legal two-layer permutation state. Every such state destroys the original paid triple `T_h(P)`.

The active closure cells from AC3ep lie outside the five support rows and columns, so the BDA decoder does not disturb them. The unordered adjacent-pair ticket of AC3ef is consumed by the composite transition.

### Proof

AC3eq supplies a legal state with the exact BDA5a support. BDA5a--BDA5e preserve both permutation layers and destroy the occupied radial triple. Their active changes use the five support rows and columns, while the closure cells use none of them. Sequential composition is therefore legal. QED.

## Composite repair envelopes

For one missing-support record `R`, let `E(R)` contain every cell used by:

- the original and completed active matchings on the completion components;
- every legal blocker transposition or derangement;
- the five-cell radial support and every BDA decoder state;
- the private occupied-slot paid bucket;
- every potential, row, column, protected-bank, replacement, and feasibility scope meeting those cells.

Build the canonical AC3v primal graph on these complete envelopes. AC3ee already gives, for every `K>=1`, either a finite scoped overload or an independent privately paid family of total weight at least `W_miss/K`.

## AC3es -- exact composite product criterion and seven-mask router -- PROVED

Let `I` be an independent missing-support family returned by AC3ee, and let

$$
D=\sum_{R\in I}w_R
$$

be its private occupied-side payment. Choose independently and uniformly from each finite composite menu of AC3er.

For a newly created collateral triple, record the nonempty subset of stages whose new-cell alphabets it meets:

- `A`: active completion targets or closure cells;
- `B`: blocker-repair cells;
- `D`: BDA decoder cells.

There are seven nonempty masks

$$
A,\ B,\ D,\ AB,\ AD,\ BD,\ ABD.
$$

Let `C_S` be the exact expected collateral weight of mask `S`. Then

$$
\boxed{\mathbb E[\text{destroyed certified payment}]=D}
$$

and

$$
\boxed{
\mathbb E[\text{created collateral}]
=
\sum_{\varnothing\ne S\subseteq\{A,B,D\}}C_S.
}
$$

If

$$
D>
\sum_{\varnothing\ne S\subseteq\{A,B,D\}}C_S,
$$

one legal product state strictly lowers the paid triple potential. If no product state improves, one exact stage mask has expected collateral at least

$$
\boxed{D/7.}
$$

Combining AC3ee with AC3eg, unless a finite scoped overload occurs, a failed endpoint-origin product returns one exact stage-mask profile of weight at least

$$
\boxed{\frac{W_x}{224KR\rho L}}
$$

and a failed oriented-variation product returns one of weight at least

$$
\boxed{\frac{W_x}{448KR\rho L}}.
$$

The factor `rho` is omitted in the same exceptional AC3ar cases as before.

### Proof

AC3v makes every deterministic product state legal and additive across selected envelopes. AC3w makes private occupied-slot payment additive. AC3er destroys every represented paid triple. Every new triple contains a cell changed by at least one stage, so the seven masks partition all created collateral. Linearity of expectation gives the identities. Failure gives a seven-term sum at least `D`; weighted pigeonhole gives `D/7`. Substitute AC3eg and AC3ee. QED.

## Consequence

The missing-support output no longer branches into informal installation, blocker, descent, or faithfulness cases.

- Every one- or two-cell partner target has a canonical active completion on at most four columns.
- Every blocker occupancy on the new target and closure cells is repairable; its size is at most four.
- The original paid radial triple survives installation and then enters an executable clean-pair decoder.
- Immediate adjacent-scale reversal remains ticketed.
- A failed composite bank returns one of seven exact completion/repair/decoder incidence masks.

The remaining work is arithmetic termination of those seven masks and their finite AC2d overload labels, not existence of a partner installation.

## Finite check

`scripts/verify_ac_bda_missing_support_completion.py` normalizes the active matching to the identity and exhausts one- and two-cell partial targets, all four active component types, disjoint blocker permutations, blocker intersections through size four, protected three-cell supports, weighted seven-mask ledgers, and the `1/224` and `1/448` constants.