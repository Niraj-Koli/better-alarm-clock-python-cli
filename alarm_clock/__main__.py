"""Allow ``python -m alarm_clock``."""

import sys

from .cli import main

sys.exit(main())
