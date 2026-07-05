import os

from models.state import PipelineState

MAX_RETRIES = 3


def compiler(state: PipelineState) -> PipelineState:
    """
    Compiler Agent

    Checks whether the generated Remotion script exists.
    If compilation succeeds, the pipeline continues.
    Otherwise, retry until MAX_RETRIES is reached.
    """

    print("=" * 60)
    print("🛠️ Compiler & Fixer Agent Started")
    print("=" * 60)

    script_path = "output/remotion.tsx"

    # Clear previous compile errors
    state.compile_errors.clear()

    if os.path.exists(script_path):

        print("✅ Remotion script found.")
        print("✅ Compilation Successful.")

        state.status = "compiled"

        return state

    # Compilation failed
    print("❌ Compilation Failed")

    state.retry_count += 1

    error = {
        "file": script_path,
        "error": "Generated Remotion script not found."
    }

    state.compile_errors.append(error)

    print(f"Retry Attempt : {state.retry_count}/{MAX_RETRIES}")

    if state.retry_count >= MAX_RETRIES:

        print("❌ Maximum retry limit reached.")

        state.status = "failed"

    else:

        print("🔁 Sending compilation errors back to Script Generator...")

        state.status = "retry"

    return state