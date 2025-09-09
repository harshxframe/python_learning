import json
import os
import threading
import time
import logging
from logging.handlers import RotatingFileHandler
from typing import List, Dict

CONFIG_PATH = "config.json"


def setup_logger(task_id: str, logfile="tasks.log") -> logging.Logger:
    logger = logging.getLogger(f"task-{task_id}")
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        handler = RotatingFileHandler(logfile, maxBytes=5_000_000, backupCount=3)
        formatter = logging.Formatter("%(asctime)s [%(name)s] %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        # also avoid propagation to root to prevent duplicate prints
        logger.propagate = False
    return logger


def main_task_logger(task_id: str, name: str, interval: float, stop_event: threading.Event):
    logger = setup_logger(task_id)
    logger.info(f"Started task '{name}' interval={interval}s")
    try:
        while not stop_event.is_set():
            # Do the actual work here. Replace with file writes, API calls, etc.
            logger.info(f"Task {task_id}: running '{name}'")
            # Wait but wake early if stop_event set
            stop_event.wait(interval)
    except Exception as e:
        logger.exception("Unhandled exception in task")
    finally:
        logger.info(f"Stopping task {task_id}")


def load_config(path: str) -> List[Dict]:
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    with open(path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in {path}: {e}") from e
    tasks = data.get("tasks")
    if not isinstance(tasks, list):
        raise ValueError("Config must contain a top-level 'tasks' list")
    # Basic validation
    validated = []
    for t in tasks:
        try:
            task_id = str(t["id"])
            name = str(t["name"])
            interval = float(t["interval_seconds"])
            if interval <= 0:
                raise ValueError("interval_seconds must be > 0")
            validated.append({"id": task_id, "name": name, "interval": interval})
        except Exception as e:
            raise ValueError(f"Invalid task entry: {t}. Error: {e}") from e
    return validated


def start_tasks(task_list: List[Dict]) -> List[threading.Event]:
    stop_events = []
    for t in task_list:
        stop = threading.Event()
        thread = threading.Thread(
            target=main_task_logger,
            args=(t["id"], t["name"], t["interval"], stop),
            daemon=True,
            name=f"task-thread-{t['id']}"
        )
        thread.start()
        stop_events.append(stop)
    return stop_events


def main():
    # Configure root logging to stdout so we see startup messages
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    try:
        tasks = load_config(CONFIG_PATH)
    except Exception as e:
        logging.exception("Failed to load config; exiting")
        return

    logging.info(f"Starting {len(tasks)} tasks")
    stops = start_tasks(tasks)

    try:
        # main thread can do other things; here we just sleep and let daemon threads run
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("Shutdown requested, signaling tasks to stop...")
        for s in stops:
            s.set()
        # give tasks a little time to finish
        time.sleep(1)
        logging.info("Exiting.")


if __name__ == "__main__":
    main()
