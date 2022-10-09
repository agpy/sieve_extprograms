# sieve_extprograms
Implemented a python script to send a notification with “from” and “subject” headers via telegram when specific sender from an address book has sent an email to a specific recipient. Used: Sieve filtering language with sieve_extprograms plugin.

For reference, here are the steps I followed to get this working:
1. create your script (ie. mail_telegram.py) in the /usr/lib/dovecot/sieve-execute/ directory.
2. ensure your script and target files have correct permissions: chmod +rx /usr/lib/dovecot/sieve-execute/mail_telegram.py
3. enable the sieve_extprograms plugin:
modify /etc/dovecot/conf.d/90-sieve.conf's plugin section with the following:
sieve_extensions = +vnd.dovecot.execute
sieve_plugins = sieve_extprograms
sieve_execute_bin_dir = /usr/lib/dovecot/sieve-execute
4. reload dovecot: systemctl restart dovecot
5. create sieve filter - mail_telegram.sieve (ie. in Roundcube goto settings -> filters -> actions -> edit filter set)
6. Now all mail delivered to any mailbox with this sieve filter will be piped through mail_telegram.py for action.
