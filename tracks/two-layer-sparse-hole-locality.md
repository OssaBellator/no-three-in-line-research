# Two-layer locality with arbitrary sparse host holes

SRR2b controls one matching when the host has an arbitrary sublinear
number of missing cells.  The complete two-layer cylinder bounds from
SRR3e allow the same conditioning argument for two edge-disjoint
matchings, even though a missing cell can interact with prescribed
edges in the opposite layer.

Let \(\mu_0\) be uniform on the ordered pairs of edge-disjoint perfect
matchings of \(K_{N,N}\), so

\[
|\Omega_2(K_{N,N})|=N!\,!N.
\]

Write

\[
D(n,q)=\sum_{j=0}^q(-1)^j\binom qj(n-j)!.
\]

Recall the SRR3e lower and upper bounds for a globally compatible
cylinder of layer ranks \((a,b)\):

\[
L_N(a,b)
=
\frac{D(N-a,b)\,!(N-b)}{N!\,!N},
\]

\[
U_N(a,b)
=
\frac{(N-a)!\,D(N-b,N-2b)}{N!\,!N}.
\]

For any feasible labelled cylinder, without global cross-layer
compatibility, the crude count

\[
\boxed{
V_N(a,b)
=
\frac{(N-a)!(N-b)!}{N!\,!N}
}
\]

is an upper bound: choose extensions in the two layers independently
and ignore their possible collisions.

## SRR3g -- two-layer sparse-hole locality

Let \(Q\) be any set of \(t\) missing cells and let
\(\mu_Q\) be uniform on \(\Omega_2(K_{N,N}\setminus Q)\).  For a
globally compatible host-valid cylinder \(E\) of ranks \((a,b)\), define

\[
\boxed{
\varepsilon_Q(a,b)
=
t\,
\frac{V_N(a+1,b)+V_N(a,b+1)}{L_N(a,b)}.
}
\]

### Theorem SRR3g -- PROVED

Under the complete two-layer measure,

\[
\boxed{
\Pr_{\mu_0}(
\text{some edge of \(Q\) occurs in either layer}
\mid E)
\leq
\varepsilon_Q(a,b).
}
\]

Consequently, let \(F\) and \(B\) be globally compatible host-valid
cylinders with layer ranks \((k_1,k_2)\) and \((s_1,s_2)\), with all
their row and column vertices disjoint.  If

\[
\varepsilon_Q(k_1,k_2)<1,
\qquad
\varepsilon_Q(s_1,s_2)<1,
\]

and the SRR3e bounds are defined at the combined ranks, then

\[
\boxed{
\frac{\mu_Q(B\mid F)}{\mu_Q(B)}
\leq
\frac{
U_N(k_1+s_1,k_2+s_2)
}{
L_N(k_1,k_2)L_N(s_1,s_2)
}
\frac1{
(1-\varepsilon_Q(k_1,k_2))
(1-\varepsilon_Q(s_1,s_2))
}.
}
\]

For fixed cylinder ranks and \(t=o(N)\), the right side is \(1+o(1)\).

### Proof

Fix a missing cell \(q\).  Conditional on \(E\), the event that \(q\)
occurs in layer one is either impossible or extends \(E\) to a feasible
cylinder of ranks \((a+1,b)\).  Its unconditional probability is at
most \(V_N(a+1,b)\), while
\(\Pr_{\mu_0}(E)\geq L_N(a,b)\).  Thus its conditional probability is at
most \(V_N(a+1,b)/L_N(a,b)\).  The same argument in layer two gives the
other term.  A union bound over both labelled copies of all \(t\)
missing cells proves the first box.

Let \(A_Q\) be the event that neither layer uses \(Q\), and set

\[
\alpha_Q(E)=\Pr_{\mu_0}(A_Q\mid E).
\]

The first box gives

\[
\alpha_Q(E)\geq1-\varepsilon_Q(a,b).
\]

Because \(\mu_Q=\mu_0(\,\cdot\mid A_Q)\),

\[
\frac{\mu_Q(B\mid F)}{\mu_Q(B)}
=
\frac{\mu_0(F\cap B)}
{\mu_0(F)\mu_0(B)}
\frac{
\alpha_Q(F\cap B)\alpha_Q(\varnothing)
}{
\alpha_Q(F)\alpha_Q(B)
}.
\]

The first factor is at most the SRR3e \(U/L/L\) ratio.  Bound both
numerator correction factors by one and use the two lower bounds in the
denominator.  This proves the displayed estimate.

Finally, \(L_N(a,b)\) and \(V_N(a,b)\) are
\((1+O_{a,b}(N^{-1}))/((N)_a(N)_b)\) up to an absolute derangement
factor, so \(\varepsilon_Q(a,b)=O_{a,b}(t/N)=o(1)\).  SRR3e supplies
the other \(1+O(N^{-1})\) factor. \(\square\)

