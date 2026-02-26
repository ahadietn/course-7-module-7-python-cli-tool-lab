# cli_tool.py

import argparse
from lib.models import Task, User

# Global dictionary to store users and their tasks
users = {}

def add_task(args):
    # Get existing user or create a new one
    if args.user not in users:
        users[args.user] = User(args.user)
    user = users[args.user]

    # Create and add the task
    task = Task(args.title)
    user.add_task(task)

def complete_task(args):
    # Look up the user
    user = users.get(args.user)
    if not user:
        print(f"User '{args.user}' not found.")
        return

    # Look up the task using the model's method
    task = user.get_task_by_title(args.title)
    if not task:
        print(f"Task '{args.title}' not found for user '{args.user}'.")
        return

    # Mark the task as complete
    task.complete()

# CLI entry point
def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers()

    # Subparser for adding tasks
    add_parser = subparsers.add_parser("add-task", help="Add a task for a user")
    add_parser.add_argument("user")
    add_parser.add_argument("title")
    add_parser.set_defaults(func=add_task)

    # Subparser for completing tasks
    complete_parser = subparsers.add_parser("complete-task", help="Complete a user's task")
    complete_parser.add_argument("user")
    complete_parser.add_argument("title")
    complete_parser.set_defaults(func=complete_task)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
