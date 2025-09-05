import os
import pytest

# Create reports folder if not exists
os.makedirs("reports", exist_ok=True)

pytest.main([
    # "tests/test_login.py",
    "tests/test_inventory.py",
    "tests/test_order.py",
    "tests/test_logout.py",
    "--html=reports/report.html",
    "--self-contained-html"
])