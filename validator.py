from validate_email import validate_email
import sys

RECHECK = 2
inp = sys.argv[1]
if __name__ == "__main__":
    invalid_mails = []
    with open(inp) as inp:
        cnt = 0
        for rec in inp:
            cnt += 1
            receiver = rec.strip()
            is_valid = validate_email(receiver, verify=True, smtp_timeout=1)
            if not is_valid:
                invalid_mails.append(receiver)
            else:
                print('#' + str(cnt) + ' ok')

    for i in range(RECHECK):
        # timeout=1s maybe not enough, so filter invalid address again
        for rec in invalid_mails:
            is_valid = validate_email(rec, verify=True, smtp_timeout=1)
            if is_valid:
                print('%s is ok' % rec)
                invalid_mails.remove(rec)
            else:
                print('%s is marked as invalid' % rec)

    print('------ RESULT ------')
    print('Invalid mails:')
    print('\n'.join(invalid_mails))
