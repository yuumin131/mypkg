# SPDX-FileCopyrightText: 2025 Yuuma Sakurai
# SPDX-License-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import requests
from bs4 import BeautifulSoup


class PressurePublisher(Node):
    def __init__(self):
        super().__init__('pressure_publisher')
        self.publisher_ = self.create_publisher(String, 'chiba_pressure', 10)
        self.timer = self.create_timer(1.0, self.publish_pressure)

    def publish_pressure(self):

        url = "https://www.data.jma.go.jp/stats/data/mdrr/synopday/data1s.html"

        res = requests.get(url)
        res.encoding = res.apparent_encoding

        soup = BeautifulSoup(res.text, "html.parser")

        #print (soup)

        elems = soup.find_all("tr")
        #print(elems[58].contents[3])
        #print(elems[58].contents[0])
        pressure_html = str(elems[58].contents[3])
        pref_html = str(elems[58].contents[0])



        pressure_data = pressure_html[:pressure_html.find("</td>")]
        pressure_data = pressure_data[pressure_data.find(">") + 1:]
        pref = pref_html[:pref_html.find("</td>")]
        pref = pref[pref_html.find(">") + 1:]
        pressure_data = pressure_data.replace(']', '')
        pressure_data = pressure_data.replace(')', '')
        pressure_data = pressure_data.replace('#', '')
        pressure_data = pressure_data.replace('*', '')
        pressure_data = pressure_data.replace('@', '')
        #print(pressure)
        #print(pref)

        #pressure = random.uniform(950.0, 1050.0)

        pressure = f"{pref}の気圧は{pressure_data}"

        msg = String()
        msg.data = pressure
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = PressurePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

