# Dark-Channel-Prior

This is an unofficial implementation of paper: [Single Image Haze Removal Using Dark Channel Prior](http://kaiminghe.com/publications/cvpr09.pdf)[He+, CVPR2009] and guided filter algorithm from paper: [Guided Image Filtering](http://kaiminghe.com/publications/eccv10guidedfilter.pdf)[He+, ECCV2010].

Both the original algorithms and an interface written by PyQt5 are provided.

# Requirements:star2:

Python 3.7.7+

numpy 1.20.3+

PyQt5 5.15.0+

```shell
pip install -r requirements.txt
```

# Work:sailboat:

This implementation contains:

- [x] 1.Implement minimum filtering using opencv-api, and simply using for loop.

- [x] 2.Get the dark channel of the given image.

- [x] 3.Calculate the global atmospheric light, a.k.a `A`.

- [x] 4.Calculate the light transmission coefficient, a.k.a `t`.

- [x] 5.Implement the guided filter algorithm.

- [x] 6.Use guided filter to optimize dark channel image.

# Theory:foggy:

The relationship between the hazed map`I(x)`and original image`J(x)`:
$$
I(x)=J(x)t(x)+A(1-t(x)) \tag{1} \label{eq1}
$$
Formulation to calculate the dark channel：
$$
J^{dark}(x)=\underset {c\in \{r,g,b\}}{min}(\underset {y\in \Omega(x)}{min}{J^c(y)}) \tag{2} \label{eq2}
$$
Minimize both sides of `eq.(1)`:
$$
\underset {y\in \Omega(x)}{min}I^c(x)=\widetilde{t}(x) \underset {y\in \Omega(x)}{min}J^c(x)+(1-\widetilde{t}(x))A^c \tag{3}
$$
Divide both sides by A:
$$
\underset {y\in \Omega(x)}{min}(\frac {I^c(x)}{A^c})=\widetilde{t}(x) \underset {y\in \Omega(x)}{min}(\frac {J^c(x)}{A^c})+(1-\widetilde{t}(x)) \tag{4} \label{eq4}
$$
Add another minimization operation:
$$
\underset {c}{min} \underset {y\in \Omega(x)}{min}(\frac {I^c(x)}{A^c})=\widetilde{t}(x) \underset {c}{min} \underset {y\in \Omega(x)}{min}(\frac {J^c(x)}{A^c})+(1-\widetilde{t}(x)) \tag{5}
$$

According to statistics,  the dark channel `J` is close to 0 , then:
$$
J^{dark}(x)=\underset {c}{min}(\underset {y \in \Omega(x)}{min}(J^c(y)))=0 \tag{6}
$$
It leads to:
$$
\underset {c}{min} \underset {y\in \Omega(x)}{min}(\frac {J^c(x)}{A^c})=0 \tag{7}
$$
Substituting `eq.(7)` into `eq.(5)`, `t` can be calculated approximately:
$$
\widetilde{t}(x)=1-\underset {c}{min}(\underset {y \in \Omega(x)}{min}(J^c(y)) \tag{8}
$$

In consideration of the existence of part of haze, a parameter `w` is set to keep the haze:
$$
\widetilde{t}(x)=1-\omega\underset {c}{min}(\underset {y \in \Omega(x)}{min}(J^c(y)) \tag{9}
$$
Finally, the formulation of calculate the original image is figured out:
$$
J(x)=\frac {I(x)-A}{max(t(x),t_0)}+A \tag{10}
$$
`A` is the global atmospheric light composition, we take the position of the brightest %0.1 point in the dark channel image, then find the maximum value of the RGB value of the point at the corresponding position on the original image, and take the average of this value of all points.

# Results:framed_picture:

![demo](./demo/demo.gif)

