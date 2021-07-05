# Objective
# 1.Read the parameters file
# 2.Process
# 3.Return the data as dataframe

import yaml
import pandas as pd
import argparse
import os

# This function is used to return the list of parameters as a dictionary


def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

# Pass the config path


def get_data(config_path):
    # read the config file from config path
    config = read_params(config_path)
    # We now fetch the data path from the parameters file
    data_path = config["data_source"]["s3_source"]
    # from the data path we fetch the csv file details into a pandas dataframe
    df = pd.read_csv(data_path, sep=",", encoding="utf-8")
    # print(df.head())
    # return the data frame object
    return df

# This will be the entry point for the project and we pass arguments through command line


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    # If config is not available we will use config file
    args.add_argument("--config", default="params.yaml")
    # Parse the arguments that is fetch the arguments
    parsed_args = args.parse_args()
    data = get_data(config_path=parsed_args.config)