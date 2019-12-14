# pyjags_arviz
Makes MCMC samples from PyJAGS usable in ArviZ

## Table of Contents

1.  [Installation](#installation)
2.  [Getting Started](#getting-started)

## Installation

1.  Install via PIP: 
    <pre>
    pip install pyjags_arviz 
    </pre>
    or 
    <pre>
    pip3 install pyjags_arviz 
    </pre>
    if not using Anaconda.
    
    To get the latest version, clone the repository from github, 
    open a terminal/command prompt, navigate to the root folder and install via
    <pre>
    pip install .
    </pre>
    or 
    <pre>
    pip3 install . 
    </pre>
    if not using Anaconda.

## Usage
Import the function convert_pyjags_samples_dict_to_arviz_inference_data via
<pre>
from pyjags_arviz import convert_pyjags_samples_dict_to_arviz_inference_data
</pre>

Having sampled the from the posterior distribution using PyJAGS via
<pre>
samples \
    = jags_model.sample(...)
</pre>
one can write 
<pre>
idata = convert_pyjags_samples_dict_to_arviz_inference_data(samples)
</pre>
to convert the dictionary returned from PyJAGS to an ArviZ InferenceData object.

This object can be used in ArviZ to generate trace plots and compute diagnostics.  
Trace plot:
<pre>
az.plot_trace(idata)
</pre>

Effective sample size:
<pre>
az.ess(idata)
</pre>

Gelman and Rubin statistic:
<pre>
az.rhat(idata)
</pre>
