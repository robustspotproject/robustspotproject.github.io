import pandas as pd
import json
import re

prefix_type="seed"
column_name ='ratio of aliased prefix'

csv_file_name_5=f"{prefix_type}_prefix_day_5_sub_category_sat.csv"
csv_file_name_4=f"{prefix_type}_prefix_day_5_org_sat.csv"
csv_file_name_3=f"{prefix_type}_prefix_day_5_country_sat.csv"
csv_file_name_2=f"{prefix_type}_prefix_day_5_category_sat.csv"
csv_file_name_1=f"{prefix_type}_prefix_day_5_as_sat.csv"


pic_name_5="Sub_category-Num"
pic_name_4="Org-AS-Num"
pic_name_3="Country-Num"
pic_name_2="Category-Num"
pic_name_1="AS-Num-Org"

csv_file_name=csv_file_name_5
pic_name=pic_name_5
select_num=9

df = pd.read_csv(csv_file_name)
df=df.sort_values(by=column_name,ascending=False,inplace=False)
other_ratio=1-df[column_name][:select_num].sum()

data=[]
for index,df_iterrow in df[:select_num].iterrows():
  as_name_str=f"{df_iterrow['as']}-{df_iterrow['number of aliased prefix']}-{df_iterrow['org_name']}"
  category_name_str=f"{df_iterrow['category']}-{df_iterrow['number of aliased prefix']}"
  country_name_str = f"{df_iterrow['country']}-{df_iterrow['number of aliased prefix']}"
  org_name_str = f"{df_iterrow['org_name']}-{df_iterrow['as']}-{df_iterrow['number of aliased prefix']}"
  sub_category_name_str=f"{df_iterrow['sub_category']}-{df_iterrow['number of aliased prefix']}"

  data_dict={}
  data_dict["name"]=sub_category_name_str
  data_dict["y"]=df_iterrow[column_name]
  data.append(data_dict)

data_dict={}
data_dict["name"]="Others"
data_dict["y"]=other_ratio
data.append(data_dict)

# 创建JSON数据
json_data = {
  "chart": {
    "plotBackgroundColor": "white",
    "plotBorderWidth": "0",
    "plotShadow": "false",
    "type": "pie"
  },
  "title": {
    "text": pic_name,
    "align": "left"
  },
  "tooltip": {
    "pointFormat": "{series.name}: <b>{point.percentage:.1f}%</b>"
  },
  "accessibility": {
    "point": {
      "valueSuffix": "%"
    }
  },
  "plotOptions": {
    "pie": {
      "allowPointSelect": "true",
      "cursor": "pointer",
      "dataLabels": {
        "enabled": "false"
      },
      "showInLegend": "true"
    }
  },
  "series": [
    {
      "name": column_name,
      "colorByPoint": "true",
      "data": data
    }
  ]
}

# 将JSON数据保存到文件或以其他方式使用
with open(f"{csv_file_name.split('.csv')[0]}.json", 'w') as json_file:
    json.dump(json_data, json_file, indent=2)
