
import "./utils.ah" as utils;

drawAxis();

draw(Circle((1,1), 4), blue);
fill(circle((1,1), 4), lightblue+opacity(0.3));

dot((1,1),blue);
label("$(x-1)^2 + (y-1)^2 \leq 16$", (5, 3), blue);
