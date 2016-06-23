from validate_email import validate_email
import DNS
import sys

DNS.defaults['server'] = ['8.8.8.8', '8.8.4.4']
RECHECK = 2

inp = sys.argv[1]
if __name__ == "__main__":
    invalid_mails = []
    with open(inp) as inp:
        for rec in inp:
            receiver = rec.strip()
            is_valid = validate_email(receiver, verify=True, smtp_timeout=5)
            if not is_valid:
                invalid_mails.append(receiver)
            else:
                print('%s ok' % receiver)

    for i in range(RECHECK):
        print('\nRecheck Round %d:\n' % (i + 1))
        # timeout=1s maybe not enough, so filter invalid address again
        for rec in invalid_mails:
            is_valid = validate_email(rec, verify=True, smtp_timeout=1)
            if is_valid:
                print('%s ok' % rec)
                invalid_mails.remove(rec)
            else:
                print('%s marked as invalid' % rec)

    print('\n------ Invalid Addresses ------\n')
    print('\n'.join(invalid_mails))
