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
        :param model: Path to saved and compiled keras model.
        :param data_path: Path to dataset
        :param data_iterator: Iterator object that will yield data for training or testing accordingly
        :return:
        """
        experiment = Experiment(name, self.full_path, model, data_path, data_iterator)
        self.experiments.append(experiment.full_path)
        experiment.test_log_file()
        return experiment


if __name__ == '__main__':
   e = ExperimentManager('temp', '/home/guy/Projects/coding_projects/ExperimentManager/')
   exp = e.run_experiment('test', 'model0.keras', '/x/x/x', object)
   x = json.dumps(e.__dict__)
   print(exp.log_path)
