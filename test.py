# import json
import linux_metrics as lm
# import json

# from fastapi.responses import JSONResponse
# print(JSONResponse(lm.cpu_stat.cpu_times()).body)

import psutil

print((psutil.net_io_counters(pernic=True)['lo'][0]))

# def main():

#     # cpu
#     print('procs running: %d' % lm.cpu_stat.procs_running())
#     cpu_pcts = lm.cpu_stat.cpu_percents(sample_duration=1)
#     print('cpu utilization: %.2f%%' % (100 - cpu_pcts['idle']))

#     # disk
#     print('disk busy: %s%%' % lm.disk_stat.disk_busy('sda', sample_duration=1))
#     r, w = lm.disk_stat.disk_reads_writes('sda1')
#     print('disk reads: %s' % r)
#     print('disk writes: %s' % w)
#     print(f"disk usage {lm.disk_stat.disk_usage('/')}")

#     # memory
#     used, total, _, _, _, _ = lm.mem_stat.mem_stats()
#     print('mem used: %s' % used)
#     print('mem total: %s' % total)

#     # network
#     rx_bits, tx_bits = lm.net_stat.rx_tx_bits('enp4s0')
#     print('net bits received: %s' % rx_bits)
#     print('net bits sent: %s' % tx_bits)



# if __name__ == '__main__':
#     main()

