import sys
import time
import keras
import os


def is_unique_path(base, name):
    return name not in os.listdir(base)


class Experiment:
    def __init__(self, name, base_path, model_path, dataset_path, data_iterator, num_epochs=50, update_on_iter=1000):
        """
        :param name: Name of experiment run.
        :param base_path: Path of base dir for all relevant experiment.
        :param model: Path to a keras model that can be loaded.
        :param dataset_path: Path to dataset.
        :param data_iterator: Path to data iterator
        """
        self.name = name
        path = os.path.join(base_path, name)
        # if not is_unique_path(base_path, name):
        #     raise Exception("Path is not unique")
        self.full_path = path
        self.log_path = os.path.join(self.full_path, name + '_log_history.log')
        self.model = keras.models.load_model(os.path.join(self.full_path, model_path))
        self.dataset_path = dataset_path
        self.data_iterator = data_iterator
        self.num_epochs = num_epochs
        self.update_iteration = update_on_iter

    def run_train(self):
        # Todo: Add to summary of the compiled model to the log file.
        with open(self.log_path, 'w') as log:
            # Todo: Add start time of training to the log file.
            self.init_training_log(log)
            for e in range(self.num_epochs):
                # Todo: How to get only train data? maybe add methods that data_iterator needs to implement
                for i, X_train, y_train in enumerate(self.data_iterator):
                    self.model.train_on_batch(X_train, y_train)
                    if i % self.update_iteration == 0:
                        # Todo: Add implemented method in data_iterator that given a batch returns text summary of batch
                        # Todo: Add text line, print it and write it to the log file.
                        log.writelines([])

    def run_test(self):
        raise NotImplementedError

    def test_log_file(self):
        # Todo: Run test on init log file
        with open(self.log_path, 'w') as log:
            self.init_training_log(log)

    def init_training_log(self, log_file):
        time_struct = time.localtime()
        log_file.write('Training started on {}/{}/{} at {}:{}:{}\n'.format(time_struct[2], time_struct[1],
                                                                               time_struct[0], time_struct[3],
                                                                               time_struct[4], time_struct[5]))
        # Todo: Assert the log_file.write is a legal print function
        keras.utils.print_summary(self.model, print_fn=lambda x: log_file.write(x + '\n'))
