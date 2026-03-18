from dotenv import load_dotenv
import os
import sentry_sdk
import time

load_dotenv()

SENTRY_DSN = "https://25f297fe1d3410b54dd88565304607a5@o4511027157401600.ingest.us.sentry.io/4511027216515072"

sentry_sdk.init(
    dsn=SENTRY_DSN,
    send_default_pii=False,
    traces_sample_rate=0.0,
)


DATABASE_URL = os.getenv("DATABASE_URL")
TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL")