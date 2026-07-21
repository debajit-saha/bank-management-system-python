from pathlib import Path
from datetime import datetime
from functools import wraps
import json


LOG_DIR = Path(__file__).parent / "logs"
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "queries.json"


def log_query(log_args=True, log_result=False):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            log = {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "method": func.__name__,
                "status": "Success"
            }

            if log_args:
                log["args"] = list(args)
                log["kwargs"] = kwargs

            try:
                result = func(*args, **kwargs)

                if log_result:
                    log["result"] = result

                return result

            except Exception as ex:
                log["status"] = "Failed"
                log["error"] = str(ex)
                raise

            finally:
                with open(LOG_FILE, "a", encoding="utf-8") as file:
                    json.dump(
                        log, file, default=lambda obj: obj.__dict__, indent=4)
                    file.write("\n")

        return wrapper

    return decorator
