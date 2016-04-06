import string
import urllib.request

__author__ = 'weiqisong'

data_center = "hb"

info_template = string.Template("C:\doc\$dc.txt")

url = string.Template(
    "http://biz.jcloud.com/router?tenantId=$tenant_id&ip=$ip&routerId=$router_id&dataCenter=$dc&action=addRouterIp")

with  open(info_template.substitute(dc=data_center)) as f:
    for line in f:
        if line:
            datas = line.split(" ")
            i = 0
            for data in datas:
                if len(data.strip()) > 0:
                    i += 1
                else:
                    continue

                if i == 1:
                    tenant_id = data

                if i == 2:
                    route_id = data

                if i == 3:
                    ip = data

            # print(tenant_id + "," + route_id + "," + ip)
            requestUrl = url.substitute(tenant_id=tenant_id, router_id=route_id, ip=ip, dc=data_center)
            print(requestUrl)
            f = urllib.request.urlopen(requestUrl)
            print(f.read())
