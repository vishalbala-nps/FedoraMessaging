
from fedora_messaging.api import publish, Message
from fedora_messaging.config import conf
import sys

msg = sys.argv[1]
conf.setup_logging()
message = Message(
    topic="tq1",
    body={"reason": msg}
)
publish(message)
