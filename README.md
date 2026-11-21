# Smart Service Desk Management System

## 1. Project Overview

### Project Statement

A company receives IT support requests from employees regarding laptop, software, network, password, account, and access-related issues. Managing these requests manually can make it difficult to organize, track, and resolve them efficiently.

The **Smart Service Desk Management System** provides a centralized solution for managing employee IT support requests. It allows support staff to create, view, search, and resolve service requests through a simple menu-driven application.

The application is developed using Python and follows Object-Oriented Programming (OOP), exception handling, JSON file handling, SOLID principles, and basic Domain-Driven Design (DDD).

All service request information is stored in a JSON file, ensuring data persistence even after the application is closed and restarted.

---

## 2. Features and Functionalities

The application provides the following functionalities:

### 2.1 Create Service Request
- Create a new service request.
- Accept Request ID, Employee Name, Issue Description, and Priority.
- Automatically assign the initial status as `OPEN`.
- Prevent duplicate Request IDs.
- Validate the priority entered by the user.

### 2.2 View All Requests
- Display all saved service requests.
- Show Request ID, Employee Name, Issue Description, Priority, and Status.

### 2.3 Search Request
- Search for a service request using its Request ID.
- Display complete request details if the request exists.
- Display an appropriate error message if the request is not found.

### 2.4 Resolve Request
- Resolve an existing OPEN service request.
- Change the status from `OPEN` to `RESOLVED`.
- Prevent an already resolved request from being resolved again.
- Save the updated status in the JSON file.

### 2.5 Data Persistence
- Store service requests in `data/requests.json`.
- Load existing requests when the application starts.
- Automatically save data after creating or resolving a request.
- Handle missing, empty, or invalid JSON files safely.

---

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

---

## 4. Technologies and Concepts Used

| Technology / Concept | Purpose |
|---|---|
| Python | Main programming language |
| Object-Oriented Programming | Organizing code using classes and objects |
| Exception Handling | Handling errors without terminating the application |
| Custom Exceptions | Managing application-specific errors |
| JSON | Storing structured service request information |
| File Handling | Reading and writing request data |
| SOLID Principles | Improving code maintainability and organization |
| Domain-Driven Design | Separating the application into different layers |
| Git | Version control |
| GitHub | Remote repository and source code management |

---

## 5. Object-Oriented Programming (OOP)

Object-Oriented Programming is implemented using the `ServiceRequest` class in the domain layer.

### ServiceRequest Class

The `ServiceRequest` class represents an individual service request.

**Attributes:**
- `request_id`
- `employee_name`
- `issue`
- `priority`
- `status`

### Constructor

The `__init__()` constructor initializes the attributes when a ServiceRequest object is created.

### Methods

| Method | Description |
|---|---|
| `__init__()` | Initializes service request attributes |
| `resolve()` | Changes the request status from OPEN to RESOLVED |
| `to_dict()` | Converts the request object into a dictionary |
| `from_dict()` | Creates a ServiceRequest object from dictionary data |

### Encapsulation

Encapsulation is implemented by keeping request-related data and behaviour within the `ServiceRequest` class.

The `resolve()` method controls the status transition and prevents an already resolved request from being resolved again.

---

## 6. Exception Handling

Exception handling is implemented to manage expected errors without terminating the application.

### Custom Exceptions

| Exception | Purpose |
|---|---|
| `DuplicateRequestError` | Raised when an existing Request ID is entered again |
| `RequestNotFoundError` | Raised when the requested ID does not exist |
| `InvalidPriorityError` | Raised when an invalid priority is entered |
| `AlreadyResolvedError` | Raised when an already resolved request is resolved again |

### Additional Error Handling

The application also handles:

- Empty input fields.
- Invalid menu choices.
- Missing JSON files.
- Empty or invalid JSON files.
- Invalid request details.

Clear and user-friendly error messages are displayed whenever an error occurs.

---

## 7. File Handling and Data Persistence

