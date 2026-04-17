import argparse
import sys


__version__ = "1.0.0"


def serve(args):
    print("🚀 Starting Ollama server...")


def create(args):
    print(f"📦 Creating model: {args.name}")


def show(args):
    print(f"🔍 Showing model info: {args.name}")


def run(args):
    print(f"🏃 Running model: {args.name}")


def stop(args):
    print(f"🛑 Stopping model: {args.name}")


def pull(args):
    print(f"⬇️ Pulling model: {args.name}")


def push(args):
    print(f"⬆️ Pushing model: {args.name}")


def signin(args):
    print("🔐 Signing in...")


def signout(args):
    print("🚪 Signing out...")


def list_models(args):
    print("📚 Listing models...")


def ps(args):
    print("📊 Listing running models...")


def cp(args):
    print(f"📄 Copying model from {args.source} to {args.destination}")


def rm(args):
    print(f"❌ Removing model: {args.name}")


def launch(args):
    print("🚀 Launching Ollama UI...")


def main():
    parser = argparse.ArgumentParser(
        prog="ollama",
        description="Large Language Model Runner",
        usage="ollama <command> [options]",
        epilog="Example: python ollama_cli.py --help",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,  # auto shows defaults
        prefix_chars="-",  # allows - or -- (default)
        add_help=True,  # automatically adds -h/--help
        allow_abbrev=True  # allows shortened flags like --dis for --distance
    )

    # Global flags
    parser.add_argument("--nowordwrap", action="store_true", help="Don't wrap words")
    parser.add_argument("--verbose", action="store_true", help="Show timings")
    # Version flag
    parser.add_argument(
        "--version",
        "-v",
        action="version",
        version=f"client version is: {__version__}"
    )

    subparsers = parser.add_subparsers(dest="command")

    # serve
    subparsers.add_parser("serve", help="Start Ollama").set_defaults(func=serve)

    # create
    create_parser = subparsers.add_parser("create", help="Create a model")
    create_parser.add_argument("name")
    create_parser.set_defaults(func=create)

    # show
    show_parser = subparsers.add_parser("show", help="Show model info")
    show_parser.add_argument("name")
    show_parser.set_defaults(func=show)

    # run
    run_parser = subparsers.add_parser("run", help="Run a model")
    run_parser.add_argument("name")
    run_parser.set_defaults(func=run)

    # stop
    stop_parser = subparsers.add_parser("stop", help="Stop a model")
    stop_parser.add_argument("name")
    stop_parser.set_defaults(func=stop)

    # pull
    pull_parser = subparsers.add_parser("pull", help="Pull a model")
    pull_parser.add_argument("name")
    pull_parser.set_defaults(func=pull)

    # push
    push_parser = subparsers.add_parser("push", help="Push a model")
    push_parser.add_argument("name")
    push_parser.set_defaults(func=push)

    # signin
    subparsers.add_parser("signin", help="Sign in").set_defaults(func=signin)

    # signout
    subparsers.add_parser("signout", help="Sign out").set_defaults(func=signout)

    # list
    subparsers.add_parser("list", help="List models").set_defaults(func=list_models)

    # ps
    subparsers.add_parser("ps", help="List running models").set_defaults(func=ps)

    # cp
    cp_parser = subparsers.add_parser("cp", help="Copy a model")
    cp_parser.add_argument("source")
    cp_parser.add_argument("destination")
    cp_parser.set_defaults(func=cp)

    # rm
    rm_parser = subparsers.add_parser("rm", help="Remove a model")
    rm_parser.add_argument("name")
    rm_parser.set_defaults(func=rm)

    # launch
    subparsers.add_parser("launch", help="Launch UI").set_defaults(func=launch)

    args = parser.parse_args()

    # Handle version manually
    if args.version:
        print(f"client version is: {__version__}")
        sys.exit(0)

    # If no command
    if not hasattr(args, "func"):
        parser.print_help()
        sys.exit(1)

    # Execute command
    args.func(args)


if __name__ == "__main__":
    main()


# ollama <command> [args]

# Example usage:
# python ollama_cli.py serve
# uv run ollama_cli.py serve
# Output:
# 🚀 Starting Ollama server...

# python ollama_cli.py create mymodel
# Output:
# 📦 Creating model: mymodel

# uv ollama_cli.py --help
# uv run ollama_cli.py serve
# uv run ollama_cli.py create llama3
# uv run ollama_cli.py run llama3
# uv run ollama_cli.py pull mistral
# uv run ollama_cli.py cp llama3 llama3-backup
# uv run ollama_cli.py --version