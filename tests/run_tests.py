import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from test_mkd import (
    test_event,
    test_config,
    test_runtime,
    test_event_queue,
    test_error_handling,
    test_logger,
)


tests = [
    test_event,
    test_config,
    test_runtime,
    test_event_queue,
    test_error_handling,
    test_logger,
]


passed = 0

for test in tests:
    try:
        test()
        print(f"[PASS] {test.__name__}")
        passed += 1
    except Exception as error:
        print(f"[FAIL] {test.__name__}: {error}")

print()
print(f"MKD TESTS: {passed}/{len(tests)} passed")

if passed != len(tests):
    raise SystemExit(1)
