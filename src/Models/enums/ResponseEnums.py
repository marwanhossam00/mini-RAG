from enum import Enum

class ResponseSignals(Enum):


    FILE_VALIDATED_SUCCESS = "file_validated_successefully"
    FILE_TYPE_NOT_SUPPORTED = "file_type_not_supported"
    FILE_SIZE_EXCEEDED = "file_size_exceeded"
    FILE_UPLOAD_SUCCESSED = "file_upload_successed"
    FILE_UPLOAD_FAILED = "file_upload_failed"