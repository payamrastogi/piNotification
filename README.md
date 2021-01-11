

```
python3 -m pip install --user virtualenv
python3 -m venv tutorial-env
source tutorial-env/bin/activate
git update-index --assume-unchanged ./settings.yaml
```

/etc/proile.d/ssh_login.sh

if [ -n "$SSH_CLIENT" ]; then
    TEXT="$(date): ssh login to ${USER}@$(hostname -f)"
    TEXT="$TEXT from $(echo $SSH_CLIENT|awk '{print $1}')"
    source /home/payam/Workspace/piNotification/venv/bin/activate
    python3 /home/payam/Workspace/piNotification/pushNotification.py "Login Alert" "$TEXT"
fi



References:
- https://askubuntu.com/questions/1180713/pip-install-requirements-txt-command-returns-many-errors-including-404-not-fo
- https://iotdesignpro.com/projects/home-security-system-using-raspberry-pi-and-pir-sensor-with-push-notification-alert
- https://stackoverflow.com/questions/6964297/untrack-files-from-git-temporarily
- https://askubuntu.com/questions/179889/how-do-i-set-up-an-email-alert-when-a-ssh-login-is-successful