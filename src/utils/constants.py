from os import environ

TASK_REPEAT_TIME = float(environ.get("TASK_REPEAT_TIME", 60))  # by seconds
