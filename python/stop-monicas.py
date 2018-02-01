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
    "stop n MONICAs on given server:port"

    config = {
        "user-id": os.environ.get("RPM_ZMQ_USER_USER_ID", ""),
        "server": "localhost",
        "port": "6666",
        "n": "1"
    }
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            k,v = arg.split("=")
            if k in config:
                config[k] = v 

    context = zmq.Context()
    socket = context.socket(zmq.PUSH)
    socket.connect("tcp://" + config["server"] + ":" + config["port"] + config["user-id"])

    for n in range(int(config["n"])):
        socket.send_json({"type": "finish"})
        print n+1,

main()
