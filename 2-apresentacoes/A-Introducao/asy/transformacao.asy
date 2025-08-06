//-----------------------------------------------------------------------------

import "./utils.ah" as utils;

size(6cm, 6cm, IgnoreAspect);

xaxis(YZero, -1, 3, L="$x$", arrow=Arrows(5));
yaxis(XZero, -1, 3, L="$y$", arrow=Arrows(5));

pair O = (0,0);
pair P = (1.9,2.2);
pair X = (P.x, 0);

//-----------------------------------------------------------------------------

pen polar = magenta+linewidth(1);
pen cart  = blue   +linewidth(1);

draw(O--X--P, cart);

draw(arc(O, 1, 0, 49), polar);
draw(O--P, polar);
dot(O);
dot(P);

label("$\theta$", (1.05, 0.5));
label("$P$", P, N);
label("$r$", P/2, NW);

label("$x$", (P.x/2,   0), S);
label("$y$", (P.x, P.y/2), E);

//-----------------------------------------------------------------------------
