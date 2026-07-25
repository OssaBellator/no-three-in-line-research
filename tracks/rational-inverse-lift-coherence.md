# Physical lift coherence for rational quotient edges

RI2k--RI4b classify cosets of the normalized secant parameter

\[
c=\frac zx
\]

and its image \(g=F_r(c)\).  The I6 absorber bank, by contrast, acts
on physical columns of one installed hyperbola layer.  Passing from
the first object to the second requires an additional lift theorem:
the normalization base \(x\) is occurrence-dependent.

This note isolates that missing datum, gives a counterexample to
automatic physical installation, and supplies an exact gate into the
conditional RI5a--RI5c bank.

## RI5d -- arbitrary base-scale freedom

Let \(p\) be prime, let \(a,b\in\mathbb F_p^\times\) with

\[
r=\frac ba\notin\{0,1\},
\]

and put

\[
F_r(c)=\frac{c(1-c)}{r-c}.
\]

For \(c\notin\{0,1,r\}\) with \(F_r(c)\ne1\), choose an arbitrary
base scale \(s(c)\in\mathbb F_p^\times\) and define

\[
x_c=s(c),
\qquad
u_c=F_r(c)s(c),
\qquad
z_c=cs(c).
\]

Use the modular hyperbola points

\[
P_x=(x,a/x),
\qquad
B_z=(z,b/z).
\]

### Theorem RI5d -- PROVED

For every choice of the function \(s\), the triple

\[
\boxed{
\{P_{x_c},P_{u_c},B_{z_c}\}
}
\]

is modularly collinear and has normalized OP4g record
\((r,c,F_r(c))\).

Consequently, normalized density in a source \(H\)-coset and its
\(F_r\)-image places no restriction on the base scales \(s(c)\).
Indeed, for any fixed \(z_0\ne0\), choosing

\[
\boxed{s(c)=z_0c^{-1}}
\]

makes every anchor column \(z_c\) equal to \(z_0\).  An arbitrarily
large normalized root family can therefore lift to one physical
anchor star rather than to a physical coset block.

### Proof

The modular secant condition for the displayed two-channel triple is

\[
r x_cu_c=z_c(x_c+u_c-z_c).
\]

After substituting \(u_c=F_r(c)x_c\) and \(z_c=cx_c\) and dividing by
\(x_c^2\), this becomes

\[
rF_r(c)=c(1+F_r(c)-c),
\]

which is exactly the defining equation for \(F_r(c)\).  The normalized
ratios are \(z_c/x_c=c\) and \(u_c/x_c=F_r(c)\).

The function \(s\) never entered the reduced equation.  Substitution
of \(s(c)=z_0c^{-1}\) gives \(z_c=z_0\), proving the final assertion.
\(\square\)

RI5d is a statement about the quotient information alone.  A real
factor has the additional equality of its integer cross carries.
That equality can and must be used by a positive lift theorem, but
RI4b and the normalized density conclusion of OP4i do not currently
bound the base scale with it.  Real factors also exhibit multiple
scales: the verifier below records a \(p=11\) fixed quotient edge with
three complete \(F_5\)-fibres and two different base-scale cosets.

## RI5e -- exact scale-coset and load gate

Fix \(H\leq\mathbb F_p^\times\).  For one actual OP4g occurrence write

\[
A=cH,
\qquad
C=F_r(c)H,
\qquad
S=xH.
\]

Call \(S\) its **base-scale coset**.  Its three physical column cosets
are exactly

\[
\boxed{
xH=S,
\qquad
uH=CS,
\qquad
zH=AS.
}
\]

For a nonfixed rational fibre
\(\{c,\tau_r(c)\}\), let
\(\mathcal S_c\) and \(\mathcal S_{\tau(c)}\) be the scale-coset sets
represented by the actual witnesses of its two roots.  The fibre has a
**coherent scale lift** when

\[
\mathcal S_c\cap\mathcal S_{\tau(c)}\ne\varnothing.
\]

A fixed fibre uses its one represented scale set.

