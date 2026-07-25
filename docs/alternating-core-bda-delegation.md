# Alternating-core delegation to bounded-denominator absorbers

**Branch:** `research/alternating-core-chain`

AC3am localizes a common-residual obstruction to one finite arithmetic role, but it deliberately does not declare that role absorbable. This note states the exact data contract needed to invoke the independent bounded-denominator branch and proves the finite-profile, scalar-slot, and weighted co-anchor routers under that contract.

## BDA-realized alternating records

A weighted alternating-core record `a` is **arithmetically BDA-realized** when it carries:

- a reduced denominator `q(a)` with `2 <= q(a) <= Q`;
- normalized primitive directions
  $$
  d(a)=(u,v),\qquad e(a)=(r,s),
  $$
  with positive first coordinates and infinity norm at most `M`;
- a nonzero determinant
  $$
  delta(a)=det(d(a),e(a));
  $$
- a scalar residue `xi(a)` modulo `q(a)`;
- an integer anchor `P(a)` and positive radial scale `h(a)`;
- a nonnegative current paid weight `w(a)`;

such that

$$
h(a)delta(a) congruent xi(a) mod q(a).
$$

The **exact arithmetic profile** is

$$
pi(a)=(q(a),d(a),e(a),xi(a)).
$$

The realization is **paid-faithful** when `w(a)` is transferable current defect incidence for the corresponding radial occurrence. It is **support-faithful** when two same-profile records at one anchor with scales `h` and `h+q` have exactly the radial-pair support used by BDA4e and BDA5a--BDA5g, and the BDA row/column conflict relation contains every actual alternating-core incompatibility between such records.

Arithmetic BDA realization is a label theorem. Paid and support faithfulness are geometric installation statements. They are kept separate so that no role is called terminal merely because it has a denominator label.

## AC3an -- finite exact BDA-profile localization -- PROVED

Let

$$
D_M=\{(x,y):1<=x<=M,\ |y|<=M,\ gcd(x,|y|)=1\}
$$

and put `N_M=|D_M|`. A family of arithmetically BDA-realized records uses at most

$$
L_{Q,M}=N_M^2\sum_{q=2}^Q q
$$

exact arithmetic profiles. In particular,

$$
L_{Q,M}
<=
M^2(2M+1)^2\frac{Q(Q+1)}2.
$$

Therefore a family of total paid weight `W` contains one exact profile of weight at least

$$
\boxed{W/L_{Q,M}}.
$$

If the denominator `q` is already fixed by the AC3am role label, the sharper profile count is `qN_M^2`.

### Proof

There are `N_M` possibilities for each primitive direction. For a fixed denominator `q`, the scalar residue has `q` possibilities. Summing over `2<=q<=Q` gives the exact first bound. The crude estimate follows from

$$
N_M<=M(2M+1).
$$

The weighted conclusion is pigeonhole. QED.

## AC3ao -- canonical scalar-slot realization -- PROVED

Fix one nonempty exact profile

$$
pi=(q,d,e,xi)
$$

and put

$$
delta=det(d,e),\qquad
g=gcd(|delta|,q),\qquad
m=q/g.
$$

All scales represented in this profile lie in one residue class modulo `m`.

Let `h_0` and `h_max` be the smallest and largest represented scales and define

$$
J=1+\frac{h_max-h_0}{m},\qquad
h_j=h_0+jm\quad(0<=j<J).
$$

For each represented anchor `P`, aggregate all records with fields `(P,h_j)` into one slot weight

$$
w_{P,j}=\sum_{a:P(a)=P,\ h(a)=h_j}w(a).
$$

Then the total profile weight is exactly

$$
S=\sum_P\sum_{j=0}^{J-1}w_{P,j}.
$$

Thus every exact AC profile has the interlaced scalar-path form required by BDA5z, with a canonical slot index and no loss of paid weight.

### Proof

The congruence `h delta congruent xi mod q` is soluble because the profile is represented. BDA5u, or the elementary reduction obtained by dividing by `g`, shows that its solutions form one residue class modulo `m=q/g`. Hence every represented scale is `h_0+jm` for a unique integer `j` in the displayed range. Aggregating equal anchor/scale records is a partition, proving the weight identity. QED.

