import arviz as az
import numpy as np
import typing as tp


def convert_pyjags_samples_dict_to_arviz_inference_data(
        samples: tp.Dict[str, np.ndarray]) -> az.InferenceData:
    # pyjags returns a dictionary of numpy arrays with shape
    #         (parameter dimension, chain length, number of chains)
    # but arviz expects samples with shape
    #         (number of chains, chain length, parameter dimension)

    parameter_name_to_samples_map = {}

    for parameter_name, chains in samples.items():
        parameter_dimension, chain_length, number_of_chains = chains.shape
        if parameter_dimension == 1:
            parameter_name_to_samples_map[parameter_name] = \
                chains[0, :, :].transpose()
        else:
            for i in range(parameter_dimension):
                parameter_name_to_samples_map[f'{parameter_name}_{i+1}'] = \
                    chains[i, :, :].transpose()

    return az.InferenceData(
        posterior=az.data.base.dict_to_dataset(parameter_name_to_samples_map))