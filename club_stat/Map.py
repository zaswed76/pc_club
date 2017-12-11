#
# pro_zone_id = {"pc111254": {"data-id":"111253", "data-ip":"172.16.11.16", "data-mac":"9c:5c:8e:97:6d:e0",
#                             }
#
#

les_id_pro_zone = ["pc111254", "pc111253", "pc111252", "pc111251",
                   "pc111250", "pc111240"]

d = {
    "28.03.2017":
        {"les":
             {"map":
                  {"1": {"id": 121, "class": "off", "pro": True},
                   "2": {"id": 122, "class": "resid", "pro": True},
                   "3": {"id": 123, "class": "off", "pro": False}
                   },
              "stat" :
                  {"all": 25, "free": 5}

              }
         }
}

date = "28.03.2017"

def get_pro(db, date, club):
    res = {}
    for cl in db.values():
        print(cl)
        if cl == club:
            for k, line in cl["map"].items():

                if line["class"] != "off" and line["pro"]:
                    res[k] = line
    return res

print(get_pro(d, date, "les"))