## AC3ap -- capped co-anchor and compatibility router -- PROVED FROM BDA4e/BDA5z

Retain one exact profile and its slot weights. Let `A` be the set of represented anchors and fix an atom cap `beta>0`.

Either some anchor-slot atom satisfies

$$
\boxed{w_{P,j}>beta,}
$$

or every atom is capped by `beta`. In the capped case define

$$
Omega_g=
\sum_P\sum_{j=0}^{J-g-1}
min\{w_{P,j},w_{P,j+g}\}.
$$

Then

$$
\boxed{
Omega_g >= (2S-beta|A|(J+g))_+.
}
$$

One of two global parity classes is radially disjoint and carries at least `Omega_g/2` paid pair weight.

Consequently, for every `epsilon>0`, if

$$
S >= (1/2+epsilon)beta|A|(J+g),
$$

then one parity class carries at least

$$
epsilon beta|A|(J+g)
$$

of paid genuine scale pairs `h,h+q`.

Apply BDA4e to that parity class with row/column load threshold `Lambda`.

1. If all loads are at most `Lambda`, a row-column-compatible subfamily carries at least
   $$
   \boxed{
   \frac{epsilon beta|A|(J+g)}{10(Lambda-1)+1}
   }
   $$
   paid pair weight.
2. If a load exceeds `Lambda`, one of the five BDA4e affine anchor laws is returned, together with at least one fifth of the paid incidence at the selected heavy coordinate.

### Proof

The heavy-atom alternative is the negation of the cap. Under the cap, AC3ao supplies exactly the weighted interlaced paths of BDA5z, giving the overlap and parity statements. The density display substitutes into that bound. BDA4e then gives the bounded-load compatible-family conclusion or the heavy-coordinate affine role. QED.

## AC3aq -- faithful AC-to-BDA delegation -- PROVED UNDER HYPOTHESES

Let an AC3am role-pure family have total paid weight `W` and an arithmetically, paid-, and support-faithful BDA realization with parameters `Q,M`.

After losing at most the explicit factor `L_{Q,M}`, one exact arithmetic profile of weight `S>=W/L_{Q,M}` satisfies one of the following.

1. **Heavy exact atom:** one anchor and scale carries weight greater than `beta`.
2. **Dispersed-anchor inequality:**
   $$
   S < (1/2+epsilon)beta|A|(J+g).
   $$
3. **Executable BDA family:** a row-column-compatible family of genuine `h,h+q` radial pairs carries at least
   $$
   \frac{epsilon beta|A|(J+g)}{10(Lambda-1)+1}
   $$
   paid weight and enters BDA5a--BDA5g.
4. **Affine anchor chain:** one of the five BDA4e heavy-load laws is returned with its current paid incidence.

No other bounded-denominator output remains hidden inside the role label.

### Proof

AC3an chooses the exact profile. AC3ao gives its scalar slots. AC3ap gives the four outputs. Paid faithfulness transfers the selected weight, while support faithfulness makes outcome 3 an actual BDA decoder input rather than only an arithmetic pair. QED.

## Exact remaining AC geometry

The arithmetic and weighted parts of the delegation are complete. For each AC3am denominator role, the remaining geometric proof obligation is now the following finite checklist.

1. Produce the fields `(q,d,e,xi,P,h)` and prove `h det(d,e) congruent xi mod q`.
2. Prove a uniform direction norm bound `M`, or return explicit direction spread before AC3an.
3. Prove that the selected current incidence is paid-faithful.
4. Prove that same-anchor scales `h,h+q` realize the BDA radial-pair support and that the BDA4e conflict graph dominates actual AC incompatibility.

Once these four items hold, AC3aq is a total transition to a heavy local atom, an explicit low-occupancy inequality, a proved decoder family, or an affine anchor chain. The unresolved work is therefore role realization and the two explicit BDA terminal alternatives, not another abstract weighted extraction lemma.

## Finite check

`scripts/verify_ac_bda_delegation.py` exhausts small normalized direction sets, denominators, scalar residues, scale solutions, weighted slot systems, and profile-weight assignments. It checks the finite profile count, canonical `q/g` slotization, exact aggregation, the weighted `g`-step overlap bound, parity disjointness, and the profile pigeonhole loss.