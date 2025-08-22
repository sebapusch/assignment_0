# Assignment: Python Project Initialization

## Objective
Your task is to initialize a Python project from scratch using modern tooling. You will create a virtual environment, add a specific dependency, write a simple script, format it, and use Git to submit your work. An automatic check will assess whether you completed this assignment properly.


> [!IMPORTANT]
> **This assignment DOES NOT count towards your grade!.** 
> It is only for you to get familiar with the workflow and tools we will be using throughout the course. Your code will automatically be checked for style, formatting, versioning, and proper types.

## Instructions

### Part 1: Git and GitHub Setup

1.  **Clone the Repository:** Clone this repository to your local machine.
    ```bash
    git clone https://github.com/rug-oop-2526/assignment_0
    cd assignment_0
    ```

2.  **Create Your GitHub Repository:** Go to **[https://github.com/new](https://github.com/new)** and create a new repository. It does not matter if it's private or public. Do not initialize it with any files, i.e. select __No template__ and __Add README, Add .gitignore, Add license__ should be __off__. Then, copy its URL.

3.  **Change the origin of your repository:** You cloned the repository from **[https://github.com/rug-oop-2526/assignment_0](https://github.com/rug-oop-2526/assignment_0)**, but now we want to use the new repository you just created. You can do so by:
    ```bash
    git remote set-url origin YOUR_NEW_REPO_URL
    ```

### Part 2: Project Initialization

1.  **Initialize the Project:** Use `uv` to create a `pyproject.toml` file and a virtual environment. This command sets up your project to use Python 3.12. Both can be done through:
    ```bash
    uv init --python 3.12
    ```

2.  **Add NumPy Dependency:** Add `numpy` version `1.26.0` and `mypy` to your project. This command will update `pyproject.toml` and install the packages into your `.venv`.
    ```bash
    uv add numpy==1.26.0 mypy
    ```

3. **Activate Virtual Environment:** Activate your virtual environment with:
    ```bash
    source .venv/bin/activate
    ```

### Part 3: Code and Submission
1.  **Write the Script:** Open the `main.py` file and add the following code:
    ```python
    import numpy as np
    def add_two_integer_lists(a: list[int], b: list[str]) -> int:
        arr=np.array(a)+np.array(b)
        print(f"My added array: {arr}")
    if __name__ == "__main__":
        add_two_integer_lists([1,2,3],[4,5,6])
    ```

2. **Note the Issues:** This code has multiple issues, namely.
    - Formatting and missing whitespaces
    - Incorrect typehints and return types
    - Missing docstrings
    - And so on... Try fixing them by yourself first.

3. **Linters and Code Formatters:** 

> [!TIP]
> To automatically format your code, run:
>   ```bash
>   uvx ruff format
>   ```

Do you see the difference?

Now, run this command and try to fix all issues:
```bash
uvx ruff check --select ALL --ignore T
```

Lastly, check if your types were correct:
```bash
uvx mypy .
```

4.  **Commit and Push:** After you think you have resolved all issues with this code, stage all your changes, commit, and push.
    ```bash
    git add .
    git commit -m "Complete project setup and add numpy script"
    git push origin main
    ```

5.  **Verify Checks:** Go to the "Actions" tab in your GitHub repository. Several workflows should be running. Wait for them to complete and ensure all checks pass with a green checkmark. If any checks fail, read the logs to debug the issue. The workflows verify code style, formatting, typing, and the exact version of NumPy. If all checks pass with a green mark, you have successfully completed this assignment.


