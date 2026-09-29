import sys
import urllib.request
import urllib.error

HEALTH_URL = "http://127.0.0.1:8000/health"


def check_health():
    try:
        response = urllib.request.urlopen(HEALTH_URL, timeout=5)

        if response.status == 200:
            print("HEALTHY: Application returned HTTP 200")
            return 0

        print(f"UNHEALTHY: Application returned HTTP {response.status}")
        return 1

    except urllib.error.URLError as error:
        print(f"UNHEALTHY: Could not reach application: {error}")
        return 1


if __name__ == "__main__":
    sys.exit(check_health())
