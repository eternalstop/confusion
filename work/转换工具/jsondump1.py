import json
data=[]
fu_txt=open("fu.txt","r").readlines()
zi_txt=open("zi.txt","r").readlines()
for i in fu_txt:
	fu_line=i.split("\t")
	seq=fu_line[0]
	name=fu_line[2].decode("gbk")
	imgUrl=fu_line[4]
	mediaCode=fu_line[5].replace("\n","")
	childInfo=[]
	for j in zi_txt:
		zi_line=j.split("\t")
		if zi_line[0]==seq:
			childInfo.append({"mediaCode":zi_line[6].replace("\n","")})
	data.append({"channel":2,
			"imgUrl":imgUrl,
			"name":name,
			"mediaCode":mediaCode,
			"childInfo":childInfo})
result=json.dumps({"data":data},indent=2)

open("list.json","w").writelines(result)
