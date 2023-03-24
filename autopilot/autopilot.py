import os
import sys
import subprocess
import time
import openai


def build_and_test():
    build_result = subprocess.run(["./build"], capture_output=True, text=True)
    if build_result.returncode != 0:
        return False, build_result.stderr

    test_result = subprocess.run(["./test"], capture_output=True, text=True)
    if test_result.returncode != 0:
        return False, test_result.stderr

    return True, None


def send_code_to_ai_api(code, error_output):
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise Exception("Environment variable OPENAI_API_KEY is not set")

    openai.api_key = api_key

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a code-fixing assistant."},
            {
                "role": "user",
                "content": f"""
Fix the following Python code:\n\n{code}\n\nError output:\n\n{error_output}.
Here is the fixed code ```python
""",
            },
        ],
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    fixed_code = response.choices[0].message["content"].strip()
    if "```" in fixed_code:
        fixed_code = fixed_code.partition("```")[0]
    return fixed_code


def commit_changes(code_file, error_output):
    subprocess.run(["git", "add", code_file], check=True)
    commit_message = (
        f"autopilot: Commit failed build or test - {code_file}\n\nError output:\n{error_output}"
    )
    subprocess.run(["git", "commit", "-m", commit_message], check=True)


def main():
    if len(sys.argv) != 2:
        print("Usage: autopilot <path_to_code_file>")
        sys.exit(1)
    code_file = sys.argv[1]

    while True:
        success, error_output = build_and_test()
        if success:
            print("Build and tests passed!")
            break

        print("Build or tests failed. Sending code and error output to AI API...")
        with open(code_file, "r") as file:
            code = file.read()

        try:
            fixed_code = send_code_to_ai_api(code, error_output)
            with open(code_file, "w") as file:
                file.write(fixed_code)
            print("AI API provided a fixed version of the code. Retrying build and tests...")

            commit_changes(code_file, error_output)
        except Exception as e:
            print(f"An error occurred while interacting with the AI API: {e}")
            break

        time.sleep(5)


if __name__ == "__main__":
    main()
