from config_manager import Config

required_envs = ["A"]
optional_envs = {
    "env1": "1",
    "env2": "2"
}

Configs = Config(required_envs,optional_envs)
Configs.load_initial_env("./..env")