# Automation Strategy – Test Automation Process, Lifecycle & Framework Types

## Name:

**Shamrutha**

## Course:

Digital Nurture 5.0 – QA Concepts & Selenium Basics

---

# Task 1: Automation Decision and Test Case Selection

## 17. Criteria for Deciding Whether a Test Case Should Be Automated

### Criterion 1: Repetitive Execution

Tests that are executed frequently are ideal candidates for automation because they save time and reduce manual effort.

**Application to Scenario:**
The `POST /api/courses/` endpoint is tested after every code change, making it suitable for automation.

---

### Criterion 2: Regression Testing

Regression tests verify that existing functionality continues to work after updates.

**Application to Scenario:**
The course creation API is a core feature that should be included in every regression cycle, so it should be automated.

---

### Criterion 3: Stable Functionality

Automation works best for features whose requirements do not change frequently.

**Application to Scenario:**
The expected behavior of returning **HTTP 201 Created** for valid course creation is stable, making it a good automation candidate.

---

### Criterion 4: Data-Driven Testing

Tests requiring multiple input combinations benefit greatly from automation.

**Application to Scenario:**
Different course names, codes, durations, and instructors can be tested automatically using multiple datasets.

---

### Criterion 5: High Business Risk

Critical business functions should always be verified through automation.

**Application to Scenario:**
Creating a course is a primary function of the Course Management API. Any failure directly impacts users, making automation highly valuable.

---

## 18. Automate or Manual?

| Test Case                                                      | Decision     | Justification                                                        |
| -------------------------------------------------------------- | ------------ | -------------------------------------------------------------------- |
| Regression test for all CRUD endpoints after every code change | **Automate** | Executed frequently and ideal for regression automation.             |
| Exploratory testing of a new search feature                    | **Manual**   | Requires human creativity and investigation.                         |
| Performance test with 100 concurrent users                     | **Automate** | Performance testing requires automated load generation.              |
| UI test for the login form                                     | **Automate** | Login is a stable, repetitive feature that benefits from automation. |
| Verify API documentation (Swagger) is accurate                 | **Manual**   | Documentation requires human review for completeness and clarity.    |
| Smoke test to verify API availability after deployment         | **Automate** | Quick automated checks provide immediate deployment feedback.        |

---

## 19. Test Automation ROI

### Definition

Test Automation Return on Investment (ROI) measures when the time and cost invested in automation become lower than repeatedly executing the same tests manually.

---

### Given

* Automation development time = **4 hours**
* Manual execution time = **30 minutes (0.5 hour)**

---

### ROI Calculation

Break-even point:

**4 ÷ 0.5 = 8 runs**

Therefore, after **8 executions**, automation becomes more cost-effective than manual testing.

---

### Maintenance Overhead

After the 10th execution, assume a **20% maintenance overhead**.

Manual execution time per run = **0.5 hour**

Maintenance time per run:

20% × 0.5 = **0.1 hour**

Even with maintenance, automation continues to provide significant time savings because each additional execution requires far less effort than running the entire test manually.

---

## 20. Flaky Tests

### Definition

A flaky test is a test that sometimes passes and sometimes fails even though the application has not changed.

---

### Example

A Selenium test clicks the **Login** button before the page finishes loading.

Sometimes the page loads quickly and the test passes.

Sometimes it loads slowly and the test fails.

---

### Strategies to Prevent Flaky Tests

1. Use explicit waits instead of fixed delays (`Thread.sleep()`).
2. Use reliable and stable element locators such as IDs or CSS selectors.
3. Ensure each test is independent and begins with a clean application state.

---

# Task 2: Compare Automation Framework Types

## 21. Automation Framework Comparison

### 1. Linear Framework

**Description**

The Linear Framework is the simplest automation framework where test steps are executed sequentially in a single script without code reuse.

**Advantage**

* Easy to understand and implement.

**Disadvantage**

* Difficult to maintain as the project grows.

**Course Management Example**

* Automating a simple login test for demonstration purposes.

---

### 2. Modular Framework

**Description**

The Modular Framework divides the application into reusable modules. Each module contains automation scripts for a specific feature.

**Advantage**

* High code reusability.

**Disadvantage**

* Requires initial effort to identify and organize modules.

**Course Management Example**

* Separate modules for Login, Courses, Students, and Faculty.

---

### 3. Data-Driven Framework

**Description**

Test data is stored separately in files such as Excel, CSV, or JSON while the automation script reads the data during execution.

**Advantage**

* Easily tests multiple input combinations.

**Disadvantage**

* Data management becomes more complex.

**Course Management Example**

* Testing login with many usernames and passwords.

---

### 4. Keyword-Driven Framework

**Description**

Test cases are written using predefined keywords such as Login, Click, EnterText, and Verify.

**Advantage**

* Non-technical users can create test cases.

**Disadvantage**

* Initial framework development is time-consuming.

**Course Management Example**

* Business analysts create login tests using keywords without writing Selenium code.

---

### 5. Hybrid Framework

**Description**

The Hybrid Framework combines Modular, Data-Driven, and Keyword-Driven approaches to maximize flexibility and maintainability.

**Advantage**

* Highly scalable and reusable.

**Disadvantage**

* More complex to design and maintain initially.

**Course Management Example**

* Enterprise-level automation covering login, CRUD operations, regression, and multiple datasets.

---

## 22. Recommended Framework

### Recommendation

A **Hybrid Framework** combining **Modular**, **Data-Driven**, and **Keyword-Driven** approaches is the best choice.

### Justification

* **Data-Driven Framework** supports testing login with **50 username/password combinations**.
* **Modular Framework** allows the login functionality to be reused across **20 different test cases**.
* **Keyword-Driven Framework** enables non-technical team members to create or modify tests using predefined keywords.
* The Hybrid Framework combines all these benefits, making it ideal for a large Selenium project.

---

## 23. Hybrid Framework Folder Structure

```text
CourseManagementAutomation/

│
├── config/
│   ├── config.properties
│   └── browser.properties
│
├── testdata/
│   ├── loginData.xlsx
│   ├── courseData.xlsx
│   └── users.csv
│
├── pages/
│   ├── LoginPage.java
│   ├── CoursePage.java
│   └── DashboardPage.java
│
├── tests/
│   ├── LoginTest.java
│   ├── CourseTest.java
│   └── SmokeTest.java
│
├── utilities/
│   ├── ExcelReader.java
│   ├── BrowserFactory.java
│   ├── WaitHelper.java
│   └── ScreenshotUtil.java
│
├── keywords/
│   ├── LoginKeywords.java
│   ├── CourseKeywords.java
│   └── CommonKeywords.java
│
├── reports/
│
├── screenshots/
│
└── pom.xml
```

### Folder Description

* **config/** – Stores framework configuration files.
* **testdata/** – Contains Excel, CSV, or JSON test data.
* **pages/** – Implements the Page Object Model for each application page.
* **tests/** – Contains Selenium test scripts.
* **utilities/** – Common helper classes such as waits, browser setup, screenshots, and Excel readers.
* **keywords/** – Reusable keyword implementations for Keyword-Driven testing.
* **reports/** – Stores generated test execution reports.
* **screenshots/** – Saves screenshots captured during test execution.

---

# Conclusion

Choosing the right automation strategy requires evaluating business value, stability, execution frequency, and maintenance effort. Core regression, smoke, performance, and data-driven tests are ideal for automation, while exploratory and documentation reviews are better suited for manual testing. Among automation frameworks, the Hybrid Framework offers the best balance of scalability, maintainability, reusability, and collaboration, making it the preferred choice for automating the Course Management frontend using Selenium.
