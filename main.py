import requests
import slackweb
import datetime
import json

latest_file_name = ''
history_file_name = ''
slack_url = ''

with open('config.json', 'r') as config:
    json_dict = json.load(config)
    latest_file_name = json_dict['files']['latest']
    history_file_name = json_dict['files']['history']
    slack_url = json_dict['slack']['url']

res = requests.get('http://inet-ip.info/ip')
ip = res.text

with open(history_file_name, mode='a') as history_file:
    history_file.write(datetime.datetime.now().isoformat() + ',' + ip + '\n')

with open(latest_file_name) as latest_file_r:
    ip_text = latest_file_r.read()

    if ip != ip_text:
        slack = slackweb.Slack(url=slack_url)
        slack.notify(text='old : ' + ip_text + '\nnew : ' + ip)

        with open(latest_file_name, mode='w') as latest_file_w:
            latest_file_w.write(ip)

