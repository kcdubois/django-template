#!/usr/bin/env python

import sys
import os
import socket
import time
import subprocess


DB_SOCKET = (os.environ['DB_HOST'], int(os.environ['DB_PORT']))


def check_database_is_alive():
    while True:
        try:
            with socket.create_connection(DB_SOCKET, 1):
                print("Database connected.")
                return True
        except socket.timeout:
            print("Database unreachable, retrying...")
        except socket.gaierror:
            print("DNS name not found, retrying...")
            time.sleep(0.5)
        except ConnectionRefusedError:
            print("Connection refused, retrying...")
            time.sleep(0.5)
        except KeyboardInterrupt:
            raise


if __name__ == "__main__":
    try:
        check_database_is_alive()

        subprocess.run(["python", "manage.py", "makemigrations"])
        subprocess.run(["python", "manage.py", "migrate"])
        subprocess.run(sys.argv[1:])  # Run the exec

    except KeyboardInterrupt:
        print("Keyboard interrupt detectec, exiting...")
        sys.exit(1)