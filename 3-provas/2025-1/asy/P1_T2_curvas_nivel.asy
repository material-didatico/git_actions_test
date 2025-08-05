
import "./utils.ah" as utils;

drawAxis();

pair center = (1,1);

real[] c_values = {0, sqrt(12), sqrt(15)};

for (int i = 0; i < pens.length; ++i)
{
  real c      = c_values[i];
  real radius = sqrt(16 - c^2);

  draw(shift(center)*Circle((0,0), radius), pens[i]);
}

dot(center, black+3pt);
label("$(1,1)$", center, S);

label("$c=0$",         (3,5),     E );
label("$c=\sqrt{12}$", (2,3.1),   E );
label("$c=\sqrt{15}$", (1.8,0.7), E );

