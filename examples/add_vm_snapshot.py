#!/usr/bin/python

#
# Copyright (c) 2016 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import logging

import ovirtsdk4 as sdk
import ovirtsdk4.types as types

logging.basicConfig(level=logging.DEBUG, filename='example.log')

# This example will connect to the server and add a snapshot to an
# existing virtual machine:

# Create the connection to the server:
connection = sdk.Connection(
  url='https://engine40.example.com/ovirt-engine/api',
  username='admin@internal',
  password='redhat123',
  ca_file='ca.pem',
  debug=True,
  log=logging.getLogger(),
)

# Locate the virtual machines service and use it to find the virtual
# machine:
vms_service = connection.system_service().vms_service()
vm = vms_service.list(search='name=myvm')[0]

# Locate the service that manages the snapshots of the virtual machine:
snapshots_service = vms_service.vm_service(vm.id).snapshots_service()

# Add the new snapshot:
snapshots_service.add(
  types.Snapshot(
    description='My snapshot',
  ),
)

# Close the connection to the server:
connection.close()
