import sys
import os
from pathlib import Path
from dotenv import load_dotenv


class ConfigError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"Config Manager Error : {self.message}"


class ConfigHolder(dict):
    def __init__(self, init={}, name=None):
        dict.__init__(self, init)

    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, dict.__repr__(self))

    def __setitem__(self, key, value):
        return super(ConfigHolder, self).__setitem__(key, self._value_parser(value))

    def __getitem__(self, name):
        return super(ConfigHolder, self).__getitem__(name)

    def __delitem__(self, name):
        return super(ConfigHolder, self).__delitem__(name)

    def _value_parser(self, value):
        _true_values = ["true", "True", "TRUE", "1", 1]
        _false_values = ["false", "False", "FALSE", "0", 0]
        if value in _true_values:
            return True
        if value in _false_values:
            return False
        return value


class Config(ConfigHolder):
    def __init__(self, required_envs, optional_envs):
        self.required_envs = required_envs
        self.optional_envs = optional_envs

    def load_initial_env(self, fname):
        env_file = Path(".env")
        load_dotenv(verbose=True, dotenv_path=env_file)

        for x in self.required_envs:
            if os.environ.get(x, None) == None:
                raise ConfigError(f"The {x} envoronment is missing!")
            else:
                self[x] = os.environ.get(x)

        for k, v in self.optional_envs.items():
            self[k] = os.environ.get(k, v)