## SRR3h -- explicit linear-hole locality window

The exact error in SRR3g has a rank-uniform elementary upper bound.

### Theorem SRR3h -- PROVED

Assume

\[
N\geq\max\{2,2b,b+2,a+b+1\}.
\]

Then

\[
\boxed{
\frac{V_N(a+1,b)}{L_N(a,b)}
\leq
\frac3{N-a-b},
}
\]

\[
\boxed{
\frac{V_N(a,b+1)}{L_N(a,b)}
\leq
\frac6{N-a-b},
}
\]

and therefore every missing set \(Q\) of size \(t\) satisfies

\[
\boxed{
\varepsilon_Q(a,b)
\leq
\frac{9t}{N-a-b}.
}
\]

In particular, SRR3g applies whenever \(9t<N-a-b\).  For remote
cylinders \(F,B\) of ranks \((k_1,k_2)\) and \((s_1,s_2)\), under the
compatibility assumptions of SRR3g, the displayed rank conditions, and

\[
9t<N-k_1-k_2,
\qquad
9t<N-s_1-s_2,
\]

the following holds:

\[
\boxed{
\frac{\mu_Q(B\mid F)}{\mu_Q(B)}
\leq
\frac{
U_N(k_1+s_1,k_2+s_2)
}{
L_N(k_1,k_2)L_N(s_1,s_2)
}
\frac1{
\left(1-\frac{9t}{N-k_1-k_2}\right)
\left(1-\frac{9t}{N-s_1-s_2}\right)
}.
}
\]

Thus, for fixed ranks and \(t/N\leq c<1/9\), the remote-correlation
inflation is uniformly \(O_c(1)\), with

\[
\limsup_{N\to\infty}
\frac{\mu_Q(B\mid F)}{\mu_Q(B)}
\leq
\frac1{(1-9c)^2}.
\]

### Proof

The union bound for \(b\) forbidden positions in a permutation of
\(N-a\) points gives

\[
D(N-a,b)
\geq
(N-a)!-b(N-a-1)!
=
(N-a-b)(N-a-1)!.
\]

Also \(!m\geq m!/3\) for \(m\geq2\), directly from the alternating
series
\(!m/m!=\sum_{j=0}^m(-1)^j/j!\).  Substitution in the first ratio gives

\[
\frac{(N-a-1)!(N-b)!}
{D(N-a,b)\,!(N-b)}
\leq
\frac3{N-a-b}.
\]

For the other layer,

\[
\frac{(N-a)!(N-b-1)!}
{D(N-a,b)\,!(N-b)}
\leq
\frac{3(N-a)}
{(N-a-b)(N-b)}.
\]

If \(a\geq b\), the last extra ratio is at most one.  If \(a<b\), the
hypothesis \(N\geq2b\) gives
\((N-a)/(N-b)\leq N/(N-b)\leq2\).  This proves the first three boxes.
Insert those bounds for the two SRR3g errors to obtain the correlation
estimate.  For fixed ranks the complete-host \(U/L/L\) factor tends to
one, proving the limit. \(\square\)

SRR3h extends arbitrary-hole control from \(o(N)\) holes with
\(1+o(1)\) locality to a small linear number of holes with explicit
constant locality.  It does not make that constant tend to one when
\(t/N\) stays positive, and it still does not reach the
\(\Theta(N^2)\)-hole superregular regime.

## Resampling consequence

The empty-cylinder bound \(\varepsilon_Q(0,0)<1\) guarantees that the
two-layer host space is nonempty.  Every host vertex has degree at least
\(N-t\), so SRR3f gives at least

\[
N-2t-3
\]

stationary four-cycle choices whenever this is positive.  Its pathwise
noncreation property combined with SRR3g proves the full fixed-rank
two-layer remote locality for every arbitrary missing set of size
\(o(N)\).

SRR3h additionally gives bounded remote inflation and
\(\Omega(N)\) stationary choices for \(|Q|\leq cN\), \(c<1/9\).
The unresolved superregular regime may therefore be assumed to lie
beyond this explicit linear-hole window when bounded locality is enough.
Near-independence at positive linear density and the
\(\Theta(N^2)\) missing cells allowed by dense superregularity remain
open.

`scripts/verify_two_layer_sparse_hole_locality.py` exhaustively checks
the complete cylinder bounds, conditional avoidance estimate, and host
remote ratio on \(K_{4,4}\) with arbitrary small hole sets.  It also
checks both elementary ratio bounds and the \(9t/(N-a-b)\) error ceiling
through a range of ranks and ambient sizes.
