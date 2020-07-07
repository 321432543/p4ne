import flask
import re
import glob
import json

hosts = {}

app = flask.Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/page1')
def page1():
    a = []
    for i in hosts.keys():
        a.append(hosts[i]['name'])
    return flask.jsonify(a)

@app.route('/page2/<hostname>')
def page2(hostname):
    b = []
    for i in hosts.keys():
        if hosts[i]['name'] == hostname:
            b.append(hosts[i]['interfaces'])
            return flask.jsonify(hosts[i]['addresses'], b)


if __name__ == '__main__':
    folder = glob.glob("C:\Files\p4ne_training\config_files\*.txt")
    for current_file_name in folder:
        hosts[current_file_name] = {}
        hosts[current_file_name]['addresses'] = []
        hosts[current_file_name]['interfaces'] = []

        with open(current_file_name) as f:
            for l in f:
                host = re.match("hostname (.+)", l)
                if host:
                    hosts[current_file_name]['name'] = host.group(1)
                    continue
                ipaddr = re.match ("^ ip address ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}) ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})", l)
                if ipaddr:
                    hosts[current_file_name]['addresses'].append({'ip': ipaddr.group(1), 'mask': ipaddr.group(2)})
                    continue
                interface = re.match("interface (.+)", l)
                if interface:
                    hosts[current_file_name]['interfaces'].append({'interface': interface.group(1)})



    app.run(debug=True)

print(hosts)