### Theorem RI5e -- PROVED

There is an exact audit with the following outputs.

1. If a complete normalized fibre has no coherent scale lift, return
   that fibre and the two disjoint scale-coset sets.  This is a
   physical-lift mismatch, not an absorber.
2. Otherwise choose one common scale coset for every complete fibre.
   If \(N\) fibres choose \(K\) distinct scale cosets, one scale class
   contains at least
   \[
   \boxed{\left\lceil\frac NK\right\rceil}
   \]
   complete fibres.  If the fibres carry nonnegative weights of total
   \(W\), one scale class carries weight at least
   \[
   \boxed{\frac WK.}
   \]
3. In a fixed scale class \(S\), choose one actual witness of each
   root at scale \(S\).  If there are \(R\) chosen root witnesses and
   no physical anchor column \(z\) occurs more than \(\mu_z\) times,
   then they occupy at least
   \[
   \boxed{\left\lceil\frac R{\mu_z}\right\rceil}
   \]
   distinct anchor cells in the fixed physical cosets \(AS\) and
   \(BS\).  With total witness payment \(P\) and physical-column load
   at most \(\beta_z\), the weighted form gives at least
   \(P/\beta_z\) distinct anchor cells.  Otherwise the heavy \(z\) is
   an explicit current anchor star.
4. The analogous statement for partner columns has lower bound
   \[
   \boxed{\left\lceil\frac R{\mu_u}\right\rceil}
   \]
   in the fixed physical image coset \(CS\), or returns a heavy
   partner-point star.

### Proof

The three physical quotient identities follow from
\(u=F_r(c)x\) and \(z=cx\).  The first output is the definition of
coherent lift.  Once every fibre has a chosen scale, pigeonholing \(N\)
objects over \(K\) classes proves conclusion 2.  Within one class,
every selected root label belongs to \(A\) or \(B\), so its anchor lies
in \(AS\) or \(BS\); every partner lies in \(CS\).  Dividing the \(R\)
occurrences by the respective maximum physical-column loads proves the
two ceiling bounds.  The identical pigeonhole and load calculations
with weights prove the weighted assertions. \(\square\)

The high-load outputs feed the existing point-star/carry routers.
The low-load outputs give genuine physical density, but still do not
silently complete a partial matching to the full I6 bank.

## Exact entrance condition for RI5a--RI5c

Call a scale-localized family **bank-ready** only when all of the
following are certified.

1. Its physical column block is a full union
   \[
   X=\bigcup_{\alpha=1}^m u_\alpha H.
   \]
2. On one current permutation layer, the cells on that block are
   exactly
   \[
   \{(x,a/x):x\in X\},
   \]
   and hence use precisely the row block \(aX^{-1}\).
3. Every paid object to be neutralized is supported on those current
   cells.
4. Every collateral event is either evaluated with its actual block
   correlation or satisfies the distinct-source/distinct-target
   cylinder hypothesis used by I6.

Under these hypotheses, RI5a--RI5c apply verbatim.  If condition 1 or
2 fails, the missing columns, missing rows, and their current occupants
form an explicit **completion debt**.  Density above one half in a
normalized coset does not pay that debt.

Thus the corrected fixed-edge interface is

\[
\boxed{
\begin{array}{c}
\text{normalized fixed edge}\\
\Downarrow\\
\text{scale mismatch, scale growth, physical star,}\\
\text{or a scale-localized physical family}\\
\Downarrow\\
\text{bank-ready audit}\\
\Downarrow\\
\text{conditional I6 collateral comparison.}
\end{array}
}
\]

The remaining positive RI5 theorem must pay the completion debt using
current syndrome incidence, or route it through the alternating
rectangle/blocker machinery.  It may not identify normalized roots
with physical columns without this audit.

`scripts/verify_rational_lift_coherence.py` checks the arbitrary-scale
secant identity over small primes, the exact physical quotient laws,
the anchor-collapse construction, coherent-scale pigeonholing, and an
explicit really collinear \(p=11\) fixed-edge family with multiple
base-scale cosets.
