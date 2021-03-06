import os
import sys

# Django connector information.
import django

project_path = "."
sys.path.append(project_path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")
django.setup()
from django_scantron.models import ( # noqa
    Scan,
    ScheduledScan
)
