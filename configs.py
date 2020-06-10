from config_manager import Config


## Init pre-defined environments:
required_envs = ["required_test_env"]
optional_envs = {
    "optional_env_test1": "1",
    "optional_env_test2": "2"
}

## Load Env file to pars configurations.
Configs = Config(required_envs,optional_envs)
Configs.load_initial_env("./..env")