The application uses JSON (JavaScript Object Notation) to store service request information.

**File Location:**

`data/requests.json`

### Operations Performed

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

JSON-based storage ensures data persistence across multiple application executions.

---

## 8. SOLID Principles

The application demonstrates the following SOLID principles:

### 8.1 Single Responsibility Principle (SRP)

Each component has a separate responsibility.

| Component | Responsibility |
|---|---|
| ServiceRequest | Manages request data and domain behaviour |
| RequestService | Handles application operations |
| FileRepository | Handles JSON file reading and writing |
| main.py | Handles user input, menu display, and application flow |

This separation makes the application easier to maintain and modify.

### 8.2 Dependency Inversion Principle (DIP)

The `RequestService` does not directly handle JSON file operations.

Instead, the repository is passed to `RequestService` through its constructor.

This is an example of **Dependency Injection**.

It separates application business operations from the file storage implementation.

---

## 9. Basic Domain-Driven Design (DDD)

The application follows a layered architecture based on basic Domain-Driven Design.

The project is divided into four main layers.

### 9.1 Domain Layer

**Location:** `domain/`

Contains:
- `ServiceRequest` class.
- Request attributes and methods.
- Priority validation.
- Resolve behaviour.
- Custom domain exceptions.

This layer represents the core business concepts and rules.

### 9.2 Application Layer

**Location:** `application/`

Contains the `RequestService` class.

Implements the following operations:

- `create_request()`
- `view_requests()`
- `search_request()`
- `resolve_request()`

It coordinates application operations and communicates with the repository.

### 9.3 Infrastructure Layer

**Location:** `infrastructure/`

Contains the `FileRepository` class.

Responsible for:
- Reading request data from JSON.
- Writing request data into JSON.
- Loading saved requests.
- Handling missing or invalid JSON files.

### 9.4 Presentation Layer

**Location:** `main.py`

Responsible for:
- Displaying the application menu.
- Accepting user input.
- Calling application service methods.
- Displaying results and error messages.
- Managing the application flow.

---

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

---

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

---

## 12. Installation and Execution

### Prerequisites

- Python 3.10 or later.
- Visual Studio Code or any Python-supported IDE.
- Git (for version control).

### Step 1: Clone the Repository

Open the terminal and execute:

```bash
git clone <repository-url>
```

Replace `<repository-url>` with your actual GitHub repository URL.

### Step 2: Navigate to the Project Directory

```bash
cd smart-service-desk
```

### Step 3: Open the Project

Open the project folder in Visual Studio Code.

### Step 4: Run the Application

Execute the following command in the terminal:

```bash
python main.py
```

### Step 5: Use the Application

The Smart Service Desk menu will appear.

Select the required operation by entering the corresponding number.

**Note:** No external Python libraries are required.

---

## 13. Testing and Validation

The following test cases are used to verify the application's functionality.

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

1. Create a service request with Request ID `SR101`.
2. Exit the application.
3. Restart the application using `python main.py`.
4. Search for `SR101`.
5. Verify that the request details are still available.
6. Verify that the latest status is maintained.

---

## 14. Git and GitHub Workflow

Git is used for version control, while GitHub is used to maintain the remote repository.

### Branch Strategy

The project uses two branches:

| Branch | Purpose |
|---|---|
| `main` | Contains the final working version of the application |
| `development` | Used for implementing and testing application features |


### Merge Development into Main

After completing development and testing:

```bash
git checkout main
git merge development
```

### Push Changes to GitHub

```bash
git push origin main
git push origin development
```

The final working application is maintained in the `main` branch.

---

## 15. Conclusion

The Smart Service Desk Management System provides a simple and organized solution for managing employee IT support requests.

The application supports request creation, viewing, searching, and resolution along with exception handling and JSON-based data persistence.

By implementing Object-Oriented Programming, SOLID principles, and basic Domain-Driven Design, the application maintains a clear separation of responsibilities and provides a structured approach to software development.