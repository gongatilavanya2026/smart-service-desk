# Smart Service Desk Management System

## 1. Project Overview

A company receives IT support requests from employees regarding laptop, software, network, password, account, and access-related issues. Earlier, these requests were maintained manually.

To make this process easier, I developed a Smart Service Desk Management System that allows support staff to create, view, search, and resolve service requests.

The application is developed using Python and follows Object-Oriented Programming (OOP), exception handling, JSON file handling, SOLID principles, and basic Domain-Driven Design (DDD).

All service request information is stored in a JSON file, ensuring that the data remains available even after the application is closed and restarted.

## 2. Features Implemented

The application provides the following functionalities:

### 2.1 Create Service Request
- Allows users to create a new service request.
- Accepts Request ID, Employee Name, Issue Description, and Priority.
- Automatically assigns the initial status as OPEN.
- Prevents duplicate Request IDs.
- Validates the priority entered by the user.

### 2.2 View All Requests
- Displays all saved service requests.
- Shows Request ID, Employee Name, Issue Description, Priority, and Status.

### 2.3 Search Request
- Allows users to search for a service request using its Request ID.
- Displays complete request details if the request exists.
- Displays a friendly error message if the request is not found.

### 2.4 Resolve Request
- Allows users to resolve an OPEN service request.
- Changes the status from OPEN to RESOLVED.
- Prevents an already resolved request from being resolved again.
- Saves the updated status in the JSON file.

### 2.5 Data Persistence
- Stores all service requests in `data/requests.json`.
- Loads existing requests when the application starts.
- Automatically saves data after creating or resolving a request.
- Handles missing, empty, or invalid JSON files safely.

## 3. Service Request Details

Each service request contains the following attributes:

| Attribute | Description | Example |
|---|---|---|
| Request ID | Unique identification of the request | SR101 |
| Employee Name | Name of the employee | Rahul |
| Issue Description | Description of the IT issue | Laptop is not starting |
| Priority | Importance of the request | HIGH |
| Status | Current state of the request | OPEN |

### Allowed Values

**Priority:**
- LOW
- MEDIUM
- HIGH

**Status:**
- OPEN
- RESOLVED

## 4. Technologies and Concepts Used

| Technology / Concept | Purpose |
|---|---|
| Python | Main programming language |
| OOP | Organizing the application using classes and objects |
| Exception Handling | Handling errors without crashing the application |
| Custom Exceptions | Handling application-specific errors |
| JSON | Storing service request information |
| File Handling | Reading and writing request data |
| SOLID Principles | Maintaining clean and maintainable code |
| DDD | Separating the application into different layers |
| Git and GitHub | Version control and source code management |

## 5. Object-Oriented Programming (OOP)

OOP is implemented using the `ServiceRequest` class in the domain layer.

### ServiceRequest Class

The class represents an individual service request.

**Attributes:**
- request_id
- employee_name
- issue
- priority
- status

**Constructor:**

The `__init__()` constructor initializes the service request attributes when an object is created.

**Methods:**

- `resolve()` – Changes the request status from OPEN to RESOLVED.
- `to_dict()` – Converts the request object into a dictionary for JSON storage.
- `from_dict()` – Creates a ServiceRequest object from stored dictionary data.

### Encapsulation

The request-related data and behaviour are maintained inside the ServiceRequest class.

The `resolve()` method is used to change the request status instead of directly modifying it from multiple places.

## 6. Exception Handling

Exception handling is implemented to manage expected errors without terminating the application.

The following custom exceptions are implemented:

| Exception | Purpose |
|---|---|
| DuplicateRequestError | Raised when an existing Request ID is entered again |
| RequestNotFoundError | Raised when a requested ID does not exist |
| InvalidPriorityError | Raised when an invalid priority is entered |
| AlreadyResolvedError | Raised when an already resolved request is resolved again |

The application also handles:
- Empty input fields.
- Invalid menu choices.
- Missing JSON files.
- Empty or invalid JSON files.

Clear and user-friendly error messages are displayed whenever an error occurs.

## 7. File Handling and Data Persistence

The application uses a JSON file to store all service requests.

**File location:**

`data/requests.json`

The application performs the following operations:

1. Loads existing requests when the application starts.
2. Saves a new request after successful creation.
3. Updates the JSON file after resolving a request.
4. Retrieves previously saved requests even after restarting the application.

### Example JSON Data

```json
[
    {
        "request_id": "SR101",
        "employee_name": "Rahul",
        "issue": "Laptop is not starting",
        "priority": "HIGH",
        "status": "RESOLVED"
    }
]
```

