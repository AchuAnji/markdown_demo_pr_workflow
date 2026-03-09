import subprocess
import time


def test_streamlit_dashboard(page):
    process = subprocess.Popen(["streamlit", "run", "app.py", "--server.port=8501"])

    # give streamlit time to start
    time.sleep(10)

    page.goto("http://localhost:8501", wait_until="networkidle")

    page.wait_for_selector(".stApp", timeout=10000)

    assert page.locator(".stApp").is_visible()

    process.terminate()
