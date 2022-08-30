#!/usr/bin/env python
import subprocess
import sys
from datetime import datetime

branch = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"]).strip()
revision = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"]).strip()
unclean = "*" if len(subprocess.check_output(["git", "status", "--porcelain"]).strip()) > 0 else ""
date = datetime.now().replace(microsecond=0)
print("%s -DDETAILED_BUILD_VERSION='\"%s-%s%s\"' -DSTRING_DISTRIBUTION_DATE='\"%s\"'" % (" ".join(sys.argv[1:]), branch, unclean, revision, date.isoformat()))
