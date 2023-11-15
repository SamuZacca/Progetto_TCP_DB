import pickle


def string_to_bytes(data):

    if not isinstance(data, str):
        raise Exception()

    return data.encode()


def bytes_to_string(data):

    if not isinstance(data, bytes):
        raise Exception()

    return data.decode()


def list_to_bytes(data):

    if not isinstance(data, list):
        raise Exception()
    list_converted = pickle.dumps(data)
    return list_converted



def bytes_to_list(data):

    if not isinstance(data, bytes):
        raise Exception()

    return pickle.loads(data)


def dict_to_bytes(data):

    if not isinstance(data, dict):
        raise Exception()
    list_converted = pickle.dumps(data, -1)
    return list_converted


def bytes_to_dict(data):

    if not isinstance(data, bytes):
        raise Exception()

    return pickle.loads(data)