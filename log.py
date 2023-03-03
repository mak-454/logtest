import urllib3
from mlflow import log_metric
import logging
import os

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    for i in range(10):
        logging.warning('Logger Test')
        print("Print Test")
        
        log_metric ("train_loss", i*i, step=i)
