import json

tree_dict = {"department":"game","project":"sklr3","application":"desklr3-game-serverv","group":"prod","point":"servers"}
base_dict = {
    "action": "create_flow",
    "data": {
        "Game": "sao",
        "Env": "prod",
        "Resources": {
            "Instances": [],
            "Redis": [],
            "Database": [],
            "Listener": []
        },
        "Actions": {
            "bind_server":[]
        }
    }
}
instances_list = base_dict["data"]["Resources"]["Instances"]
redis_list = base_dict["data"]["Resources"]["Redis"]
mysql_list = base_dict["data"]["Resources"]["Database"]
listener_list = base_dict["data"]["Resources"]["Listener"]
bind_list = base_dict["data"]["Actions"]["bind_server"]

for i in range(12121, 12131):
    # instances_tmp = {
    #     "group_name": "instance-gs-s{}-group".format(i),
    #     "instance_name": "sao-tx-sh5-prod-s{}-gs".format(i),
    #     "instance_cpu": 16,
    #     "instance_memory": 64,
    #     "data_disk_size": 300,
    #     "service_tree": tree_dict,
    #     "extranet_on": "true",
    #     "count": 1
    # }
    # instances_list.append(instances_tmp)
    # redis_tmp = {
    #     "name": "sao-tx-sh5-prod-s{}-rd".format(i),
    #     "type": "master-slave",
    #     "version": "5.0",
    #     "memory": 8,
    #     "count": 1
    # }
    # redis_list.append(redis_tmp)
    # mysql_tmp = {
    #     "name": "sao-tx-sh5-prod-s{}-dbm".format(i),
    #     "disk_size": 300,
    #     "cpu": 4,
    #     "memory": 16,
    #     "type": "master-slave",
    #     "engine": "mysql",
    #     "version": "5.7",
    #     "count": 1
    # }
    # mysql_list.append(mysql_tmp)
    # listener_tmp = {
    #     "group_name":"s8-listener-{}".format(i),
    #     "slb_id":"bili-s8-slb",
    #     "listener_name":"tcp_{}".format(i),
    #     "protocol":"tcp",
    #     "port":i,
    #     "expire_time":0,
    #     "service_tree": tree_dict
    # }
    # listener_list.append(listener_tmp)
    bind_tmp = {
        "instance_group":"bili-s8-gs-group",
        "listener_group":"s8-listener-{}".format(i),
        "port":i,
        "weight":10
    }
    bind_list.append(bind_tmp)
    # break

# with open("prod-ob-gs-181-230.json", "w+") as fp:
#     fp.write(json.dumps(base_dict, indent=2))

with open("prod-ob-gs-181-230.json", "w+") as fp:
    fp.write(json.dumps(base_dict, indent=2))
# print(base_dict)


# test_dict = \
#     {
#         "action": "create_flow",
#         "data": {
#             "Game": "projectbp",
#             "Env": "prod",
#             "Resources": {
#                 "Instances": [
#                     {"group_name": "gs", "instance_name": "projectbp-tx-sh-prod-gs", "count": 8, "instance_cpu": 4,
#                      "instance_memory": 16, "data_disk_size": 200,
#                      "service_tree": {"department": "game", "project": "projectbp", "application": "game",
#                                       "group": "prod", "point": "servers"}, "extranet_on": "false"}],
#                 "Database": [{"disk_size": 200, "cpu": 4, "memory": 8, "type": "master-slave", "engine": "mysql",
#                               "version": "5.7", "count": 1, "name": "projectbp-tx-sh-prod-dbm"}],
#                 "Redis": [{"name": "projectbp-tx-sh-prod-rd", "type": "master-slave", "memory": 8, "count": 1,
#                            "version": "4.0"}],
#                 "Slb": [{"group_name": "gs-lb", "slb_name": "projectbp-tx-sh-prod-gs-lb", "network_mode": "public",
#                          "service_tree": {"department": "game", "project": "projectbp", "application": "game",
#                                           "group": "prod", "point": "servers"}}],
#                 "Cdns": [],
#                 "Listener": [
#                     {"group_name": "20001", "slb_id": "gs-lb", "listener_name": "listener_20001", "protocol": "tcp",
#                      "port": 20001, "expire_time": 0,
#                      "service_tree": {"department": "game", "project": "projectbp", "application": "game",
#                                       "group": "prod", "point": "servers"}},
#                     {"group_name": "20002", "slb_id": "gs-lb", "listener_name": "listener_20002", "protocol": "tcp",
#                      "port": 20002, "expire_time": 0,
#                      "service_tree": {"department": "game", "project": "projectbp", "application": "game",
#                                       "group": "prod", "point": "servers"}}],
#                 "General": []
#             },
#             "Actions": {
#                 "bind_server": [{"instance_group": "gs", "listener_group": "20001", "port": 20001, "weight": 10},
#                                 {"instance_group": "gs", "listener_group": "20002", "port": 20002, "weight": 10}]}
#         }
#     }
# with open("test.json", "w+") as fp:
#      fp.write(json.dumps(test_dict, indent=2))
