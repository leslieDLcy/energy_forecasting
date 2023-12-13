import matplotlib.pyplot as plt
from darts.metrics import mape
from energy_forecasting.params import Params


def eval_model(model, n, actual_series, val_series, metric='None'):
    
    pred_series = model.predict(n=n, num_samples=200)

    # plot actual series
    plt.figure(figsize=(10,3))
    actual_series[: pred_series.end_time()].plot(label="actual")

    # plot prediction with quantile ranges
    pred_series.plot(
        low_quantile=Params.lowest_q, high_quantile=Params.highest_q, label=Params.label_q_outer
    )
    pred_series.plot(low_quantile=Params.low_q, high_quantile=Params.high_q, label=Params.label_q_inner)
    plt.legend()
    if metric == "mape":
        metric_mape = mape(val_series, pred_series)
        plt.title("MAPE: {:.2f}%".format(metric_mape))
        return metric_mape
    else:
        pass    