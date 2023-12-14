energy_forecasting
==============================

Experiments on community dataset regarding energy demand/generation forecasting with uncertainty-aware deep learning models. Data are sourced from [Global Energy Forecasting Competition 2012 - Load Forecasting](https://www.kaggle.com/competitions/global-energy-forecasting-competition-2012-load-forecasting/overview) and [Global Energy Forecasting Competition 2012 - wind power Forecasting](https://www.kaggle.com/competitions/GEF2012-wind-forecasting/data).
Correspoing Jupyter notebooks can be found in the directory `notebooks`.


## *highlights*

- [x] uncertainty-aware DL modelling;
- [x] seq2seq


## LSTM Autoencoder

An intuitive web application[^1] is created for facilitating the use of `Virtual Raphael`. 

<!-- [![](visualisations/UI.png)](visualisations/UI.png) -->


## Temporal fusion transformer model

The application can be easily run from terminal, after [installing the package locally](#installation). Put your PDF file into the directory `inference_reports/New Report` and call the CLI command as below. Currently, running a cycle of all the models takes about 110s. The results and visualisations will be saved into the `Predictions` directory. 

<!-- ![alt text](visualisations/prediction.png "Prediction") -->



## installation

Some library codes for preprocessing and building models can be installed locally for convenience. For installing[^2]

```shell
pip install .
```


### reference

--------
[^1]: Created by [Yu Chen](https://yuchenakaleslie.github.io/);
[^2]: Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. 