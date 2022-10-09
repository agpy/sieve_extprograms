require ["body","fileinto","imap4flags","vnd.dovecot.execute","variables"];

# rule:[send_telegram_teamates]
if header :contains "x-addressbook" "teamates"
{
        execute :pipe "mail_telegram.py" "Teamates! ";
        fileinto "INBOX.0Teamates";
}
