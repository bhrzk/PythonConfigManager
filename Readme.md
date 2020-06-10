
# Python Config Manager 

A simple and handy python script to handle configurations for a python project.

### How does it work?
Well, it's easy. You set your configurations as environment variables and let the script know what are those and the rest will be handled. 
Right now there are two types of environment supported: 

**1- Required:**
    These are the ones which if the module cannot find it will return an error and terminate the project from running.

**2- Optional:**
    These are the ones you set default value so if the module finds them ins environment will override the default otherwise the default value uses.

### Example: 

Initialization:

configs.py:
```python
    from configs import Configs

    required_envs = ["required_test_env"]

    optional_envs = {
        "optional_env_test1": "1",
        "optional_env_test2": "2"
    }

    Configs = Config(required_envs,optional_envs)
    Configs.load_initial_env("./..env")
```

Simple use get:

```python
    from configs import Configs    

    print(Configs["optional_env_test1"])
    # >>> 1

    # Set configs in runtime
    Configs["runtime_config"] = "hello"
    print(Configs["runtime_config"])
    # >>> hello

    # Change a config in runtime
    Configs["runtime_config"] = "bye"
    print(Configs["runtime_config"])
    # >>> bye

    # Delete a config
    del Configs["runtime_config"]
```


