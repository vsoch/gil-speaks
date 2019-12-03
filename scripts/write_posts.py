#!/usr/bin/env python

import os
import re
import yaml
from datetime import datetime

# Get script folder
repo_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_file = os.path.join(repo_base, "_data", "posts.yml")

if not os.path.exists(data_file):
    sys.exit("%s does not exist." % data_file)

with open(data_file, 'r') as filey:
    posts = yaml.safe_load(filey)

# Iterate over timestamps and post content
for ts, post in posts['posts'].items():

    # Convert timestmap to proper datetime
    dt_object = datetime.fromtimestamp(ts)
    filename_dt = dt_object.strftime("%Y-%m-%d")

    # Write the post (come up with title later)
    words = "-".join(post.split(" ")[0:3]).lower()
    words = re.sub('[^0-9a-zA-Z-]+', '', words).replace('--','-')
    post_file = os.path.join(repo_base, "_posts", "%s-%s.md" %(filename_dt, words))
    title = " ".join([x.capitalize() for x in words.replace("-"," ").split(" ")])
    content = '''
---
layout: post
title: "%s"
author: "@vsoch"
categories: wisdom
---

%s
''' %(title, post)

    # Write to file
    if not os.path.exists(post_file):
        with open(post_file, 'w') as filey:
            filey.write(content)
