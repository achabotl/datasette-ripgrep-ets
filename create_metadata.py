from datetime import datetime
import os
import pytz
from pytz import timezone

project_urls = {}

projects = os.listdir('all')
for project in projects:
    git_config = os.path.join('all', project, '.git', 'config')
    with open(git_config, encoding='utf-8') as f:
        for line in f:
            if line.strip().startswith('url'):
                url = line.split()[-1].rstrip('.git')
                project_urls[project] = url


metadata_template = """\
title: Search Enthought Tool Suite Source Code
about: achabotl/datasette-ripgrep-ets
about_url: https://github.com/achabotl/datasette-ripgrep-ets
description_html: |-
  <style>
  form.ripgrep label {
      font-weight: normal;
      display: inline;
  }
  </style>
  <form class="ripgrep" action="/-/ripgrep" method="get">
    <p>
        <input type="search" name="pattern" value="">
        <input type="submit" value="Search">
    </p>
    <p><strong>Options:</strong> <label><input type="checkbox" name="literal"> Literal search (not regex)</label> <label><input type="checkbox" name="ignore"> Ignore case</label></p>
    <p>
        <label><strong>File pattern</strong>: &nbsp;<input type="text" style="max-width: 20em" name="glob" value=""></label>
    </p>
    <p class="glob-examples">For example <code>*.py</code> or <code>**/templates/**/*.html</code> or <code>datasette/**</code> or </code><code>!setup.py</code>
    </p>
  </form>
  <p>%(updated)s</p>
  <ul class="bullets">
    %(project_links)s
  </ul>
plugins:
    datasette-ripgrep:
        path: /app/all
        time_limit: 5.0
"""

us_central = timezone('US/Central')
now = datetime.now(pytz.utc).astimezone(us_central)
fmt = '%Y-%m-%d %H:%M:%S %Z%z'
updated = f"The following projects were last indexed on {now.strftime(fmt)}:"

project_links = '\n'.join(
        f'  <li><a href="{url}">{project}</a></li>'
        for project, url in sorted(project_urls.items()))

metadata = metadata_template % {'updated': updated, 'project_links': project_links}


with open('./metadata.yml', 'w', encoding='utf-8') as f:
    f.write(metadata)
