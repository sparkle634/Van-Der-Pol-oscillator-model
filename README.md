# Van-Der-Pol-oscillator-model
The acoustic pressure fluctuations of combustion noise is modelled as a classical Van Der Pol oscillator equation with an external forcing. Heat release rate fluctuations are modelled as white Gaussian noise $(\xi)$ of intensity $\Gamma$.
<br>
$\frac{d^2\eta}{dt^2} + (\beta - \kappa\eta^2)\frac{d\eta}{dt} + \omega^2\eta = \xi$
<br>
Here, $\beta$ represents the linear damping in the system and $\kappa$ represents the non-linear damping in the system.
<br>
This equation is rewritten as system of equations which can be expressed as:
<br>
$\frac{d\eta}{dt} = \dot \eta$
<br>
$\frac{d\dot \eta}{dt} = (\kappa\eta^2 -\beta)\dot \eta - \omega^2\eta + \xi$
<br>
This is solved using both Runge-Kutta Method and Adam-Bashforth_moulton predictor corrector algorithm.
