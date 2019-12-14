import arviz as az
import numpy as np
import typing as tp


def convert_pyjags_samples_dict_to_arviz_inference_data(
        samples: tp.Dict[str, np.ndarray]) -> az.InferenceData:
    # pyjags returns a dictionary of numpy arrays with shape
    #         (parameter dimension, chain length, number of chains)
    # but arviz expects samples with shape
    #         (number of chains, chain length, parameter dimension)
    reordered_samples \
        = {name: np.swapaxes(sample, 0, 2)
           for name, sample
           in samples.items()}

    return az.InferenceData(
        posterior=az.data.base.dict_to_dataset(reordered_samples))
