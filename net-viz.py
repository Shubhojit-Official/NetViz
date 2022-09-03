import dpkt
import socket
import pygeoip
import os


gi = pygeoip.GeoIP('GeoLiteCity.dat')
PACKETS = './Packets'
def main():
    kml_content = ''
    kml_header = '<?xml version="1.0" encoding="UTF-8"?> \n<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document>\n'\
        '<Style id="transBluePoly">' \
                    '<LineStyle>' \
                    '<width>1.5</width>' \
                    '<color>501400E6</color>' \
                    '</LineStyle>' \
                    '</Style>'
    kml_footer ='</Document>\n</kml>\n'
    for filename in os.listdir(PACKETS):
        file = open(os.path.join(PACKETS,filename),'rb')
        pcap = dpkt.pcap.Reader(file)
        kml_content += map_IPs(pcap)
    kml_doc = kml_header + kml_content + kml_footer
    with open('IPs.kml','w+') as f:
        f.write(kml_doc)
    print(kml_doc)

def map_IPs(pcap):
    kml_pts = ''
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            KML = ret_kml(dst, src)
            kml_pts = kml_pts + KML
        except:
            pass
    return kml_pts

def ret_kml(dstip, srcip):
    dst = gi.record_by_name(dstip)
    src = gi.record_by_name('x.xxx.xxx.xxx')
    try:
        dst_longitude = dst['longitude']
        dst_latitude = dst['latitude']
        src_longitude = src['longitude']
        src_latitude = src['latitude']
        kml = (
            '<Placemark>\n'
            '<name>%s</name>\n'
            '<extrude>1</extrude>\n'
            '<tessellate>1</tessellate>\n'
            '<styleUrl>#transBluePoly</styleUrl>\n'
            '<LineString>\n'
            '<coordinates>%6f,%6f\n%6f,%6f</coordinates>\n'
            '</LineString>\n'
            '</Placemark>\n'
        )%(dstip, dst_longitude, dst_latitude, src_longitude, src_latitude)
        return kml
    except:
        return ''


if __name__ == "__main__":
    main()

