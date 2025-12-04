# 更新日志(change log)

## 2019 年 2 月 8 日（Redis 3+）

* 更换了新皮肤
* 全面更新了命令的样式
* 添加了 `BITMAP` 、 `SWAPDB` 、 `ROLE` 命令的文档翻译

## 2016 年 7 月 27 日（Redis 3.2）

添加 `HSTRLEN` 命令的文档翻译。

## 2016 年 7 月 21 日（Redis 3.2）

添加 `BITFIELD` 命令的文档翻译。

## 2015 年 8 月 10 日（Redis 3.2）

添加 `GEOADD` 、 `GEOPOS` 、 `GEORADIUS` 、 `GEORADIUSBYMEMBER` 和 `GEOHASH` 这五个 GEO 特性命令的文档翻译。

## 2015 年 8 月 3 日

[云巴（yunba.io）](http://yunba.io/) 成为本文档的赞助商。

## 2014 年 12 月 31 日（Redis 2.8）

* 添加 [PFADD key element [element …]](hyperloglog/pfadd.md#pfadd) 、 [PFCOUNT key [key …]](hyperloglog/pfcount.md#pfcount) 和 [PFMERGE destkey sourcekey [sourcekey …]](hyperloglog/pfmerge.md#pfmerge) 三个 HyperLogLog 命令。
* 添加 [ZRANGEBYLEX key min max [LIMIT offset count]](sorted_set/zrangebylex.md#zrangebylex) 、 [ZLEXCOUNT key min max](sorted_set/zlexcount.md#zlexcount) 和 [ZREMRANGEBYLEX key min max](sorted_set/zremrangebylex.md#zremrangebylex) 三个有序集合命令。

## 2013 年 12 月(Redis 2.8)

Redis 2.8 带来的更新：

* 添加 [SCAN cursor [MATCH pattern] [COUNT count]](database/scan.md#scan) 命令、 [SSCAN key cursor [MATCH pattern] [COUNT count]](set/sscan.md#sscan) 命令、 [HSCAN](hash/hscan.md#hscan) 命令和 [ZSCAN key cursor [MATCH pattern] [COUNT count]](sorted_set/zscan.md#zscan) 命令。
* 添加 [CONFIG REWRITE](configure/config_rewrite.md#config-rewrite) 命令。
* 添加 [PUBSUB &lt;subcommand&gt; [argument [argument …]]](pubsub/pubsub.md#pubsub) 命令。
* 添加 [CLIENT SETNAME connection-name](client_and_server/client_setname.md#client-setname) 命令和 [CLIENT GETNAME](client_and_server/client_getname.md#client-getname) 命令。
* 修改 [TTL key](expire/ttl.md#ttl) 和 [PTTL key](expire/pttl.md#pttl) 命令的返回值。

文档本身的更新：

* 开始翻译 Redis 的主题（topic）文档：
  目前已经完成了 [集群教程](topic/cluster-tutorial.md#cluster-tutorial) 、 [Sentinel](topic/sentinel.md#sentinel) 、 [复制（Replication）](topic/replication.md#replication-topic) 、 [持久化（persistence）](topic/persistence.md#persistence) 等主要文档，
  未来还会翻译更多主题文档。
* 支持 PDF 格式的离线文档下载。
* 添加捐款连接。

## 2012 年 5 月（Redis 2.6）

[42区VPS（vps.42qu.com）](http://vps.42qu.com) 成为本文档的赞助商。

## 2012 年 4 月(Redis 2.6)

此次更新的主要内容来自于 Redis 2.6 版本：

* 2.6 版本新增的所有命令(EVAL 、 SCRIPT \* 、 TIME 、 PTTL 等)的相关文档全部翻译完毕。
* 2.6 版本新添加的几个应用模式，比如 INCR 命令的计数器模式和限速器模式、 EXPIRE 命令的导航会话模型等，全部翻译完毕。
* 2.6 版本对旧有命令的改进，比如为 SHUTDOWN 添加修饰符、为 INFO 设置新的输出格式 、 CONFIG RESETSTAT 的变动等，这些命令的文档全部翻译/更新完毕。
* 对代码示例及其注释进行了很多修改和重排版，让代码示例更直观。

文档自身的更新：

* 添加 disqus 评论功能。
* 命令不再按类型分页，而是每个命令各一页，载入速度更快。
* 添加进度表，随时了解项目最新动态。

## 2011 年 12 月(Redis 2.4)

完成 pub/sub 、 transaction 、 connection 和 server 四个部分的翻译。

## 2011 年 10 月(Redis 2.4)

更新命令到 Redis 2.4 版本。

## 2011 年 6 月(Redis 2.2)

完成 keys 、 string 、 list 、 set 和 sorted set 六个部分的翻译。

## 2011 年 4 月(Redis 2.2)

开始进行 Redis 命令参考的翻译工作。
