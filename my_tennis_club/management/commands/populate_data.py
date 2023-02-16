import json
import sys
import logging
from dateutil import parser
from django.core.management.base import BaseCommand

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = "Populating User data obtained in JSON from Monolith."

    def handle(self, *args, **options):
        for line in sys.stdin:
            data = json.loads(line)

            # Populating User Model
            if data["model"] == "User":
                user= User(
                    user_id=data["id"],
                    username=data["username"],
                    mobile_number=data["mobile_number"],
                    created_at=parser.parse(data["created_at"]),
                )
                user.save()
                logger.debug("User populated:{}".format(user.user_id))