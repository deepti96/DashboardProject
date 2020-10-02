result= `systemctl --type=service --state=active | awk '{print $1}'| tail -2 | head -1`
