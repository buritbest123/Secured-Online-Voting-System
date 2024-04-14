# Online Voting System

This project implements an e-Voting system designed to securely simulate an online voting environment. It incorporates robust features such as TCP socket programming, synchronized multithreading to handle multiple clients, and voter authentication to prevent repeated votes and ensure election integrity.

## Features

- **Secure Authentication:** Ensures that each voter is authenticated before voting.
- **Repeat Voting Prevention:** Each voter can only cast their vote once.
- **Voter and Candidate Data Management:** Stores voter and candidate information securely using CSV files.
- **Concurrent Client Handling:** Uses synchronized threads to handle multiple voting clients concurrently without interference.
- **Admin and Voter Interfaces:** Separate login interfaces for admin and voters to manage and participate in elections respectively.

## Requirements

- Python 3.x
- Pandas
- Tkinter for the GUI interface
- Socket programming for TCP connections
- Subprocess for OS-level command execution

## Installation

1. Clone the repository to your local machine (replace `[repo-link]` with the actual URL of the repository):
   ```bash
   git clone [repo-link]
   cd Online-Voting-System
   ```

2. No external libraries are needed beyond the standard Python libraries included in the requirements.

## Running the Application
1. Install the required cryptography package:
   ```bash
   pip install cryptography
   ```
2. Change directory to the project file:
   ```bash
   cd path_to_project_directory
   ```
3. Run the application:
   ```bash
   python -u "path_to_homePage.py"
   ```
   Replace `path_to_project_directory` and `path_to_homePage.py` with the actual paths in your system.

## How to Login

- **Admin Login:**
  - **Admin ID:** Admin
  - **Password:** admin

- **Voter Login:**
  - **Voter IDs:** 10001 to 10005
  - **Password:** abcd

## Additional Details
- **Admin and Voter Login:** Information about admin setup and voter registration.
- **Database Management:** Details on how the system uses CSV files to manage voter and candidate data.

## License

This project is released under the MIT License, which allows for extensive reusability and modification. Please see the `LICENSE.md` file for legal details.

## Contact Information

For further inquiries or issues, please contact us through our GitHub repository or email the project maintainers directly.

For any inquiries, bugs, or contributions, please contact the project team at their institute email addresses provided in the project report.

---

Please ensure to replace placeholders like `[repo-link]` with actual links and provide any additional necessary details that may not be included here. The structure and content are based on your system's described functionality and setup as provided in the report.
