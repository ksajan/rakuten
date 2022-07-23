# import json
import linux_metrics as lm
# import json

# from fastapi.responses import JSONResponse
# print(JSONResponse(lm.cpu_stat.cpu_times()).body)

import psutil

# print((psutil.net_io_counters(pernic=True)['lo'][0]))

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


# import pandas as pd
# import numpy as np
# # technologies= {
# #     'Courses':["Spark","PySpark","Hadoop","Python","Pandas"],
# #     'Fee' :[22000,25000,23000,24000,26000],
# #     'Duration':['30days','50days','30days', None,np.nan],
# #     'Discount':[1000,2300,1000,1200,2500]
# #           }
# # df = pd.DataFrame(technologies)
# # print(df)

# # # Query Rows using DataFrame.query()
# # df2=df.query("Courses == 'Spark'")
# # print(df2)
# # #Using variable
# # value='Spark'
# # df2=df.query("Courses == @value")
# # print(df2)
# # import requests
# # response = requests.request("GET", 'https://system-alert-and-monitoring.herokuapp.com/api/v1/system_metrics/cpu_stat/cpu_avg_load')
# # print(response.elapsed.total_seconds())
# df = pd.read_csv("https://rakhuten.s3.ap-south-1.amazonaws.com/data/data/csv_data/Apache/Apache_2k.log_structured.csv")
# print(df.head())

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='aravind.bhaskar@oureye.ai',
    to_emails='yuvaraj@oureye.ai',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    print(type(os.environ.get('SENDGRID_API_KEY')))
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)