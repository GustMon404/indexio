from enum import Enum


class STATUS(str, Enum):
    PENDING = 'Pending'
    PROCESSING = 'Processing'
    FINISHED = 'Finished'
    ERROR = 'Error'


class ERROR_TYPE(str, Enum):
    JSON_INVALID = 'Json Invalid'
    OBJECT_NOT_FOUND = 'Object not Found'
    UPDATE_ERROR = 'Updater Error'