This ensures data persistence across multiple application executions.

## 8. SOLID Principles

The application mainly demonstrates the following SOLID principles:

### 8.1 Single Responsibility Principle (SRP)

Each component has a separate responsibility.

- ServiceRequest: Manages request data and domain behaviour.
- RequestService: Handles application operations.
- FileRepository: Handles JSON file reading and writing.
- main.py: Handles user input, menu display, and application flow.

### 8.2 Dependency Inversion Principle (DIP)

The RequestService does not directly handle JSON file operations.

Instead, the repository is passed to RequestService through its constructor.

This is called Dependency Injection.

It separates business operations from file storage implementation.

## 9. Basic Domain-Driven Design (DDD)

The application follows a layered structure based on basic Domain-Driven Design.

The project is divided into four main layers.

### 9.1 Domain Layer

Location: `domain/`

Contains:
- ServiceRequest class.
- Request attributes and methods.
- Priority validation.
- Resolve behaviour.
- Custom domain exceptions.

### 9.2 Application Layer

Location: `application/`

Contains the RequestService class.

Implements the main application operations:

- `create_request()`
- `view_requests()`
- `search_request()`
- `resolve_request()`

It coordinates the business operations and communicates with the repository.

### 9.3 Infrastructure Layer

Location: `infrastructure/`

Contains the FileRepository class.

Responsible for:
- Reading request data from JSON.
- Writing request data into JSON.
- Loading saved requests.
- Handling missing or invalid JSON files.

### 9.4 Presentation Layer

Location: `main.py`

Responsible for:
- Displaying the application menu.
- Accepting user input.
- Calling application service methods.
- Displaying results and error messages.
- Managing the application flow.

## 10. Project Folder Structure

```text
smart-service-desk/
│
├── domain/
│   ├── __init__.py
│   ├── service_request.py
│   └── exceptions.py
│
├── application/
│   ├── __init__.py
│   └── request_service.py
│
├── infrastructure/
│   ├── __init__.py
│   └── file_repository.py
│
├── data/
│   └── requests.json
│
├── main.py
├── README.md
└── .gitignore
```

## 11. Application Menu

When the application starts, the following menu is displayed:

```text
========== SMART SERVICE DESK SYSTEM ==========

1. Create Service Request
2. View All Requests
3. Search Request
4. Resolve Request
5. Exit

Enter your choice:
```

The user can select an option to perform the required operation.

## 12. Steps to Run the Application

### Prerequisites

- Python 3.10 or later.
- Visual Studio Code or any Python-supported IDE.
- Git (for version control).

### Execution Steps

1. Clone or download the project repository.
2. Open the project folder in Visual Studio Code.
3. Open the terminal.
4. Navigate to the project root directory.
5. Execute the following command:

```bash
python main.py
```

6. The Smart Service Desk menu will appear.
7. Select the required operation.

No external Python libraries are required.

## 13. Testing and Validation

The following test cases are used to verify the application.

| Test Case | Expected Result |
|---|---|
| Create a new request | Request created successfully |
| Create duplicate Request ID | Duplicate error displayed |
| Enter invalid priority | Priority validation error displayed |
| View all requests | All saved requests displayed |
| Search existing Request ID | Request details displayed |
| Search invalid Request ID | Request not found message displayed |
| Resolve OPEN request | Status changes to RESOLVED |
| Resolve already resolved request | Already resolved message displayed |
| Restart application | Previously saved requests are loaded |
| Search after restart | Latest request status is displayed |

### Persistence Testing

1. Create a service request with Request ID SR101.
2. Exit the application.
3. Restart the application using `python main.py`.
4. Search for SR101.
5. Verify that the request details are still available.
6. Verify that the latest status is maintained.

## 14. Git and GitHub Workflow

Git is used for version control and GitHub is used to maintain the remote repository.

The project uses two branches:

- `main` – Contains the final working version of the application.
- `development` – Used for implementing and testing the application.

### Meaningful Commits

The following commits are used to maintain the development history:

1. `Create initial project structure`
2. `Add ServiceRequest domain model and exceptions`
3. `Add JSON file repository`
4. `Add request service and business operations`
5. `Complete CLI application and documentation`

### Merge Commands

After completing development and testing:

```bash
git checkout main
git merge development
git push origin main
```

The final working application is maintained in the main branch.

## 15. Conclusion

The Smart Service Desk Management System provides a simple and organized solution for managing employee IT support requests.

The application successfully implements request creation, viewing, searching, and resolution along with exception handling and JSON-based data persistence.
