#!/usr/bin/python
# -*- coding: UTF-8

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/. */

# Authors:
# Michael Berg-Mohnicke <michael.berg@zalf.de>
#
# Maintainers:
# Currently maintained by the authors.
#
# This file has been created at the Institute of
# Landscape Systems Analysis at the ZALF.
# Copyright (C: Leibniz Centre for Agricultural Landscape Research (ZALF)

import os
import sys
#print sys.path

import zmq
#print "pyzmq version: ", zmq.pyzmq_version(), " zmq version: ", zmq.zmq_version()

def main():
    "start n MONICAs on given server:port"

    config = {
        "user-id": os.environ.get("RPM_ZMQ_USER_USER_ID", ""),
        "n": "1",
        "server": "localhost",
        "port": "8888",
        "in-host": "localhost",
        #"in-fe-port": "6666",
        "in-be-port": "6677",
        "out-host": "localhost",
        "out-fe-port": "7788"#,
        #"out-be-port": "7777"
    }
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            k,v = arg.split("=")
            if k in config:
                config[k] = v 

    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://" + config["server"] + ":" + config["port"])

    msg = {
        "type": "start-new",
        "count": int(config["n"]),
        "control-addresses": "",
        "input-addresses": "tcp://" + config["in-host"] + ":" + config["in-be-port"] + config["user-id"],
        "output-addresses": "tcp://" + config["out-host"] + ":" + config["out-fe-port"] + config["user-id"]
    }
    print("sending:", msg)
    socket.send_json(msg)
    result = socket.recv_json()
    print("receiving:", result)

main()
