import requests
import sys

# run this script with
# python <this-file>.py <email-list>.txt <mailgun-pubkey>

inp = sys.argv[1]
key = sys.argv[2]
invalid_addrs = []
if __name__ == "__main__":
    with open(inp) as f:
        for rec in f:
            recipient = rec.strip()
            res = requests.get("https://api.mailgun.net/v3/address/validate",
                               auth=("api", key),
                               params={"address": recipient})
            if (res.status_code != 200):
                print('status code: ' + str(res.status_code))
            else:
                res_dict = res.json()
                if (res_dict['is_valid']):
                    print('%s ok' % recipient)
                else:
                    invalid_addrs.append(recipient)

    print('Invalid address:')
    print(invalid_addrs)
