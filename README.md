# PC Uptime

It shows total uptime of my computer.

You can find working application [here](https://uptime-81p9.onrender.com/).

Application uses Flask and PostgreSQL.

Data is sent to the server by script:
```bash
#!/usr/bin/env bash

uptime=$(uptime | awk -F ' ' '{print $3}' | sed s/,//)
if echo "$uptime" | grep ':'; then
    hours=$(echo $uptime | awk -F ':' '{print $1}')
    minutes=$(echo $uptime | awk -F ':' '{print $2}')
    seconds=$(($hours * 3600 + $minutes * 60))
else
    seconds=$(($uptime * 60))
fi

curl -d "uptime=$seconds" -X POST https://uptime-81p9.onrender.com/update
```

Script is executed before shutdown or restart by systemd:

```
[Unit]
Description=Sends uptime data to server before shutdown/restart

[Service]
Type=oneshot
RemainAfterExit=true
WorkingDirectory=/home/dreamer20
ExecStop=/bin/bash /home/dreamer20/save_uptime.sh

[Install]
WantedBy=multi-user.target
```