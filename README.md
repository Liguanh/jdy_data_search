#### 功能简介
此项目仅用于九斗鱼债权梳理的小项目, 志在通过待回款的项目推出相关的债权关系信息，包括正常债权和第三方的个人借款的债权，并过滤出第三方借款人详情和关联的第三方债权包金额不匹配的债权数据，最后做统一导出execl,
中间过程中包括项目ID，债权ID，项目信息列表等临时文件,最终执行完成后会生成5个生成文件

#### 命令行介绍

项目目录下有个`app.py` 文件，是脚本执行的入口文件

* python app.py --help 
> 显示当前入口文件的命令行帮助信息

* python app.py --refund refund 

> 回款表中获取待回款的项目id集合，并生成项目ID集合的txt文件

* python app.py --project project

> 通过上一步命令获得的项目ID集合，获取项目信息，并生成execl文件到本地，如果上一步未执行，当前执行会停止

* python app.py --link project_link_credit 

 > 通过项目ID集合获取项目关联债权关系的债权ID集合，并导出到txt文件, 如果没有项目ID，执行停止

 * python app.py --credit credit

  > 通过上一步的债权ID信息集合，获取金额不匹配的债权以及所有的债权关联关系信息，并坐导出execl中，如果上一步未执行，当前执行会停止


  #### 版本支持

  * python3版本
  * yaml 包支持
  * argparse 模块支持
  * tablib 第三方模块支持
  * pymysql 数据库模块支持
