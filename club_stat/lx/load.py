
import pandas as pd

line = """class="comp bg_off" data-id="111253" data-ip="172.16.11.16" data-mac="9c:5c:8e:97:6d:e0" data-unauth="" id="pc111253" title="">16<"""

data = pd.read_html(line)
print(data)