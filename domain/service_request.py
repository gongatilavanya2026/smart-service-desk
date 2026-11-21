from domain.exceptions import InvalidPriorityError, AlreadyResolvedError


class ServiceRequest:
    ALLOWED_PRIORITIES = {"LOW", "MEDIUM", "HIGH"}
    ALLOWED_STATUSES = {"OPEN", "RESOLVED"}

    def __init__(self, request_id, employee_name, issue, priority, status="OPEN"):
        priority = str(priority).strip().upper()
        status = str(status).strip().upper()

        if priority not in self.ALLOWED_PRIORITIES:
            raise InvalidPriorityError("Priority must be LOW, MEDIUM or HIGH.")
        if status not in self.ALLOWED_STATUSES:
            raise ValueError("Status must be OPEN or RESOLVED.")

        self.request_id = str(request_id).strip().upper()
        self.employee_name = str(employee_name).strip()
        self.issue = str(issue).strip()
        self.priority = priority
        self.status = status

        if not self.request_id:
            raise ValueError("Request ID cannot be empty.")
        if not self.employee_name:
            raise ValueError("Employee name cannot be empty.")
        if not self.issue:
            raise ValueError("Issue description cannot be empty.")

    def resolve(self):
        """Change an OPEN request to RESOLVED."""
        if self.status == "RESOLVED":
            raise AlreadyResolvedError(
                f"Request {self.request_id} is already resolved."
            )
        self.status = "RESOLVED"

    def to_dict(self):
        return {
            "request_id": self.request_id,
            "employee_name": self.employee_name,
            "issue": self.issue,
            "priority": self.priority,
            "status": self.status,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            request_id=data["request_id"],
            employee_name=data["employee_name"],
            issue=data["issue"],
            priority=data["priority"],
            status=data.get("status", "OPEN"),
        )
