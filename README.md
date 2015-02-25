# Juju.fail

Sometimes CI breaks on Juju and when that happens no additional code can land.
Currently, you find out about this breakage by simply submitting code for a
fix then having the bot tell you that tree is blocked. This uses the same
code that Juju CI does in order to illuminate which branches are blocked and
by which bugs.

# Install

You will need to run this in the `bin` directory

    bzr branch lp:juju-ci-tools citools

Run `bzr pull` in `citools`

Place the following cron on the system as the web user:

```
*/5 * * * * /path/to/juju.fail/bin/blocked.py > /path/to/juju/fail/html/status.json
```

# Run

Put a web server in front of the html directory. For testing you can use the following:

```
python -m SimpleHTTPServer
```

from within the html directory.
