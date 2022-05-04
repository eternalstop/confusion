# coding=utf-8
from asyncore import write
import io
import os
import pandas


read_excel_path = "./423.xlsx"
writer_excel_path = "./425.xlsx"

game_app_id_dict = {
    "agamesdk": ["阿里游戏国内sdk", "236"],
    "aoi": ["千年之旅", "116"],
    "armorgirls": ["机动战姬", "13"],
    "armorgirls-jp": ["机动战姬日版", "221"],
    "armorgirls-tw": ["机动战姬繁体","303"],
    "bd": ["BanG Dream!", "48"],
    "beatless": ["空匣人型", "2"],
    "bigfun": ["bigfun", "86"],
    "blmn": ["爆裂魔女", "266"],
    "bsywy3": ["宝石研物语3", "293"],
    "cabwg": ["长安百万贯", "198"],
    "craftman": ["工匠与旅人", "117"],
    "d100": ["梦100", "47"],
    "darkboom_jp": ["黑潮日服", "168"],
    "eu-figurestory": ["模型少女Awake全球", "274"],
    "excalibur": ["律响彼方", "103"],
    "fairysphere-jp": ["精灵之境日版", "146"],
    "fantasticdays": ["为美好的世界献上祝福！（素晴）", "149"],
    "figurestory": ["模型少女Awake繁体", "129"],
    "gamecenter-wiki": ["wiki", "80"],
    "gamesdk": ["idc国内sdk", "333"],
    "gzlj": ["公主连结", "12"],
    "hjzx": ["灰烬战线", "8"],
    "idolish7": ["idolish7", "6"],
    "jsz-jp": ["解神者:X2日服", "185"],
    "kdarkboom": ["黑潮繁体", "57"],
    "klight": ["光隙解语", "143"],
    "klight-tw": ["光隙解语繁体", "321"],
    "kr-figurestory": ["模型少女Awake韩版", "175"],
    "lapis": ["七千兆亿的星空", "118"],
    "lgmx-tw": ["来古弥新繁体", "267"],
    "mha-kr": ["我的英雄学院韩版", "162"],
    "mha-sea": ["我的英雄学院东南亚", "284"],
    "myr": ["古剑奇谭木语人", "10"],
    "na-figurestory": ["模型少女Awake全球", "274"],
    "nfl": ["诺弗兰物语", "126"],
    "nier-mys": ["尼尔马来西亚", "310"],
    "nier-tw": ["尼尔繁体", "217"],
    "nier-tw-dev-all": ["尼尔繁体", "217"],
    "ona": ["代号：黑街", "269"],
    "overlord": ["overlord", "92"],
    "planc": ["代号C计划", "81"],
    "qdwy": ["奇点物语", "192"],
    "quantummaki": ["终末阵线", "91"],
    "re0-kr": ["Re0韩版", "174"],
    "re0-sgp": ["Re0泰服", "194"],
    "re0-tw": ["Re0繁体", "171"],
    "sao": ["刀剑神域黑衣剑士：王牌", "119"],
    "sgp-figurestory": ["模型少女Awake全球", "274"],
    "sgsy": ["上古神域", "153"],
    "slb": ["腾讯云国内运维平台", "230"],
    "slsk": ["狩猎时刻", "120"],
    "snake": ["坎公骑冠剑", "19"],
    "sngj": ["少女歌剧", "106"],
    "starryplaza": ["星耀购物街", "99"],
    "taegis": ["机甲爱丽丝", "25"],
    "tdanceclub": ["梦想养成计划", "35"],
    "tgameops": ["腾讯云国内运维平台", "230"],
    "tgamesdk": ["腾讯云国内sdk", "229"],
    "thrud": ["斯露德", "156"],
    "time": ["拾光梦行", "30"],
    "udarkboom": ["黑潮繁体", "57"],
    "ugamesdk": ["ucloud台湾SDK", ""],
    "uma-tw": ["赛马娘（繁体）", "200"],
    "umha": ["赛马娘", "165"],
    "vita2": ["梦王国与不思议的寻梦少年", "179"],
    "wasteland-cn": ["拂晓的拾荒团", "135"],
    "wasteland-tw": ["拂晓的拾荒团繁体", "121"],
    "xtxo": ["箱庭小偶", "122"],
    "ydy": ["伊甸园的骄傲", "209"],
    "yjzs": ["悠久之树", "96"],
    "yqlxx": ["一起来修仙", "158"],
    "yxwj": ["一血万杰", "20"]
}


data = pandas.read_excel(io=read_excel_path, sheet_name="Sheet1")
nrows = data.shape[0]
ncols = data.shape[1]

writer = pandas.ExcelWriter(writer_excel_path)
data_frame = pandas.DataFrame(columns=("app_id", "业务名称", "业务ID"))

for row in range(0, nrows):
    service_tree = []
    row_data= []
    service_tree = data.iloc[row, 3]
    if service_tree.split(".")[0] == "game":
        game_app = service_tree.split(".")[1]
        row_data = game_app_id_dict[game_app]
        data_frame.loc[row + 1] = [service_tree] + row_data


data_frame.to_excel(writer, "Sheet1")
writer.save()