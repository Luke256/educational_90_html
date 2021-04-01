# -*- coding:utf8 -*-

import subprocess, os


print("問題更新中")
try:
    os.chdir("kyopro_educational_90/")
    subprocess.check_output(["git","pull","origin","main"])
    os.chdir("../")
    print("成功")
except:
    os.chdir("../")
    print("失敗")
    exit()

print("問題ファイル作成中")

files = os.listdir("./kyopro_educational_90/problem")
files.remove("sample.jpg")
files.sort()

with open("template.html") as f:
    TEMPLATE=f.read()

for task in files:
    name=task.split('.')[0]
    
    
    with open("tasks/{name}.html".format(name=name), mode="w") as f:

        with open("kyopro_educational_90/sample/{name}.txt".format(name=name)) as sample:
            samples=sample.read().split("----------")

            # 入力形式
            input_shape=samples[0][6:].replace("\n","<br>")
            samples.remove(samples[0])

            input_sample="<hr>"
            for case in samples:
                res=""
                raw=case.split("\n")

                ipt=[s for s in raw if s.startswith('# 入力例 ')][0]
                opt=[s for s in raw if s.startswith('# 出力例 ')][0]

                raw.remove(ipt)
                raw.remove(opt)
                while(raw[0]==""):
                    raw.remove("")

                # 入力例
                res+='<h2 class="uk-heading-bullet uk-padding-small">{case_name}</h2>'.format(case_name=ipt[2:])
                res+='<div class="uk-card uk-card-default uk-padding-small uk-margin-left uk-margin-right">'
                inputs=[]
                while(len(raw) and raw[0]!=""):
                    inputs.append(raw[0])
                    raw.remove(raw[0])
                res+="<br>".join(inputs)
                res+="</div>"

                raw.remove("")

                # 出力例
                res+='<h2 class="uk-heading-bullet uk-padding-small">{case_name}</h2>'.format(case_name=opt[2:])
                res+='<div class="uk-card uk-card-default uk-padding-small uk-margin-left uk-margin-right">'
                outputs=[]
                while(len(raw) and raw[0]!=""):
                    outputs.append(raw[0])
                    raw.remove(raw[0])
                res+="<br>".join(outputs)
                res+="</div>"
                
                # 改行文字だったものは全部削除(備考があればそれだけ残るはず)
                while "" in raw:
                    raw.remove("")

                # 残ったものを改行区切りで出力
                res+="<br>".join(raw)
                res+="<hr>"

                input_sample+=res


        # 解説・ソースコード
        try:
            with open("kyopro_educational_90/sol/{name}.cpp".format(name=name), encoding = "shift_jis") as code:
                sample_code=code.read()

        # まだ解説が公開されていなければスルー
        except FileNotFoundError:
            sample_code="まだ解説が公開されていません"

        value=TEMPLATE.format(name=name,input_shape=input_shape, sample=input_sample, sample_code=sample_code)

        f.write(value)

print("完了")