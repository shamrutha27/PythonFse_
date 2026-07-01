# V-Model Analysis – SDLC vs TDLC

## Name:

**Shamrutha**

## Course:

Digital Nurture 5.0 – QA Concepts & Selenium Basics

---

# Task 1: V-Model Mapping

## 9. V-Model Diagram

The V-Model establishes a direct relationship between each Software Development Life Cycle (SDLC) phase and its corresponding Testing Development Life Cycle (TDLC) phase.

```text
                 SDLC (Development)

            Requirements
                 │
                 │
            System Design
                 │
                 │
         Architecture Design
                 │
                 │
            Module Design
                 │
                 │
               Coding
                 ▲
                 │
          Unit Testing
                 │
                 │
      Integration Testing
                 │
                 │
         System Testing
                 │
                 │
      Acceptance Testing

               TDLC (Testing)
```

### SDLC ↔ TDLC Mapping

| SDLC Phase          | Corresponding TDLC Phase            |
| ------------------- | ----------------------------------- |
| Requirements        | Acceptance Testing                  |
| System Design       | System Testing                      |
| Architecture Design | Integration Testing                 |
| Module Design       | Unit Testing                        |
| Coding              | Execution of all testing activities |

---

## 10. Test Artifacts Produced During Development

| SDLC Phase          | Corresponding Testing Phase | Test Artifact Produced                           |
| ------------------- | --------------------------- | ------------------------------------------------ |
| Requirements        | Acceptance Testing          | Acceptance Test Plan and Acceptance Test Cases   |
| System Design       | System Testing              | System Test Plan and System Test Cases           |
| Architecture Design | Integration Testing         | Integration Test Plan and Integration Test Cases |
| Module Design       | Unit Testing                | Unit Test Cases and Unit Test Plan               |
| Coding              | All Testing Levels          | Source Code, Build, and Executable Application   |

---

## 11. Entry and Exit Criteria

### Unit Testing

**Entry Criteria**

* Module coding completed.
* Unit test cases prepared.
* Development environment is ready.

**Exit Criteria**

* All unit test cases executed.
* All critical defects fixed.
* Code coverage meets project standards.

---

### Integration Testing

**Entry Criteria**

* All modules have passed unit testing.
* Integration environment is available.
* Integration test cases are ready.

**Exit Criteria**

* All integration test cases executed.
* Interfaces between modules work correctly.
* No unresolved critical integration defects.

---

### System Testing

**Entry Criteria**

* Complete application is integrated.
* System test plan approved.
* Test environment is configured.

**Exit Criteria**

* All planned system test cases executed.
* No Critical or High severity defects remain open.
* Application satisfies functional and non-functional requirements.

---

### Acceptance Testing

**Entry Criteria**

* System testing completed successfully.
* Application deployed in UAT environment.
* Business users are available for testing.

**Exit Criteria**

* Users approve the application.
* All acceptance criteria satisfied.
* Product is ready for production deployment.

---

## 12. Early QA Engagement in the Course Management API Project

### 1. Requirements Review

QA reviews the functional requirements before development begins to identify ambiguities, missing requirements, and testability issues.

Example:

* Verify whether the course code must be unique.
* Check validation rules for mandatory fields.

---

### 2. Design Review

QA participates in reviewing the API design and database schema.

Example:

* Ensure API endpoints follow REST standards.
* Verify response codes and error handling.
* Review database relationships for consistency.

Early QA involvement helps prevent defects before coding starts, reducing both cost and development time.

---

# Task 2: Agile QA and Shift-Left Testing

## 13. Problems with Waterfall Testing

### Problem 1: Late Defect Detection

Testing begins only after development is complete, making defects more expensive and time-consuming to fix.

---

### Problem 2: Requirement Misunderstandings

If developers misunderstand a requirement, the issue is discovered only during testing, resulting in significant rework.

---

### Problem 3: Delayed Product Delivery

Finding many defects late in the project delays testing, bug fixing, and final release of the Course Management API.

---

## 14. QA Role in Agile Ceremonies

### Sprint Planning

* Review user stories.
* Define acceptance criteria.
* Estimate testing effort.
* Identify testing risks.

---

### Daily Standup

* Share testing progress.
* Report blocked test cases.
* Communicate defects affecting the sprint.

---

### Sprint Review

* Validate completed features.
* Demonstrate tested functionality.
* Confirm acceptance criteria are met.

---

### Sprint Retrospective

* Discuss testing challenges.
* Suggest improvements to the QA process.
* Recommend better automation or collaboration practices.

---

## 15. Shift-Left Testing Practices

### a) Requirement Review for Testability

QA reviews requirements before development starts.

Example:
Ensure the API clearly specifies mandatory fields, validation rules, and expected HTTP response codes.

---

### b) Writing Test Cases Before Code (TDD/BDD)

Test scenarios are prepared before implementation begins.

Example:
Create test cases for the `POST /api/courses` endpoint before developers write the API.

---

### c) Static Code Analysis

Developers analyze source code using static analysis tools to detect coding issues before execution.

Example:
Identify unused variables, coding standard violations, or potential security vulnerabilities in the Course Management API.

---

### d) API Contract Testing Before Integration

Verify that the API adheres to the agreed request and response contract before integrating with other services.

Example:
Ensure the API always returns the expected JSON structure and HTTP status codes defined in the API specification.

---

## 16. Acceptance Criteria (Given-When-Then Format)

### Scenario 1: Successful Course Creation

**Given**
The college administrator is logged into the system.

**When**
The administrator submits valid course details.

**Then**
The course is created successfully and the system returns **HTTP 201 Created**.

---

### Scenario 2: Duplicate Course Code

**Given**
A course with the same course code already exists.

**When**
The administrator attempts to create another course using that course code.

**Then**
The system displays an appropriate error message and returns **HTTP 409 Conflict**.

---

### Scenario 3: Missing Required Fields

**Given**
The administrator leaves one or more mandatory fields empty.

**When**
The administrator submits the course creation request.

**Then**
The system displays validation errors for the missing fields and returns **HTTP 400 Bad Request**.

---

# Conclusion

The V-Model demonstrates how every development phase is paired with a corresponding testing phase, ensuring early planning and comprehensive validation. By integrating QA throughout Agile ceremonies and adopting Shift-Left practices, defects can be identified and prevented much earlier, resulting in higher software quality, reduced development costs, and faster delivery of the Course Management API.
