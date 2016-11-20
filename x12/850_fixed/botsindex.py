import datetime

plugins = [
{'plugintype': 'routes', 'idroute': u'x12_850tofixed-ebcedic2fixed', 'seq': 9999, 'tochannel': u'fixed_out', 'frommessagetype': u'x12ebcedic', 'translateind': True, 'fromchannel': u'850_ebcdic_in', 'active': False, 'fromeditype': u'x12'},
{'plugintype': 'routes', 'idroute': u'x12-850tofixed', 'seq': 9999, 'tochannel': u'fixed_out', 'frommessagetype': u'x12', 'translateind': True, 'fromchannel': u'850_in', 'active': False, 'fromeditype': u'x12'},
{'plugintype': 'routes', 'idroute': u'x12-Fixedto850', 'seq': 9999, 'tochannel': u'x12_out', 'frommessagetype': u'ordersfixedsplit', 'translateind': True, 'fromchannel': u'fixed_in', 'active': False, 'fromeditype': u'fixed'},
{'starttls': False, 'ftpaccount': u'', 'syslock': False, 'askmdn': u'no', 'inorout': u'in', 'port': 0, 'parameters': u'', 'charset': u'us-ascii', 'filename': u'*.x12', 'secret': u'', 'apop': False, 'type': u'file', 'username': u'', 'idchannel': u'850_in', 'ftpactive': False, 'ftpbinary': True, 'host': u'', 'path': u'botssys/infile/x12_850tofixed/850', 'plugintype': 'channel', 'lockname': u'', 'remove': False, 'sendmdn': u'no'},
{'starttls': False, 'ftpaccount': u'', 'syslock': False, 'askmdn': u'no', 'inorout': u'in', 'port': 0, 'parameters': u'', 'charset': u'us-ascii', 'filename': u'*.fix', 'secret': u'', 'apop': False, 'type': u'file', 'username': u'', 'idchannel': u'fixed_in', 'ftpactive': False, 'ftpbinary': True, 'host': u'', 'path': u'botssys/infile/x12_850tofixed/fixed', 'plugintype': 'channel', 'lockname': u'', 'remove': False, 'sendmdn': u'no'},
{'starttls': False, 'ftpaccount': u'', 'syslock': False, 'askmdn': u'no', 'inorout': u'in', 'port': 0, 'parameters': u'', 'charset': u'cp500', 'filename': u'*.x12', 'secret': u'', 'apop': False, 'type': u'file', 'username': u'', 'idchannel': u'850_ebcdic_in', 'ftpactive': False, 'ftpbinary': True, 'host': u'', 'path': u'botssys/infile/x12_850tofixed/850ebcdic', 'plugintype': 'channel', 'lockname': u'', 'remove': False, 'sendmdn': u'no'},
{'starttls': False, 'ftpaccount': u'', 'syslock': True, 'askmdn': u'no', 'inorout': u'out', 'port': 0, 'parameters': u'', 'charset': u'iso-8859-1', 'filename': u'*.fix', 'secret': u'', 'apop': False, 'type': u'file', 'username': u'', 'idchannel': u'fixed_out', 'mdnchannel': u'', 'ftpactive': False, 'ftpbinary': True, 'host': u'', 'path': u'botssys/outfile/x12_850tofixed/fixed', 'plugintype': 'channel', 'lockname': u'', 'remove': True, 'sendmdn': u'no'},
{'starttls': False, 'ftpaccount': u'', 'syslock': True, 'askmdn': u'no', 'inorout': u'out', 'port': 0, 'parameters': u'', 'charset': u'us-ascii', 'filename': u'*.12', 'secret': u'', 'apop': False, 'type': u'file', 'username': u'', 'idchannel': u'x12_out', 'mdnchannel': u'', 'ftpactive': False, 'ftpbinary': True, 'host': u'', 'path': u'botssys/outfile/x12_850tofixed/x12', 'plugintype': 'channel', 'lockname': u'', 'remove': True, 'sendmdn': u'no'},
{'plugintype': 'translate', 'frommessagetype': u'850004010', 'toeditype': u'fixed', 'frompartner': u'', 'topartner': u'', 'active': True, 'alt': u'', 'fromeditype': u'x12', 'tscript': u'1101ordersx122fixed', 'tomessagetype': u'ordersfixedsplit'},
{'plugintype': 'translate', 'frommessagetype': u'850004010VICS', 'toeditype': u'fixed', 'frompartner': u'', 'topartner': u'', 'active': True, 'alt': u'', 'fromeditype': u'x12', 'tscript': u'1101ordersx122fixed', 'tomessagetype': u'ordersfixedsplit'},
{'plugintype': 'translate', 'frommessagetype': u'850004030', 'toeditype': u'fixed', 'frompartner': u'', 'topartner': u'', 'active': True, 'alt': u'', 'fromeditype': u'x12', 'tscript': u'1101ordersx122fixed', 'tomessagetype': u'ordersfixedsplit'},
{'plugintype': 'translate', 'frommessagetype': u'ordersfixedsplit', 'toeditype': u'x12', 'frompartner': u'', 'topartner': u'', 'active': True, 'alt': u'', 'fromeditype': u'fixed', 'tscript': u'1102ordersfixed2x12', 'tomessagetype': u'850004010'},
{'plugintype': 'translate', 'frommessagetype': u'850004030VICS', 'toeditype': u'fixed', 'frompartner': u'', 'topartner': u'', 'active': True, 'alt': u'', 'fromeditype': u'x12', 'tscript': u'1101ordersx122fixed', 'tomessagetype': u'ordersfixedsplit'},
]