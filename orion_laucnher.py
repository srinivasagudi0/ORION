import runpy
import sys
from importlib.metadata import version


def main():
    if "--version" in sys.argv[1:]:
        print(f"ORION {version('orion-macos')}")
        return 0

    if "--help" in sys.argv[1:] or "-h" in sys.argv[1:]:
        print(
            "ORION — macOS automation assistant\n\n"
            "Run: orion\n"
            "Then type 'help' for available commands.\n\n"
            "AI features require your own OPENAI_API_KEY.\n"
            "Computer control requires macOS privacy permissions."
        )
        return 0

    if sys.platform != "darwin":
        print("ORION currently supports macOS only.", file=sys.stderr)
        return 1

    try:
        runpy.run_module("main", run_name="__main__")
    except (KeyboardInterrupt, EOFError):
        print("\nExiting ORION.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
