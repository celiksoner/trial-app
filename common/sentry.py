import sentry_sdk
from flask import Flask

sentry_sdk.init(
    dsn="https://c8e14adcb4626bf7a0e5bcefe295bf8c@o4507265623654400.ingest.de.sentry.io/4507265720189008",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

app = Flask(__name__)