from flask import Flask

import socket
import random
import argparse
import requests
import logging
from dataclasses import dataclass

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


@dataclass
class Host:
    def __init__(self, ip: str, port: int):
        self.ip = ip
        self.port = port
        self.url = "{0}:{1}".format(self.ip, self.port)

    def isAlive(self):
        try:
            socket.create_connection((self.ip , self.port), timeout=1)
            return True
        except:
            return False

@dataclass
class Service:
    name: str
    httpContext: str
    hosts: list
    schema: str = "http"

    """
    def __init__(self, name: str, httpContext: str, hosts: list, schema: str = "http"):
        self.name = name
        self.hosts = hosts
        self.httpContext = httpContext
        self.schema = schema
    """

    def add_host(self, host: Host):
        self.hosts.append(host)

    def host_is_alive(self):
        ret = []
        for host in self.hosts:
            if host.isAlive():
                ret.append(host)
        return ret

    def get_random_host(self):
        hostAlive = self.host_is_alive()
        return hostAlive[random.randint(0, len(self.host_is_alive()) - 1)]


app = Flask(__name__)

@app.route("/carrello")
def get_carrello():
    logger.debug("connecting to backend services")
    host = carrello.get_random_host()
    logger.debug("backend host: --> %s" % str(host))
    url = "%s://%s/%s" % ( carrello.schema, host.url, carrello.httpContext )
    res = requests.get(url)
    return res.text, res.status_code
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true", dest='debug', default=False)
    parser.add_argument("--host", dest="host", default="0.0.0.0")
    parser.add_argument("--port", dest="port", default=5000)
    ar = parser.parse_args()
    
    carrello = Service("carrello", "/carrello", [
        Host("192.168.1.2", 80),
        Host("192.168.1.3", 80)
    ])

    app.run(host=ar.host, port=int(ar.port), debug=ar.debug)
