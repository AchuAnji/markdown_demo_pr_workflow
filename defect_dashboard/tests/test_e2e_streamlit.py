def test_streamlit_dashboard(page):
    # 1. Increase the timeout or wait for the app to load
    page.goto("http://localhost:8501", wait_until="networkidle")

    # 2. Specifically wait for the Streamlit app container
    page.wait_for_selector(".stApp", timeout=10000)

    # 3. Check for visibility
    assert page.locator(".stApp").is_visible()
