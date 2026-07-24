# Component-clean row-lift banks

The full row-lift support contains too many candidate-only triples, but those
triples split naturally into three classes:

1. triples wholly inside the movement rectangle;
2. triples wholly inside the refill rectangle;
3. triples meeting both rectangles.

This chapter removes the first two classes at the bank-design stage and gives an
exact endpoint for the remaining cross-component geometry.

## 1. Independent clean component banks

Let `X` be the retained old configuration. Let `Omega_M` be a probability
distribution on movement states and `Omega_F` a probability distribution on
refill states. Assume every movement state:

- restores every deleted old-column deficit;
- gives exactly two points to every new row;
- has distinct cells;
- is internally no-three-in-line.

Assume every refill state analogously restores the deleted old rows, gives two
points to every new column, has distinct cells, and is internally no-three.
The movement and refill rectangles are disjoint. Sample `M` and `F`
independently.

Define:

- `B_M,B_F`: component cells on secants through two points of `X`;
- `P_MM,P_FF`: same-component cell pairs whose line contains a point of `X`;
- `P_MF`: movement-refill cell pairs whose line contains a point of `X`;
- `T_MMF`: collinear triples with two movement cells and one refill cell;
- `T_MFF`: collinear triples with one movement cell and two refill cells.

For a component state distribution write `p_M(Q)=Pr(Q subseteq M)` and
`p_F(Q)=Pr(Q subseteq F)`.

### Theorem PP3z -- PROVED

If

\[
\begin{aligned}
&\sum_{z\in B_M}p_M(z)
+\sum_{z\in B_F}p_F(z)\\
&+\sum_{P\in P_{MM}}p_M(P)
+\sum_{P\in P_{FF}}p_F(P)
+\sum_{\{z,w\}\in P_{MF}}p_M(z)p_F(w)\\
&+\sum_{\{z_1,z_2,w\}\in T_{MMF}}p_M(z_1,z_2)p_F(w)\\
&+\sum_{\{z,w_1,w_2\}\in T_{MFF}}p_M(z)p_F(w_1,w_2)
<1,
\end{aligned}
\]

then some pair `(M,F)` gives an executable no-three-in-line row-lift patch.

#### Proof

Let `Z` count selected certificates of the seven displayed types. Independence
factorizes every mixed-component probability, so the displayed expression is
exactly `E Z`.

Because `Z` is a nonnegative integer, expectation below one gives a state pair
with `Z=0`. Such a pair has no triple with two retained points, no triple with
one retained point, and no cross-component inserted triple. The two component
banks exclude triples lying wholly inside one component. Their degree conditions
and disjoint supports give an executable patch. ∎

## 2. Spread form

Suppose

\[
p_M(z)\le\frac{\alpha_M}{t},
\qquad
p_M(z,z')\le\frac{\beta_M}{(t)_2},
\]

and analogously with constants `alpha_F,beta_F` for the refill bank.

### Corollary PP3aa -- PROVED

It is sufficient that

\[
\begin{aligned}
&\frac{\alpha_M|B_M|+\alpha_F|B_F|}{t}\\
&+\frac{\beta_M|P_{MM}|+\beta_F|P_{FF}|}{(t)_2}
+\frac{\alpha_M\alpha_F|P_{MF}|}{t^2}\\
&+\frac{\beta_M\alpha_F|T_{MMF}|
+\alpha_M\beta_F|T_{MFF}|}{t^2(t-1)}
<1.
\end{aligned}
\]

#### Proof

Apply the cell and pair spread bounds term by term in PP3z. Mixed probabilities
factor by independence. ∎

This endpoint does not pay for any triple wholly inside one component. It is
therefore compatible with algebraic component banks, such as families built
from internally clean permutation pairs.

## 3. Deterministic cross-triple cap

### Proposition PP3ab -- PROVED

Let `M` and `F` be two internally no-three sets, each of size `2t`, in disjoint
rectangles. Then their union contains at most

\[
\boxed{
4\binom{2t}{2}=4t(2t-1)
}
\]

cross-component collinear triples.

#### Proof

Every pair of points in `M` determines one line. Since `F` is no-three, that
line contains at most two points of `F`. Hence triples with two movement points
and one refill point number at most

\[
2\binom{2t}{2}.
\]

Interchanging `M` and `F` gives the same bound for triples with one movement
point and two refill points. Add the two estimates. ∎

The bound is quadratic rather than the `Omega(t^4 log t)` triple population of
the full support. It does not itself force a zero-triple pair, but it confirms
that component cleaning removes the multiscale candidate-only accumulation
inside each rectangle.

## 4. Revised construction target

A component-clean PP3 theorem may proceed in two stages:

1. construct spread banks of internally no-three saturated states separately in
   the movement and refill rectangles;
2. use PP3z or PP3aa to choose a pair with no retained-core or cross-component
   certificate.

This route trades the four-layer activated-load problem for two internally clean
component banks plus one cross-incidence estimate.