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