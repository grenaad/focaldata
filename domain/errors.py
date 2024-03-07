class Error:
    msg: str = ""
    exception: Exception | None = None

    def __str__(self) -> str:
        if self.exception == None:
            return self.msg
        else:
            return self.msg + "\nException:\n" + str(self.exception)


class EmbeddingServiceAPIUnknown(Error):
    msg = "Embedding Service Error: Unkown error"

    def __init__(self, exception: Exception):
        self.exception = exception


class EmbeddingServiceAPIAuthenticationError(Error):
    msg = "Embedding Service Error: Authentication error"


class EmbeddingServiceAPIPermissionDeniedError(Error):
    msg = "Embedding Service Error: Permission denied error"


class EmbeddingServiceAPIRateLimitError(Error):
    msg = "Embedding Service Error: Rate Limited error"


class EmbeddingServiceAPIRateInternalServerError(Error):
    msg = "Embedding Service Error: Unkown error"


class EmbeddingServiceAPIConnectionError(Error):
    msg = "Embedding Service Error: Connection error"
