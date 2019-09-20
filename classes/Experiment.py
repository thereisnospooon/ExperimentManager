import sys
import os


class Experiment:
    def __init__(self, name, full_path, model, dataset_path, data_iterator):
        self.name = name
        # Todo: assert name of experiment is unique
        self.full_path = full_path
        pass

    def run_train(self):
        pass

    def run_test(self):
        pass
