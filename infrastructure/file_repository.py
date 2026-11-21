import json
from pathlib import Path

from domain.service_request import ServiceRequest
from domain.exceptions import DataFileError


class FileRepository:
    """Persists service requests in a JSON file."""
    def __init__(self, file_path="data/requests.json"):
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.file_path.exists():
            self.file_path.write_text("[]", encoding="utf-8")

    def load_all(self):
        try:
            content = self.file_path.read_text(encoding="utf-8").strip()
            if not content:
                return []
            data = json.loads(content)
            if not isinstance(data, list):
                raise DataFileError("The JSON file must contain a list of requests.")
            return [ServiceRequest.from_dict(item) for item in data]
        except json.JSONDecodeError as exc:
            raise DataFileError("The requests.json file contains invalid JSON.") from exc
        except (OSError, KeyError, TypeError, ValueError) as exc:
            if isinstance(exc, DataFileError):
                raise
            raise DataFileError(f"Could not read request data: {exc}") from exc

    def save_all(self, requests):
        try:
            data = [request.to_dict() for request in requests]
            self.file_path.write_text(
                json.dumps(data, indent=4), encoding="utf-8"
            )
        except OSError as exc:
            raise DataFileError(f"Could not save request data: {exc}") from exc
