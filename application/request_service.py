from typing import Protocol

from domain.service_request import ServiceRequest
from domain.exceptions import DuplicateRequestError, RequestNotFoundError


class RequestRepository(Protocol):
    """Storage contract. The application depends on this abstraction."""
    def load_all(self): ...
    def save_all(self, requests): ...


class RequestService:
    """Contains application use cases; does not perform JSON file operations."""
    def __init__(self, repository: RequestRepository):
        self.repository = repository

    def create_request(self, request_id, employee_name, issue, priority):
        requests = self.repository.load_all()
        normalized_id = str(request_id).strip().upper()
        if any(req.request_id == normalized_id for req in requests):
            raise DuplicateRequestError(
                f"Request ID {normalized_id} already exists. Please use another ID."
            )

        request = ServiceRequest(normalized_id, employee_name, issue, priority)
        requests.append(request)
        self.repository.save_all(requests)
        return request

    def view_requests(self):
        return self.repository.load_all()

    def search_request(self, request_id):
        normalized_id = str(request_id).strip().upper()
        for request in self.repository.load_all():
            if request.request_id == normalized_id:
                return request
        raise RequestNotFoundError(f"Request {normalized_id} was not found.")

    def resolve_request(self, request_id):
        requests = self.repository.load_all()
        normalized_id = str(request_id).strip().upper()
        for request in requests:
            if request.request_id == normalized_id:
                request.resolve()
                self.repository.save_all(requests)
                return request
        raise RequestNotFoundError(f"Request {normalized_id} was not found.")
