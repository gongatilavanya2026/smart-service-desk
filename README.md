# Smart Service Desk Management System

A command-line Python application for creating, viewing, searching, and resolving employee IT service requests. Requests are persisted in `data/requests.json`.

## Features
- Create requests with unique IDs and LOW, MEDIUM, or HIGH priority.
- Automatically assign OPEN status to new requests.
- View all saved requests.
- Search by Request ID.
- Resolve an OPEN request; prevent resolving it twice.
- Persist data in JSON across application restarts.
- Handle expected errors using custom exceptions.

## Concepts demonstrated
- OOP: `ServiceRequest` class, constructor, attributes, and methods.
- Encapsulation: `resolve()` owns the status transition.
- Exceptions: custom service desk exceptions.
- File handling: JSON repository.
- SOLID: separate domain, application, infrastructure, and presentation responsibilities; `RequestService` depends on a repository protocol rather than a concrete JSON class.
- Basic DDD: domain model and layered project structure.

## Project structure
```text
smart-service-desk/
├── domain/
│   ├── service_request.py
│   └── exceptions.py
├── application/
│   └── request_service.py
├── infrastructure/
│   └── file_repository.py
├── data/
│   └── requests.json
├── main.py
├── README.md
└── .gitignore
```

## Requirements
Python 3.9 or later. No third-party packages are required.

## Run
Open a terminal in the project root and execute:
```bash
python main.py
```

## Git workflow
Create a `development` branch from `main`, make meaningful commits on `development`, test the application, then merge `development` into `main` and push both branches.
