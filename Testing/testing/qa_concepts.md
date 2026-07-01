# QA Concepts & Selenium Basics – Hands-On 1

## Name:

**Shamrutha**

## Course:

Digital Nurture 5.0 – QA Concepts & Selenium Basics

---

# Task 1: Map Testing Types to a Real System

## 1. Test Cases for Different Testing Levels

### a) Unit Testing

**Description:**
Test the function responsible for validating course data before saving it to the database.

**Test Case:**

* Input:

  * Course Name = "Python Basics"
  * Duration = 30
* Verify that the validation function returns **True** for valid data.
* Invalid data (empty course name) should return an appropriate validation error.

**Type:** Functional Testing

---

### b) Integration Testing

**Description:**
Verify that the `POST /api/courses/` endpoint correctly stores course details in the database.

**Test Case:**

* Send a POST request with valid course information.
* Verify that:

  * HTTP Status = 201 Created
  * Course record exists in the database.

**Type:** Functional Testing

---

### c) System Testing

**Description:**
Verify the complete flow of creating and retrieving a course.

**Test Case:**

1. Send POST request to create a new course.
2. Receive success response.
3. Send GET request to retrieve all courses.
4. Verify the newly created course appears in the response.

**Type:** Functional Testing

---

### d) User Acceptance Testing (UAT)

**Description:**
A college administrator verifies that the Course Management API supports daily operations.

**Test Case:**

* Login as Admin.
* Add a new course.
* Edit the course.
* View the course list.
* Delete the course.

The administrator confirms that all operations work as expected.

**Type:** Functional Testing

---

## 2. Functional vs Non-Functional Testing

### Functional Test

Verify that the API correctly creates a new course when valid data is submitted.

Expected Result:

* Course is added successfully.
* Status Code = 201 Created.

---

### Non-Functional Test

**Performance Testing**

Send **1000 simultaneous POST requests** to the API.

Verify:

* Average response time is less than 2 seconds.
* Server remains stable.
* No request failures occur.

---

## 3. Black-Box Testing vs White-Box Testing

### Black-Box Testing

Black-box testing verifies the software functionality without looking at the internal source code.

The tester only checks:

* Inputs
* Outputs
* Business requirements

Example:

Send a POST request and verify the response.

---

### White-Box Testing

White-box testing verifies the internal code structure, logic, conditions, loops, and execution paths.

Developers usually perform white-box testing while writing unit tests.

---

### Difference

| Black-Box Testing              | White-Box Testing              |
| ------------------------------ | ------------------------------ |
| No knowledge of source code    | Requires source code knowledge |
| Tests functionality            | Tests internal logic           |
| Performed mainly by QA Testers | Performed mainly by Developers |

---

## 4. Formal Test Cases for POST /api/courses/

| Test Case ID | Description                            | Preconditions         | Test Steps                                   | Expected Result                                          | Actual Result | Pass/Fail |
| ------------ | -------------------------------------- | --------------------- | -------------------------------------------- | -------------------------------------------------------- | ------------- | --------- |
| TC001        | Create course with valid data          | API running           | Send POST request with valid course details  | Course created successfully with HTTP 201                |               |           |
| TC002        | Create course with missing course name | API running           | Send POST request with empty course name     | HTTP 400 Bad Request with validation message             |               |           |
| TC003        | Create duplicate course                | Course already exists | Send POST request using existing course name | Duplicate course rejected with appropriate error message |               |           |

---

# Task 2: Defect Lifecycle & Severity Classification

## 5. Defect Lifecycle

```
New
  ↓
Assigned
  ↓
Open
  ↓
Fixed
  ↓
Retest
  ↓
Verified
  ↓
Closed
```

### Alternate Paths

**Rejected**

* Developer determines that the issue is not actually a defect.
* The defect status changes to **Rejected**.

**Deferred**

* The defect is valid but fixing it is postponed to a future release because of lower priority or time constraints.

---

## 6. Severity and Priority Classification

### a) POST /api/courses returns 500 Internal Server Error

**Severity:** Critical

**Priority:** P1

**Justification:**

The API cannot perform its primary function, preventing users from creating courses. It must be fixed immediately.

---

### b) Course names longer than 150 characters are silently truncated

**Severity:** Medium

**Priority:** P2

**Justification:**

The application continues working but causes data loss because users are not informed that the course name has been truncated.

---

### c) Swagger /docs page contains a typo

**Severity:** Low

**Priority:** P4

**Justification:**

This is only a documentation issue. The API functionality is not affected.

---

### d) Login occasionally returns 401 despite correct credentials

**Severity:** High

**Priority:** P1

**Justification:**

Although intermittent, users cannot reliably log in. This affects usability and indicates possible authentication instability.

---

## 7. Defect Report

### Defect ID

BUG-001

### Title

POST /api/courses returns HTTP 500 Internal Server Error for all requests

### Environment

* Windows 11
* Python 3.x
* FastAPI
* Chrome Browser
* Localhost

### Build Version

Version 1.0

### Severity

Critical

### Priority

P1

### Steps to Reproduce

1. Start the Course Management API.
2. Open Swagger UI.
3. Select POST `/api/courses/`.
4. Enter valid course details.
5. Click Execute.

### Expected Result

The course should be created successfully.

HTTP Status:

**201 Created**

### Actual Result

The API returns:

**500 Internal Server Error**

No course is created.

### Attachments

Screenshot of 500 Internal Server Error.

---

## 8. Difference Between Severity and Priority

### Severity

Severity indicates **how serious the defect is** and how much it impacts the application.

### Priority

Priority indicates **how urgently the defect should be fixed**.

---

### Example

A typo on the CEO's dashboard:

* Severity: Low (the application still works correctly)
* Priority: High (P1), because the CEO will see it during an important presentation.

This demonstrates that a defect can have **Low Severity but High Priority**, depending on the business impact.

---

# Conclusion

This exercise demonstrates the fundamentals of Quality Assurance, including testing levels, functional and non-functional testing, black-box and white-box testing, formal test case documentation, defect lifecycle management, defect reporting, and severity versus priority classification. These concepts provide the foundation for effective software testing and quality assurance practices.
