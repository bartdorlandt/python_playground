import logging
import os
import threading
from dataclasses import dataclass, field
from queue import Queue


@dataclass
class JiraFilter:
    filter: int
    name: str
    keys: list = field(default_factory=list)
    export_to_csv: bool = False


iterable_things = [
    JiraFilter(
        filter=22818,
        name="MI-INC",
        keys=[
            "INC",
            "Issue Key",
        ],
        export_to_csv=True,
    ),
]


def excepthook(args):
    print("\nError encountered. Terminating.\nError:", args.exc_value)
    os._exit(1)


def get_issues_fields(project, issue, connection):
    pass


def work_assigner(jobs_queue: Queue) -> None:
    """The `work_assigner` function is a worker thread that takes tasks from a queue and processes them by calling the `get_issues_fields` function.

    Args:
        jobs_queue (Queue): The jobs_queue parameter is a queue object that contains the tasks to be
    processed. Each task is a tuple containing the project, issue, and connection information.

    """
    while not jobs_queue.empty():
        project, issue, connection = jobs_queue.get()
        get_issues_fields(project, issue, connection)
        jobs_queue.task_done()


def get_issues(project, filter, connection):
    """Do things."""
    pass


def main():
    """_summary_."""
    # The excepthook takes care of any unhandled exceptions that occur in the threads.
    # Calling a function to define the necessary action.
    threading.excepthook = excepthook
    jira_connection = None
    threads = []
    workers = []
    projects = {}
    project_issues = {}
    total_threads = 5
    jobs: Queue = Queue()  # creating a queue object named `jobs` and assigning it the type `Queue`.

    for i in iterable_things:
        print(f"Retrieving project: {i.name}")
        thread = threading.Thread(target=get_issues, args=(i.name, i.filter, jira_connection))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    for project, issues in projects.items():  #  Calls function to modify the data in the project_issues dictionary.
        project_issues[project] = {}
        for issue in issues:
            # adding issues to queue
            jobs.put((project, issue, jira_connection))

    for _ in range(total_threads):
        worker = threading.Thread(target=work_assigner, args=(jobs,))
        worker.start()
        workers.append(worker)

    logging.info(f"waiting for queue to complete {jobs.qsize()} tasks")
    jobs.join()

    # Wait for all threads to complete
    for w in workers:
        w.join()
