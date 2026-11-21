from application.request_service import RequestService
from infrastructure.file_repository import FileRepository
from domain.exceptions import (
    ServiceDeskError,
    InvalidPriorityError,
)


def display_request(request):
    print("\nRequest details")
    print("---------------")
    print(f"Request ID    : {request.request_id}")
    print(f"Employee Name : {request.employee_name}")
    print(f"Issue         : {request.issue}")
    print(f"Priority      : {request.priority}")
    print(f"Status        : {request.status}")


def main():
    repository = FileRepository()
    service = RequestService(repository)

    while True:
        print("\n========== SMART SERVICE DESK ==========")
        print("1. Create Service Request")
        print("2. View All Requests")
        print("3. Search Request")
        print("4. Resolve Request")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                request_id = input("Enter Request ID: ")
                employee_name = input("Enter Employee Name: ")
                issue = input("Enter Issue Description: ")
                priority = input("Enter Priority (LOW/MEDIUM/HIGH): ")
                request = service.create_request(
                    request_id, employee_name, issue, priority
                )
                print(f"\nService request {request.request_id} created successfully.")
                print("Status: OPEN")

            elif choice == "2":
                requests = service.view_requests()
                if not requests:
                    print("No service requests found.")
                else:
                    print("\nID | Employee | Issue | Priority | Status")
                    print("-" * 75)
                    for request in requests:
                        print(
                            f"{request.request_id} | {request.employee_name} | "
                            f"{request.issue} | {request.priority} | {request.status}"
                        )

            elif choice == "3":
                request_id = input("Enter Request ID to search: ")
                display_request(service.search_request(request_id))

            elif choice == "4":
                request_id = input("Enter Request ID to resolve: ")
                request = service.resolve_request(request_id)
                print(f"Request {request.request_id} has been resolved successfully.")

            elif choice == "5":
                print("Exiting Smart Service Desk. Goodbye!")
                break

            else:
                print("Invalid menu choice. Please enter a number from 1 to 5.")

        except InvalidPriorityError as exc:
            print(f"Invalid priority: {exc}")
        except ServiceDeskError as exc:
            print(f"Error: {exc}")
        except ValueError as exc:
            print(f"Invalid input: {exc}")


if __name__ == "__main__":
    try:
        main()
    except ServiceDeskError as exc:
        print(f"Unable to start because request data could not be loaded: {exc}")
