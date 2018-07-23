#!/usr/local/python/bin/python
# coding=utf-8
import json

# dic2 = {'data': [{'mediacode': '4843793', 'childInfo': [{'mediacode': '4856647'}, {'mediacode': '4856660'}, {'mediacode': '4856658'}, {'mediacode': '4856656'}, {'mediacode': '4856652'}, {'mediacode': '4856654'}, {'mediacode': '4856663'}, {'mediacode': '4856662'}, {'mediacode': '4856649'}, {'mediacode': '4856648'}, {'mediacode': '4856661'}, {'mediacode': '4856657'}, {'mediacode': '4856650'}, {'mediacode': '4856659'}, {'mediacode': '4856655'}, {'mediacode': '4856651'}, {'mediacode': '4856653'}], 'imgUrl': 'pic4238851.jpg', 'channel': 2, 'name': '幼儿学拼音'}, {'mediacode': '4844595', 'childInfo': [{'mediacode': '4856776'}, {'mediacode': '4856834'}, {'mediacode': '4856743'}, {'mediacode': '4856734'}, {'mediacode': '4856774'}, {'mediacode': '4856685'}, {'mediacode': '4856714'}, {'mediacode': '4856781'}, {'mediacode': '4856741'}, {'mediacode': '4856829'}, {'mediacode': '4856844'}, {'mediacode': '4856827'}, {'mediacode': '4856695'}, {'mediacode': '4856803'}, {'mediacode': '4856706'}, {'mediacode': '4856736'}, {'mediacode': '4856704'}, {'mediacode': '4856836'}, {'mediacode': '4856726'}, {'mediacode': '4856710'}, {'mediacode': '4856749'}, {'mediacode': '4856709'}, {'mediacode': '4856800'}, {'mediacode': '4856751'}, {'mediacode': '4856731'}, {'mediacode': '4856830'}, {'mediacode': '4856775'}, {'mediacode': '4856795'}, {'mediacode': '4856841'}, {'mediacode': '4856692'}, {'mediacode': '4856801'}, {'mediacode': '4856824'}, {'mediacode': '4856821'}, {'mediacode': '4856727'}, {'mediacode': '4856819'}, {'mediacode': '4856673'}, {'mediacode': '4856822'}, {'mediacode': '4856838'}, {'mediacode': '4856682'}, {'mediacode': '4856784'}, {'mediacode': '4856742'}, {'mediacode': '4856791'}, {'mediacode': '4856808'}, {'mediacode': '4856810'}, {'mediacode': '4856729'}, {'mediacode': '4856813'}, {'mediacode': '4856779'}, {'mediacode': '4856723'}, {'mediacode': '4856691'}, {'mediacode': '4856707'}, {'mediacode': '4856696'}, {'mediacode': '4856728'}, {'mediacode': '4856794'}, {'mediacode': '4856670'}, {'mediacode': '4856690'}, {'mediacode': '4856667'}, {'mediacode': '4856669'}, {'mediacode': '4856765'}, {'mediacode': '4856772'}, {'mediacode': '4856832'}, {'mediacode': '4856740'}, {'mediacode': '4856746'}, {'mediacode': '4856680'}, {'mediacode': '4856757'}, {'mediacode': '4856753'}, {'mediacode': '4856807'}, {'mediacode': '4856752'}, {'mediacode': '4856837'}, {'mediacode': '4856722'}, {'mediacode': '4856716'}, {'mediacode': '4856748'}, {'mediacode': '4856798'}, {'mediacode': '4856846'}, {'mediacode': '4856853'}, {'mediacode': '4856758'}, {'mediacode': '4856849'}, {'mediacode': '4856790'}, {'mediacode': '4856789'}, {'mediacode': '4856806'}, {'mediacode': '4856681'}, {'mediacode': '4856826'}, {'mediacode': '4856799'}, {'mediacode': '4856851'}, {'mediacode': '4856750'}, {'mediacode': '4856688'}, {'mediacode': '4856817'}, {'mediacode': '4856672'}, {'mediacode': '4856694'}, {'mediacode': '4856664'}, {'mediacode': '4856676'}, {'mediacode': '4856747'}, {'mediacode': '4856835'}, {'mediacode': '4856845'}, {'mediacode': '4856767'}, {'mediacode': '4856785'}, {'mediacode': '4856850'}, {'mediacode': '4856712'}, {'mediacode': '4856677'}, {'mediacode': '4856777'}, {'mediacode': '4856843'}, {'mediacode': '4856678'}, {'mediacode': '4856793'}, {'mediacode': '4856724'}, {'mediacode': '4856839'}, {'mediacode': '4856802'}, {'mediacode': '4856679'}, {'mediacode': '4856778'}, {'mediacode': '4856763'}, {'mediacode': '4856668'}, {'mediacode': '4856768'}, {'mediacode': '4856698'}, {'mediacode': '4856783'}, {'mediacode': '4856771'}, {'mediacode': '4856842'}, {'mediacode': '4856809'}, {'mediacode': '4856744'}, {'mediacode': '4856705'}, {'mediacode': '4856732'}, {'mediacode': '4856825'}, {'mediacode': '4856812'}, {'mediacode': '4856703'}, {'mediacode': '4856769'}, {'mediacode': '4856715'}, {'mediacode': '4856815'}, {'mediacode': '4856730'}, {'mediacode': '4856816'}, {'mediacode': '4856684'}, {'mediacode': '4856713'}, {'mediacode': '4856828'}, {'mediacode': '4856733'}, {'mediacode': '4856665'}, {'mediacode': '4856683'}, {'mediacode': '4856687'}, {'mediacode': '4856759'}, {'mediacode': '4856671'}, {'mediacode': '4856818'}, {'mediacode': '4856811'}, {'mediacode': '4856693'}, {'mediacode': '4856761'}, {'mediacode': '4856735'}, {'mediacode': '4856755'}, {'mediacode': '4856717'}, {'mediacode': '4856699'}, {'mediacode': '4856780'}, {'mediacode': '4856708'}, {'mediacode': '4856814'}, {'mediacode': '4856833'}, {'mediacode': '4856847'}, {'mediacode': '4856702'}, {'mediacode': '4856718'}, {'mediacode': '4856745'}, {'mediacode': '4856786'}, {'mediacode': '4856852'}, {'mediacode': '4856840'}, {'mediacode': '4856700'}, {'mediacode': '4856762'}, {'mediacode': '4856711'}, {'mediacode': '4856738'}, {'mediacode': '4856823'}, {'mediacode': '4856797'}, {'mediacode': '4856756'}, {'mediacode': '4856725'}, {'mediacode': '4856737'}, {'mediacode': '4856848'}, {'mediacode': '4856787'}, {'mediacode': '4856788'}, {'mediacode': '4856754'}, {'mediacode': '4856831'}, {'mediacode': '4856804'}, {'mediacode': '4856666'}, {'mediacode': '4856739'}, {'mediacode': '4856720'}, {'mediacode': '4856782'}, {'mediacode': '4856689'}, {'mediacode': '4856770'}, {'mediacode': '4856760'}, {'mediacode': '4856697'}, {'mediacode': '4856686'}, {'mediacode': '4856766'}, {'mediacode': '4856674'}, {'mediacode': '4856792'}, {'mediacode': '4856719'}, {'mediacode': '4856820'}, {'mediacode': '4856721'}, {'mediacode': '4856701'}, {'mediacode': '4856796'}, {'mediacode': '4856805'}, {'mediacode': '4856675'}, {'mediacode': '4856773'}], 'imgUrl': 'pic4238855.jpg', 'channel': 2, 'name': '幼教数学篇'}, {'mediacode': '4848075', 'childInfo': [{'mediacode': '4856912'}, {'mediacode': '4856984'}, {'mediacode': '4856985'}, {'mediacode': '4856915'}, {'mediacode': '4856931'}, {'mediacode': '4856903'}, {'mediacode': '4856861'}, {'mediacode': '4856909'}, {'mediacode': '4856949'}, {'mediacode': '4856895'}, {'mediacode': '4856936'}, {'mediacode': '4856952'}, {'mediacode': '4856940'}, {'mediacode': '4856875'}, {'mediacode': '4857001'}, {'mediacode': '4856894'}, {'mediacode': '4856874'}, {'mediacode': '4857015'}, {'mediacode': '4856901'}, {'mediacode': '4856978'}, {'mediacode': '4856866'}, {'mediacode': '4856884'}, {'mediacode': '4856880'}, {'mediacode': '4856930'}, {'mediacode': '4856950'}, {'mediacode': '4856980'}, {'mediacode': '4856988'}, {'mediacode': '4856917'}, {'mediacode': '4856928'}, {'mediacode': '4856990'}, {'mediacode': '4856891'}, {'mediacode': '4856951'}, {'mediacode': '4856957'}, {'mediacode': '4856994'}, {'mediacode': '4856971'}, {'mediacode': '4856918'}, {'mediacode': '4856899'}, {'mediacode': '4856878'}, {'mediacode': '4856938'}, {'mediacode': '4856943'}, {'mediacode': '4856863'}, {'mediacode': '4856902'}, {'mediacode': '4856962'}, {'mediacode': '4856855'}, {'mediacode': '4856904'}, {'mediacode': '4856898'}, {'mediacode': '4856905'}, {'mediacode': '4856910'}, {'mediacode': '4856868'}, {'mediacode': '4856982'}, {'mediacode': '4856929'}, {'mediacode': '4856983'}, {'mediacode': '4856993'}, {'mediacode': '4856864'}, {'mediacode': '4856859'}, {'mediacode': '4856888'}, {'mediacode': '4856907'}, {'mediacode': '4856968'}, {'mediacode': '4856886'}, {'mediacode': '4857014'}, {'mediacode': '4856879'}, {'mediacode': '4857011'}, {'mediacode': '4856948'}, {'mediacode': '4856997'}, {'mediacode': '4856876'}, {'mediacode': '4856958'}, {'mediacode': '4856883'}, {'mediacode': '4856947'}, {'mediacode': '4856860'}, {'mediacode': '4856935'}, {'mediacode': '4856914'}, {'mediacode': '4856932'}, {'mediacode': '4856961'}, {'mediacode': '4856869'}, {'mediacode': '4856973'}, {'mediacode': '4857005'}, {'mediacode': '4856959'}, {'mediacode': '4856867'}, {'mediacode': '4856987'}, {'mediacode': '4856873'}, {'mediacode': '4857013'}, {'mediacode': '4856989'}, {'mediacode': '4856969'}, {'mediacode': '4856877'}, {'mediacode': '4856970'}, {'mediacode': '4856916'}, {'mediacode': '4856856'}, {'mediacode': '4856923'}, {'mediacode': '4856858'}, {'mediacode': '4856890'}, {'mediacode': '4856939'}, {'mediacode': '4856927'}, {'mediacode': '4857000'}, {'mediacode': '4856871'}, {'mediacode': '4857008'}, {'mediacode': '4856967'}, {'mediacode': '4856996'}, {'mediacode': '4856942'}, {'mediacode': '4856963'}, {'mediacode': '4856906'}, {'mediacode': '4857009'}, {'mediacode': '4857010'}, {'mediacode': '4856862'}, {'mediacode': '4857016'}, {'mediacode': '4856976'}, {'mediacode': '4856887'}, {'mediacode': '4856892'}, {'mediacode': '4856897'}, {'mediacode': '4856920'}, {'mediacode': '4856946'}, {'mediacode': '4856889'}, {'mediacode': '4856924'}, {'mediacode': '4856944'}, {'mediacode': '4856964'}, {'mediacode': '4856981'}, {'mediacode': '4856960'}, {'mediacode': '4856937'}, {'mediacode': '4856881'}, {'mediacode': '4856872'}, {'mediacode': '4856965'}, {'mediacode': '4856998'}, {'mediacode': '4856870'}, {'mediacode': '4856900'}, {'mediacode': '4856925'}, {'mediacode': '4856966'}, {'mediacode': '4856908'}, {'mediacode': '4856926'}, {'mediacode': '4856977'}, {'mediacode': '4856945'}, {'mediacode': '4856954'}, {'mediacode': '4856919'}, {'mediacode': '4857003'}, {'mediacode': '4857018'}, {'mediacode': '4857002'}, {'mediacode': '4856941'}, {'mediacode': '4857006'}, {'mediacode': '4856921'}, {'mediacode': '4856986'}, {'mediacode': '4856975'}, {'mediacode': '4857004'}, {'mediacode': '4857007'}, {'mediacode': '4856896'}, {'mediacode': '4856913'}, {'mediacode': '4856995'}, {'mediacode': '4856922'}, {'mediacode': '4856953'}, {'mediacode': '4856991'}, {'mediacode': '4856882'}, {'mediacode': '4856857'}, {'mediacode': '4856979'}, {'mediacode': '4856974'}, {'mediacode': '4856999'}, {'mediacode': '4856885'}, {'mediacode': '4857017'}, {'mediacode': '4856992'}, {'mediacode': '4856865'}, {'mediacode': '4856933'}, {'mediacode': '4856893'}, {'mediacode': '4856972'}, {'mediacode': '4856956'}, {'mediacode': '4856955'}, {'mediacode': '4857012'}, {'mediacode': '4856911'}, {'mediacode': '4856934'}], 'imgUrl': 'pic4238859.jpg', 'channel': 2, 'name': '幼教英语篇'}, {'mediacode': '4849418', 'childInfo': [{'mediacode': '4857171'}, {'mediacode': '4857199'}, {'mediacode': '4857177'}, {'mediacode': '4857149'}, {'mediacode': '4857165'}, {'mediacode': '4857131'}, {'mediacode': '4857117'}, {'mediacode': '4857204'}, {'mediacode': '4857146'}, {'mediacode': '4857056'}, {'mediacode': '4857150'}, {'mediacode': '4857090'}, {'mediacode': '4857070'}, {'mediacode': '4857069'}, {'mediacode': '4857212'}, {'mediacode': '4857135'}, {'mediacode': '4857042'}, {'mediacode': '4857167'}, {'mediacode': '4857033'}, {'mediacode': '4857065'}, {'mediacode': '4857180'}, {'mediacode': '4857045'}, {'mediacode': '4857181'}, {'mediacode': '4857041'}, {'mediacode': '4857074'}, {'mediacode': '4857229'}, {'mediacode': '4857141'}, {'mediacode': '4857049'}, {'mediacode': '4857096'}, {'mediacode': '4857227'}, {'mediacode': '4857071'}, {'mediacode': '4857214'}, {'mediacode': '4857126'}, {'mediacode': '4857220'}, {'mediacode': '4857119'}, {'mediacode': '4857144'}, {'mediacode': '4857209'}, {'mediacode': '4857195'}, {'mediacode': '4857050'}, {'mediacode': '4857091'}, {'mediacode': '4857189'}, {'mediacode': '4857161'}, {'mediacode': '4857072'}, {'mediacode': '4857201'}, {'mediacode': '4857093'}, {'mediacode': '4857147'}, {'mediacode': '4857172'}, {'mediacode': '4857111'}, {'mediacode': '4857063'}, {'mediacode': '4857083'}, {'mediacode': '4857099'}, {'mediacode': '4857129'}, {'mediacode': '4857118'}, {'mediacode': '4857057'}, {'mediacode': '4857112'}, {'mediacode': '4857060'}, {'mediacode': '4857215'}, {'mediacode': '4857182'}, {'mediacode': '4857053'}, {'mediacode': '4857080'}, {'mediacode': '4857081'}, {'mediacode': '4857051'}, {'mediacode': '4857151'}, {'mediacode': '4857217'}, {'mediacode': '4857143'}, {'mediacode': '4857175'}, {'mediacode': '4857043'}, {'mediacode': '4857084'}, {'mediacode': '4857077'}, {'mediacode': '4857196'}, {'mediacode': '4857067'}, {'mediacode': '4857173'}, {'mediacode': '4857188'}, {'mediacode': '4857105'}, {'mediacode': '4857054'}, {'mediacode': '4857178'}, {'mediacode': '4857113'}, {'mediacode': '4857124'}, {'mediacode': '4857109'}, {'mediacode': '4857079'}, {'mediacode': '4857139'}, {'mediacode': '4857037'}, {'mediacode': '4857154'}, {'mediacode': '4857048'}, {'mediacode': '4857210'}, {'mediacode': '4857157'}, {'mediacode': '4857106'}, {'mediacode': '4857216'}, {'mediacode': '4857046'}, {'mediacode': '4857076'}, {'mediacode': '4857191'}, {'mediacode': '4857058'}, {'mediacode': '4857123'}, {'mediacode': '4857088'}, {'mediacode': '4857087'}, {'mediacode': '4857228'}, {'mediacode': '4857202'}, {'mediacode': '4857032'}, {'mediacode': '4857125'}, {'mediacode': '4857218'}, {'mediacode': '4857095'}, {'mediacode': '4857162'}, {'mediacode': '4857164'}, {'mediacode': '4857153'}, {'mediacode': '4857086'}, {'mediacode': '4857034'}, {'mediacode': '4857116'}, {'mediacode': '4857092'}, {'mediacode': '4857203'}, {'mediacode': '4857073'}, {'mediacode': '4857110'}, {'mediacode': '4857122'}, {'mediacode': '4857098'}, {'mediacode': '4857160'}, {'mediacode': '4857104'}, {'mediacode': '4857107'}, {'mediacode': '4857047'}, {'mediacode': '4857114'}, {'mediacode': '4857156'}, {'mediacode': '4857179'}, {'mediacode': '4857138'}, {'mediacode': '4857198'}, {'mediacode': '4857222'}, {'mediacode': '4857127'}, {'mediacode': '4857169'}, {'mediacode': '4857137'}, {'mediacode': '4857224'}, {'mediacode': '4857208'}, {'mediacode': '4857064'}, {'mediacode': '4857103'}, {'mediacode': '4857186'}, {'mediacode': '4857176'}, {'mediacode': '4857040'}, {'mediacode': '4857152'}, {'mediacode': '4857159'}, {'mediacode': '4857219'}, {'mediacode': '4857187'}, {'mediacode': '4857170'}, {'mediacode': '4857055'}, {'mediacode': '4857082'}, {'mediacode': '4857059'}, {'mediacode': '4857128'}, {'mediacode': '4857221'}, {'mediacode': '4857211'}, {'mediacode': '4857066'}, {'mediacode': '4857120'}, {'mediacode': '4857174'}, {'mediacode': '4857163'}, {'mediacode': '4857183'}, {'mediacode': '4857062'}, {'mediacode': '4857102'}, {'mediacode': '4857225'}, {'mediacode': '4857052'}, {'mediacode': '4857205'}, {'mediacode': '4857166'}, {'mediacode': '4857194'}, {'mediacode': '4857044'}, {'mediacode': '4857200'}, {'mediacode': '4857075'}, {'mediacode': '4857136'}, {'mediacode': '4857085'}, {'mediacode': '4857158'}, {'mediacode': '4857155'}, {'mediacode': '4857101'}, {'mediacode': '4857036'}, {'mediacode': '4857184'}, {'mediacode': '4857142'}, {'mediacode': '4857206'}, {'mediacode': '4857121'}, {'mediacode': '4857185'}, {'mediacode': '4857223'}, {'mediacode': '4857190'}, {'mediacode': '4857089'}, {'mediacode': '4857115'}, {'mediacode': '4857226'}, {'mediacode': '4857168'}, {'mediacode': '4857193'}, {'mediacode': '4857197'}, {'mediacode': '4857061'}, {'mediacode': '4857207'}, {'mediacode': '4857094'}, {'mediacode': '4857068'}, {'mediacode': '4857108'}, {'mediacode': '4857100'}, {'mediacode': '4857213'}, {'mediacode': '4857097'}, {'mediacode': '4857035'}, {'mediacode': '4857145'}, {'mediacode': '4857130'}, {'mediacode': '4857038'}, {'mediacode': '4857078'}, {'mediacode': '4857039'}, {'mediacode': '4857140'}, {'mediacode': '4857192'}, {'mediacode': '4857134'}, {'mediacode': '4857148'}], 'imgUrl': 'pic4238860.jpg', 'channel': 2, 'name': '幼教语文篇'}, {'mediacode': '5215008', 'childInfo': [{'mediacode': '5215389'}, {'mediacode': '5215379'}, {'mediacode': '5215377'}, {'mediacode': '5215369'}, {'mediacode': '5215390'}, {'mediacode': '5215380'}, {'mediacode': '5215371'}, {'mediacode': '5215376'}, {'mediacode': '5215386'}, {'mediacode': '5215383'}, {'mediacode': '5215382'}, {'mediacode': '5215393'}, {'mediacode': '5215375'}, {'mediacode': '5215392'}, {'mediacode': '5215372'}, {'mediacode': '5215384'}, {'mediacode': '5215378'}, {'mediacode': '5215385'}, {'mediacode': '5215388'}, {'mediacode': '5215381'}, {'mediacode': '5215370'}, {'mediacode': '5215387'}, {'mediacode': '5215373'}, {'mediacode': '5215368'}, {'mediacode': '5215374'}, {'mediacode': '5215391'}], 'imgUrl': 'pic4614988.jpg', 'channel': 2, 'name': '超级飞侠大百科第二季'}, {'mediacode': '5215004', 'childInfo': [{'mediacode': '5216179'}, {'mediacode': '5216175'}, {'mediacode': '5216169'}, {'mediacode': '5216188'}, {'mediacode': '5216171'}, {'mediacode': '5216173'}, {'mediacode': '5216177'}, {'mediacode': '5216180'}, {'mediacode': '5216185'}, {'mediacode': '5216191'}, {'mediacode': '5216187'}, {'mediacode': '5216182'}, {'mediacode': '5216190'}, {'mediacode': '5216178'}, {'mediacode': '5216193'}, {'mediacode': '5216172'}, {'mediacode': '5216183'}, {'mediacode': '5216174'}, {'mediacode': '5216181'}, {'mediacode': '5216192'}, {'mediacode': '5216189'}, {'mediacode': '5216184'}, {'mediacode': '5216170'}, {'mediacode': '5216186'}, {'mediacode': '5216176'}], 'imgUrl': 'pic4614959.jpg', 'channel': 2, 'name': '宝宝巴士之奇妙汉字第二季'}, {'mediacode': '5214982', 'childInfo': [{'mediacode': '5216201'}, {'mediacode': '5216204'}, {'mediacode': '5216205'}, {'mediacode': '5216207'}, {'mediacode': '5216206'}, {'mediacode': '5216215'}, {'mediacode': '5216208'}, {'mediacode': '5216213'}, {'mediacode': '5216200'}, {'mediacode': '5216210'}, {'mediacode': '5216211'}, {'mediacode': '5216202'}, {'mediacode': '5216214'}, {'mediacode': '5216198'}, {'mediacode': '5216219'}, {'mediacode': '5216209'}, {'mediacode': '5216212'}, {'mediacode': '5216199'}, {'mediacode': '5216216'}, {'mediacode': '5216195'}, {'mediacode': '5216203'}, {'mediacode': '5216218'}, {'mediacode': '5216194'}, {'mediacode': '5216217'}, {'mediacode': '5216197'}, {'mediacode': '5216196'}], 'imgUrl': 'pic4614859.jpg', 'channel': 2, 'name': '超级飞侠大百科第一季'}, {'mediacode': '5212684', 'childInfo': [{'mediacode': '5212741'}, {'mediacode': '5212744'}, {'mediacode': '5212745'}, {'mediacode': '5212747'}, {'mediacode': '5212742'}, {'mediacode': '5212743'}, {'mediacode': '5212748'}, {'mediacode': '5212746'}], 'imgUrl': 'pic4612598.jpg', 'channel': 2, 'name': '宝宝巴士之奇妙的节日'}, {'mediacode': '5221246', 'childInfo': [{'mediacode': '5228715'}, {'mediacode': '5228722'}, {'mediacode': '5228746'}, {'mediacode': '5228728'}, {'mediacode': '5228711'}, {'mediacode': '5228747'}, {'mediacode': '5228750'}, {'mediacode': '5228706'}, {'mediacode': '5228733'}, {'mediacode': '5228737'}, {'mediacode': '5228744'}, {'mediacode': '5228710'}, {'mediacode': '5228704'}, {'mediacode': '5228714'}, {'mediacode': '5228712'}, {'mediacode': '5228739'}, {'mediacode': '5228716'}, {'mediacode': '5228745'}, {'mediacode': '5228701'}, {'mediacode': '5228743'}, {'mediacode': '5228741'}, {'mediacode': '5228740'}, {'mediacode': '5228708'}, {'mediacode': '5228724'}, {'mediacode': '5228705'}, {'mediacode': '5228707'}, {'mediacode': '5228718'}, {'mediacode': '5228748'}, {'mediacode': '5228742'}, {'mediacode': '5228727'}, {'mediacode': '5228738'}, {'mediacode': '5228730'}, {'mediacode': '5228700'}, {'mediacode': '5228709'}, {'mediacode': '5228751'}, {'mediacode': '5228703'}, {'mediacode': '5228702'}, {'mediacode': '5228735'}, {'mediacode': '5228717'}, {'mediacode': '5228734'}, {'mediacode': '5228731'}, {'mediacode': '5228713'}, {'mediacode': '5228719'}, {'mediacode': '5228749'}, {'mediacode': '5228729'}, {'mediacode': '5228725'}, {'mediacode': '5228721'}, {'mediacode': '5228736'}, {'mediacode': '5228723'}, {'mediacode': '5228726'}, {'mediacode': '5228732'}, {'mediacode': '5228720'}], 'imgUrl': 'pic4618363.jpg', 'channel': 2, 'name': '美食大冒险之文明之旅'}, {'mediacode': '5236784', 'childInfo': [{'mediacode': '5236838'}, {'mediacode': '5236832'}, {'mediacode': '5236839'}, {'mediacode': '5236833'}, {'mediacode': '5236848'}, {'mediacode': '5236824'}, {'mediacode': '5236829'}, {'mediacode': '5236835'}, {'mediacode': '5236830'}, {'mediacode': '5236847'}, {'mediacode': '5236851'}, {'mediacode': '5236840'}, {'mediacode': '5236846'}, {'mediacode': '5236831'}, {'mediacode': '5236844'}, {'mediacode': '5236822'}, {'mediacode': '5236842'}, {'mediacode': '5236849'}, {'mediacode': '5236850'}, {'mediacode': '5236845'}, {'mediacode': '5236843'}, {'mediacode': '5236827'}, {'mediacode': '5236837'}, {'mediacode': '5236841'}, {'mediacode': '5236834'}, {'mediacode': '5236823'}, {'mediacode': '5236825'}, {'mediacode': '5236836'}, {'mediacode': '5236828'}, {'mediacode': '5236826'}], 'imgUrl': 'pic4636042.jpg', 'channel': 2, 'name': '红果果英语儿歌'}, {'mediacode': '5269450', 'childInfo': [{'mediacode': '5269596'}, {'mediacode': '5269594'}, {'mediacode': '5269599'}, {'mediacode': '5269600'}, {'mediacode': '5269592'}, {'mediacode': '5269597'}, {'mediacode': '5269590'}, {'mediacode': '5269595'}, {'mediacode': '5269598'}, {'mediacode': '5269593'}, {'mediacode': '5269601'}, {'mediacode': '5269591'}], 'imgUrl': 'pic4667940.jpg', 'channel': 2, 'name': '小普林变变变第一季'}, {'mediacode': '5285584', 'childInfo': [{'mediacode': '5285632'}, {'mediacode': '5285645'}, {'mediacode': '5285626'}, {'mediacode': '5285646'}, {'mediacode': '5285629'}, {'mediacode': '5285627'}, {'mediacode': '5285633'}, {'mediacode': '5285630'}, {'mediacode': '5285644'}, {'mediacode': '5285625'}, {'mediacode': '5285631'}, {'mediacode': '5285636'}, {'mediacode': '5285637'}, {'mediacode': '5285628'}, {'mediacode': '5285642'}, {'mediacode': '5285635'}, {'mediacode': '5285634'}, {'mediacode': '5285641'}, {'mediacode': '5285638'}, {'mediacode': '5285639'}, {'mediacode': '5285643'}, {'mediacode': '5285624'}, {'mediacode': '5285640'}], 'imgUrl': 'pic4683419.jpg', 'channel': 2, 'name': '宝宝语言启蒙'}, {'mediacode': '5335713', 'childInfo': [{'mediacode': '5336178'}, {'mediacode': '5336168'}, {'mediacode': '5336205'}, {'mediacode': '5336183'}, {'mediacode': '5336167'}, {'mediacode': '5336190'}, {'mediacode': '5336173'}, {'mediacode': '5336181'}, {'mediacode': '5336180'}, {'mediacode': '5336165'}, {'mediacode': '5336211'}, {'mediacode': '5336201'}, {'mediacode': '5336185'}, {'mediacode': '5336171'}, {'mediacode': '5336196'}, {'mediacode': '5336207'}, {'mediacode': '5336182'}, {'mediacode': '5336210'}, {'mediacode': '5336200'}, {'mediacode': '5336203'}, {'mediacode': '5336175'}, {'mediacode': '5336164'}, {'mediacode': '5336191'}, {'mediacode': '5336193'}, {'mediacode': '5336197'}, {'mediacode': '5336169'}, {'mediacode': '5336187'}, {'mediacode': '5336212'}, {'mediacode': '5336170'}, {'mediacode': '5336166'}, {'mediacode': '5336199'}, {'mediacode': '5336198'}, {'mediacode': '5336184'}, {'mediacode': '5336186'}, {'mediacode': '5336177'}, {'mediacode': '5336208'}, {'mediacode': '5336209'}, {'mediacode': '5336189'}, {'mediacode': '5336179'}, {'mediacode': '5336204'}, {'mediacode': '5336174'}, {'mediacode': '5336206'}, {'mediacode': '5336192'}, {'mediacode': '5336188'}, {'mediacode': '5336202'}, {'mediacode': '5336213'}, {'mediacode': '5336195'}, {'mediacode': '5336172'}, {'mediacode': '5336176'}, {'mediacode': '5336194'}], 'imgUrl': 'pic4732945.jpg', 'channel': 2, 'name': '聪明宝宝学英语'}, {'mediacode': '5353424', 'childInfo': [{'mediacode': '5353552'}, {'mediacode': '5353546'}, {'mediacode': '5353580'}, {'mediacode': '5353572'}, {'mediacode': '5353549'}, {'mediacode': '5353539'}, {'mediacode': '5353589'}, {'mediacode': '5353567'}, {'mediacode': '5353583'}, {'mediacode': '5353518'}, {'mediacode': '5353532'}, {'mediacode': '5353525'}, {'mediacode': '5353535'}, {'mediacode': '5353523'}, {'mediacode': '5353563'}, {'mediacode': '5353609'}, {'mediacode': '5353607'}, {'mediacode': '5353608'}, {'mediacode': '5353603'}, {'mediacode': '5353571'}, {'mediacode': '5353610'}, {'mediacode': '5353577'}, {'mediacode': '5353547'}, {'mediacode': '5353574'}, {'mediacode': '5353554'}, {'mediacode': '5353553'}, {'mediacode': '5353560'}, {'mediacode': '5353573'}, {'mediacode': '5353604'}, {'mediacode': '5353586'}, {'mediacode': '5353530'}, {'mediacode': '5353520'}, {'mediacode': '5353575'}, {'mediacode': '5353537'}, {'mediacode': '5353521'}, {'mediacode': '5353544'}, {'mediacode': '5353516'}, {'mediacode': '5353566'}, {'mediacode': '5353576'}, {'mediacode': '5353582'}, {'mediacode': '5353606'}, {'mediacode': '5353578'}, {'mediacode': '5353587'}, {'mediacode': '5353536'}, {'mediacode': '5353602'}, {'mediacode': '5353534'}, {'mediacode': '5353548'}, {'mediacode': '5353555'}, {'mediacode': '5353533'}, {'mediacode': '5353531'}, {'mediacode': '5353561'}, {'mediacode': '5353515'}, {'mediacode': '5353584'}, {'mediacode': '5353527'}, {'mediacode': '5353570'}, {'mediacode': '5353557'}, {'mediacode': '5353588'}, {'mediacode': '5353611'}, {'mediacode': '5353581'}, {'mediacode': '5353513'}, {'mediacode': '5353556'}, {'mediacode': '5353562'}, {'mediacode': '5353612'}, {'mediacode': '5353512'}, {'mediacode': '5353569'}, {'mediacode': '5353528'}, {'mediacode': '5353558'}, {'mediacode': '5353510'}, {'mediacode': '5353524'}, {'mediacode': '5353559'}, {'mediacode': '5353585'}, {'mediacode': '5353529'}, {'mediacode': '5353568'}, {'mediacode': '5353517'}, {'mediacode': '5353564'}, {'mediacode': '5353511'}, {'mediacode': '5353605'}, {'mediacode': '5353509'}, {'mediacode': '5353565'}, {'mediacode': '5353543'}, {'mediacode': '5353545'}, {'mediacode': '5353522'}, {'mediacode': '5353541'}, {'mediacode': '5353540'}, {'mediacode': '5353613'}, {'mediacode': '5353550'}, {'mediacode': '5353579'}, {'mediacode': '5353514'}, {'mediacode': '5353538'}, {'mediacode': '5353526'}, {'mediacode': '5353551'}, {'mediacode': '5353542'}], 'imgUrl': 'pic4750419.jpg', 'channel': 2, 'name': '儿童国学 '}, {'mediacode': '5420092', 'childInfo': [{'mediacode': '5420259'}, {'mediacode': '5420265'}, {'mediacode': '5420253'}, {'mediacode': '5420257'}, {'mediacode': '5420261'}, {'mediacode': '5420255'}, {'mediacode': '5420254'}, {'mediacode': '5420264'}, {'mediacode': '5420263'}, {'mediacode': '5420268'}, {'mediacode': '5420258'}, {'mediacode': '5420260'}, {'mediacode': '5420267'}, {'mediacode': '5420262'}, {'mediacode': '5420266'}, {'mediacode': '5420256'}], 'imgUrl': 'pic4782356.jpg', 'channel': 2, 'name': '好习惯不用教'}, {'mediacode': '5443714', 'childInfo': [{'mediacode': '5447213'}, {'mediacode': '5447207'}, {'mediacode': '5447204'}, {'mediacode': '5447205'}, {'mediacode': '5447206'}, {'mediacode': '5447208'}, {'mediacode': '5447218'}, {'mediacode': '5447201'}, {'mediacode': '5447212'}, {'mediacode': '5447210'}, {'mediacode': '5447203'}, {'mediacode': '5447209'}, {'mediacode': '5447219'}, {'mediacode': '5447211'}, {'mediacode': '5447215'}, {'mediacode': '5447216'}, {'mediacode': '5447220'}, {'mediacode': '5447214'}, {'mediacode': '5447202'}, {'mediacode': '5447217'}], 'imgUrl': 'pic4840121.jpg', 'channel': 2, 'name': '宝宝巴士之奇妙数字大冒险'}]}
# # print(len(dic2["data"]))
# if len(dic2["data"]) > 10:
# 	for k in range(0, len(dic2["data"]) // 10 + 1):
# 		if (k + 1) * 10 >= len(dic2["data"]):
# 			dic = {"data": dic2["data"][k * 10:len(dic2["data"])]}
# 			fin_json = json.dumps(dic, indent=2, ensure_ascii=False)
# 			with open("list_%s.json" % k, "wb+") as fd:
# 				fd.write(fin_json.encode('utf-8'))
# 				# open("list_%s.json" % k, "w").writelines(fin_json.encode('utf-8'))
# 		else:
# 			dic = {"data": dic2["data"][k * 10:(k + 1) * 10]}
# 			fin_json = json.dumps(dic, indent=2, ensure_ascii=False)
# 			with open("list_%s.json" % k, "wb+") as fd:
# 				fd.write(fin_json.encode('utf-8'))
# 			# open("list_%s.json" % k, "w").writelines(fin_json.encode('utf-8'))
# else:
# 	fin_json = json.dumps(dic2, indent=2, ensure_ascii=False)
# 	print(3, fin_json)
data=[]
fu_txt=open("fu.txt", "r").readlines()
zi_txt=open("zi.txt", "r").readlines()
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
result=json.dumps({"data":data},indent=2,ensure_ascii=False)

open("list.json","w").writelines(result.encode('utf-8'))
