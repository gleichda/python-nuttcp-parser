

class Parser():
    def __init__(self, nuttcp_string):
        self.nuttcp_string = nuttcp_string

    def parse(self):
        lines = self.nuttcp_string.splitlines()
        summary_split = lines[len(lines) - 1].split('=')
        transmit = summary_split[0].split('/')
        transmitted_MB = float(transmit[0].split()[0]) # output of NUTTCP is always in MB
        duration = transmit[1].split()
        rest = summary_split[1].split()
        speed = float(rest[0])
        tx = int(rest[2])
        rx = int(rest[4])
        retrans = int(rest[6])
        rtt = float(rest[8])
        result = NUTTCPResult()
        result.summary['transmitted_MB'] = transmitted_MB
        result.summary['duration'] = float(duration[0])
        result.summary['speed_Mbs'] = speed
        result.summary['RX'] = rx
        result.summary['TX'] = tx
        result.summary['retrans'] = retrans
        result.summary['RTT'] = rtt
        return result




class NUTTCPResult():
    def __init__(self):
        self.summary = dict.fromkeys(['duration', 'transmitted_MB', 'speed_Mbs', 'RX', 'TX', 'retrans', 'RTT'])
