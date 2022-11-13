def decorator(fn):
    def inner(*args, **kwargs):
        # 前置操作
        result = fn(*args, **kwargs)
        # 后置操作
        return result

    return inner




