import sys
import json
import os
from Experiment import Experiment


class ExperimentManager:
    def __init__(self, name, full_path):
        """
        :param name: Name of experiment.
        :param full_path: full path to experiment.
        """
        self.name = name
        self.full_path = full_path
        self.experiments = []

    def run_experiment(self, name, model, data_path, data_iterator):
        """
        :param name: Name of run.
        :param model: Python function that is the model (keras/tensorflow)
        :param data_path: Path to dataset
        :param data_iterator: Iterator object that will yield data for training or testing accordingly
        :return:
        """
        experiment = Experiment(name, os.path.join(self.full_path, name), model, data_path, data_iterator)
        self.experiments.append(experiment.full_path)


if __name__ == '__main__':
   e = ExperimentManager('temp', '~/Projects/coding_project/ExperimentManager/')
   e.run_experiment('tepmp', min, '/x/x/x', object)
   x = json.dumps(e.__dict__)
   print(x)
