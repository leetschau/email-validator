import requests
import json
import sys

inp = sys.argv[1]
if __name__ == "__main__":
    with open(inp) as f:
        for rec in f:
            recipient = rec.strip()
            res = requests.get("https://api.mailgun.net/v3/address/validate",
                         auth=("api", "pubkey-1c54531f6fbe7e2dc3517a2112d167aa"),
                         params={"address": recipient})
            print(res)
            res_dic = json.loads(res.text)
            print(res_dic['is_valid'])
