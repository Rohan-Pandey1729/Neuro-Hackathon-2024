import time
import matplotlib.pyplot as plt
import numpy as np
from dotenv import load_dotenv
import pickle
import os

from brainflow.board_shim import (
    BoardShim,
    BrainFlowInputParams,
    BoardIds,
    BrainFlowPresets,
)
from brainflow import ml_model
from brainflow.ml_model import *


def get_prob(
    model_path=os.path.join("..", "finalized_model_l1_C=1e-7.sav"), sample_time=11.0
):
    """
    `model_path` is relative path of model file from `main.py` (hackathon fr)

    `sample_time` is how long to sleep for while collecting data
    """
    time.sleep(5)
    return np.random.random()
    # load_dotenv()

    # BoardShim.enable_dev_board_logger()

    # board_id = 0
    # serial_port = os.getenv("SERIAL_PORT")

    # params = BrainFlowInputParams()
    # params.serial_port = serial_port
    # board = BoardShim(board_id, params)
    # board.prepare_session()
    # sampling_rate = board.get_sampling_rate(board_id)  # per second, presumably

    # board.start_stream()
    # sample_time = 11
    # time.sleep(sample_time)
    # # data = board.get_current_board_data (256) # get latest 256 packages or less, doesnt remove them from internal buffer
    # data = board.get_board_data()  # get all data and remove it from internal buffer
    # board.stop_stream()
    # board.release_session()

    # d2 = data[1:8, :2406]
    # dfft = np.fft.fft(d2).view(np.float64).reshape(7, 2406, 2)
    # model = pickle.load(open(model_path, "rb"))
    # probs = model.predict_proba(dfft.reshape(1, -1))
    # return probs[0][1]
