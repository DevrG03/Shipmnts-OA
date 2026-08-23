class DomainException(Exception):
    """Base exception for all domain errors."""
    def __init__(self, message: str = "A domain error occurred"):
        self.message = message
        super().__init__(self.message)


class EntityNotFoundError(DomainException):
    def __init__(self, entity_name: str, entity_id: any):
        super().__init__(f"{entity_name} with identifier '{entity_id}' was not found.")


class EntityConflictError(DomainException):
    def __init__(self, message: str = "Entity with given details already exists."):
        super().__init__(message)


class ValidationDomainError(DomainException):
    def __init__(self, message: str = "Invalid input or business rule violation."):
        super().__init__(message)


class UnauthorizedError(DomainException):
    def __init__(self, message: str = "Invalid or expired credentials."):
        super().__init__(message)


class ForbiddenError(DomainException):
    def __init__(self, message: str = "You do not have permission to perform this action."):
        super().__init__(message)
