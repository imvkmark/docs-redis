# Redis 命令参考

本文档是 [Redis Command Reference](http://redis.io/commands) 和 [Redis Documentation](http://redis.io/documentation) 的中文翻译版，
阅读这个文档可以帮助你了解 Redis 命令的具体使用方法，
并学会如何使用 Redis 的事务、持久化、复制、Sentinel、集群等功能。

Note

![images/guide-cover.png](images/guide-cover.png)

由本文档译者黄健宏创作的《Redis使用手册》正在热卖中，欢迎选购：[RedisGuide.com](http://redisguide.com/) 。

* [字符串](string/index.md)
  + [SET](string/set.md)
  + [SETNX](string/setnx.md)
  + [SETEX](string/setex.md)
  + [PSETEX](string/psetex.md)
  + [GET](string/get.md)
  + [GETSET](string/getset.md)
  + [STRLEN](string/strlen.md)
  + [APPEND](string/append.md)
  + [SETRANGE](string/setrange.md)
  + [GETRANGE](string/getrange.md)
  + [INCR](string/incr.md)
  + [INCRBY](string/incrby.md)
  + [INCRBYFLOAT](string/incrbyfloat.md)
  + [DECR](string/decr.md)
  + [DECRBY](string/decrby.md)
  + [MSET](string/mset.md)
  + [MSETNX](string/msetnx.md)
  + [MGET](string/mget.md)
* [哈希表](hash/index.md)
  + [HSET](hash/hset.md)
  + [HSETNX](hash/hsetnx.md)
  + [HGET](hash/hget.md)
  + [HEXISTS](hash/hexists.md)
  + [HDEL](hash/hdel.md)
  + [HLEN](hash/hlen.md)
  + [HSTRLEN](hash/hstrlen.md)
  + [HINCRBY](hash/hincrby.md)
  + [HINCRBYFLOAT](hash/hincrbyfloat.md)
  + [HMSET](hash/hmset.md)
  + [HMGET](hash/hmget.md)
  + [HKEYS](hash/hkeys.md)
  + [HVALS](hash/hvals.md)
  + [HGETALL](hash/hgetall.md)
  + [HSCAN](hash/hscan.md)
* [列表](list/index.md)
  + [LPUSH](list/lpush.md)
  + [LPUSHX](list/lpushx.md)
  + [RPUSH](list/rpush.md)
  + [RPUSHX](list/rpushx.md)
  + [LPOP](list/lpop.md)
  + [RPOP](list/rpop.md)
  + [RPOPLPUSH](list/rpoplpush.md)
  + [LREM](list/lrem.md)
  + [LLEN](list/llen.md)
  + [LINDEX](list/lindex.md)
  + [LINSERT](list/linsert.md)
  + [LSET](list/lset.md)
  + [LRANGE](list/lrange.md)
  + [LTRIM](list/ltrim.md)
  + [BLPOP](list/blpop.md)
  + [BRPOP](list/brpop.md)
  + [BRPOPLPUSH](list/brpoplpush.md)
* [集合](set/index.md)
  + [SADD](set/sadd.md)
  + [SISMEMBER](set/sismember.md)
  + [SPOP](set/spop.md)
  + [SRANDMEMBER](set/srandmember.md)
  + [SREM](set/srem.md)
  + [SMOVE](set/smove.md)
  + [SCARD](set/scard.md)
  + [SMEMBERS](set/smembers.md)
  + [SSCAN](set/sscan.md)
  + [SINTER](set/sinter.md)
  + [SINTERSTORE](set/sinterstore.md)
  + [SUNION](set/sunion.md)
  + [SUNIONSTORE](set/sunionstore.md)
  + [SDIFF](set/sdiff.md)
  + [SDIFFSTORE](set/sdiffstore.md)
* [有序集合](sorted_set/index.md)
  + [ZADD](sorted_set/zadd.md)
  + [ZSCORE](sorted_set/zscore.md)
  + [ZINCRBY](sorted_set/zincrby.md)
  + [ZCARD](sorted_set/zcard.md)
  + [ZCOUNT](sorted_set/zcount.md)
  + [ZRANGE](sorted_set/zrange.md)
  + [ZREVRANGE](sorted_set/zrevrange.md)
  + [ZRANGEBYSCORE](sorted_set/zrangebyscore.md)
  + [ZREVRANGEBYSCORE](sorted_set/zrevrangebyscore.md)
  + [ZRANK](sorted_set/zrank.md)
  + [ZREVRANK](sorted_set/zrevrank.md)
  + [ZREM](sorted_set/zrem.md)
  + [ZREMRANGEBYRANK](sorted_set/zremrangebyrank.md)
  + [ZREMRANGEBYSCORE](sorted_set/zremrangebyscore.md)
  + [ZRANGEBYLEX](sorted_set/zrangebylex.md)
  + [ZLEXCOUNT](sorted_set/zlexcount.md)
  + [ZREMRANGEBYLEX](sorted_set/zremrangebylex.md)
  + [ZSCAN](sorted_set/zscan.md)
  + [ZUNIONSTORE](sorted_set/zunionstore.md)
  + [ZINTERSTORE](sorted_set/zinterstore.md)
* [HyperLogLog](hyperloglog/index.md)
  + [PFADD](hyperloglog/pfadd.md)
  + [PFCOUNT](hyperloglog/pfcount.md)
  + [PFMERGE](hyperloglog/pfmerge.md)
* [地理位置](geo/index.md)
  + [GEOADD](geo/geoadd.md)
  + [GEOPOS](geo/geopos.md)
  + [GEODIST](geo/geodist.md)
  + [GEORADIUS](geo/georadius.md)
  + [GEORADIUSBYMEMBER](geo/georadiusbymember.md)
  + [GEOHASH](geo/geohash.md)
* [位图](bitmap/index.md)
  + [SETBIT](bitmap/setbit.md)
  + [GETBIT](bitmap/getbit.md)
  + [BITCOUNT](bitmap/bitcount.md)
  + [BITPOS](bitmap/bitpos.md)
  + [BITOP](bitmap/bitop.md)
  + [BITFIELD](bitmap/bitfield.md)
* [数据库](database/index.md)
  + [EXISTS](database/exists.md)
  + [TYPE](database/type.md)
  + [RENAME](database/rename.md)
  + [RENAMENX](database/renamenx.md)
  + [MOVE](database/move.md)
  + [DEL](database/del.md)
  + [RANDOMKEY](database/randomkey.md)
  + [DBSIZE](database/dbsize.md)
  + [KEYS](database/keys.md)
  + [SCAN](database/scan.md)
  + [SORT](database/sort.md)
  + [FLUSHDB](database/flushdb.md)
  + [FLUSHALL](database/flushall.md)
  + [SELECT](database/select.md)
  + [SWAPDB](database/swapdb.md)
* [自动过期](expire/index.md)
  + [EXPIRE](expire/expire.md)
  + [EXPIREAT](expire/expireat.md)
  + [TTL](expire/ttl.md)
  + [PERSIST](expire/persist.md)
  + [PEXPIRE](expire/pexpire.md)
  + [PEXPIREAT](expire/pexpireat.md)
  + [PTTL](expire/pttl.md)
* [事务](transaction/index.md)
  + [MULTI](transaction/multi.md)
  + [EXEC](transaction/exec.md)
  + [DISCARD](transaction/discard.md)
  + [WATCH](transaction/watch.md)
  + [UNWATCH](transaction/unwatch.md)
* [Lua 脚本](script/index.md)
  + [EVAL](script/eval.md)
  + [EVALSHA](script/evalsha.md)
  + [SCRIPT\_LOAD](script/script_load.md)
  + [SCRIPT\_EXISTS](script/script_exists.md)
  + [SCRIPT\_FLUSH](script/script_flush.md)
  + [SCRIPT\_KILL](script/script_kill.md)
* [持久化](persistence/index.md)
  + [SAVE](persistence/save.md)
  + [BGSAVE](persistence/bgsave.md)
  + [BGREWRITEAOF](persistence/bgrewriteaof.md)
  + [LASTSAVE](persistence/lastsave.md)
* [发布与订阅](pubsub/index.md)
  + [PUBLISH](pubsub/publish.md)
  + [SUBSCRIBE](pubsub/subscribe.md)
  + [PSUBSCRIBE](pubsub/psubscribe.md)
  + [UNSUBSCRIBE](pubsub/unsubscribe.md)
  + [PUNSUBSCRIBE](pubsub/punsubscribe.md)
  + [PUBSUB](pubsub/pubsub.md)
* [复制](replication/index.md)
  + [SLAVEOF](replication/slaveof.md)
  + [ROLE](replication/role.md)
* [客户端与服务器](client_and_server/index.md)
  + [AUTH](client_and_server/auth.md)
  + [QUIT](client_and_server/quit.md)
  + [INFO](client_and_server/info.md)
  + [SHUTDOWN](client_and_server/shutdown.md)
  + [TIME](client_and_server/time.md)
  + [CLIENT\_GETNAME](client_and_server/client_getname.md)
  + [CLIENT\_KILL](client_and_server/client_kill.md)
  + [CLIENT\_LIST](client_and_server/client_list.md)
  + [CLIENT\_SETNAME](client_and_server/client_setname.md)
* [配置选项](configure/index.md)
  + [CONFIG\_SET](configure/config_set.md)
  + [CONFIG\_GET](configure/config_get.md)
  + [CONFIG\_RESETSTAT](configure/config_resetstat.md)
  + [CONFIG\_REWRITE](configure/config_rewrite.md)
* [调试](debug/index.md)
  + [PING](debug/ping.md)
  + [ECHO](debug/echo.md)
  + [OBJECT](debug/object.md)
  + [SLOWLOG](debug/slowlog.md)
  + [MONITOR](debug/monitor.md)
  + [DEBUG\_OBJECT](debug/debug_object.md)
  + [DEBUG\_SEGFAULT](debug/debug_segfault.md)
* [内部命令](internal/index.md)
  + [MIGRATE](internal/migrate.md)
  + [DUMP](internal/dump.md)
  + [RESTORE](internal/restore.md)
  + [SYNC](internal/sync.md)
  + [PSYNC](internal/psync.md)
* [功能文档](topic/index.md)
  + [Redis 集群规范](topic/cluster-spec.md)
  + [持久化（persistence）](topic/persistence.md)
  + [发布与订阅（pub/sub）](topic/pubsub.md)
  + [Sentinel](topic/sentinel.md)
  + [集群教程](topic/cluster-tutorial.md)
  + [键空间通知（keyspace notification）](topic/notification.md)
  + [通信协议（protocol）](topic/protocol.md)
  + [复制（Replication）](topic/replication.md)
  + [事务（transaction）](topic/transaction.md)

## 关于

本文档由 [黄健宏（huangz）](http://www.huangz.me) 翻译，
版权归 Redis 官方所有。

[更新日志(change log)](change_log.md#change-log) 列出了本文档的主要更新细节，
你也可以通过关注 [文档的 github 项目](https://github.com/huangz1990/redis) 来随时追踪文档的最新更新信息。

有任何问题、意见或建议，
请在文档配套的 disqus 论坛里留言，
或者直接联系译者。

## Redis 书籍推荐

![images/guide-cover.png](images/guide-cover.png)

由本文档译者黄健宏创作的《Redis 使用手册》正在热销中，
该书详细地介绍了 Redis 各个命名的描述及其使用方法，
是 Redis 使用者和初学者必不可少的参考书。

欢迎访问 [RedisGuide.com](http://redisguide.com) 并了解关于《Redis 使用手册》的更多信息。

---

![images/cover.png](images/cover.png)

由本文档译者黄健宏创作的《Redis 设计与实现》一书正在热销中，
该书详细地介绍了 Redis 内部的运作原理以及各项功能的实现原理，
是一本致力于帮助 Redis 使用者加深对 Redis 的理解，
并且更高效地使用 Redis 的书籍。

欢迎访问 [RedisBook.com](http://www.RedisBook.com) 并了解《Redis 设计与实现》的更多相关信息。

---

![images/riacn-cover.png](images/riacn-cover.png)

由本文档译者黄健宏翻译的《Redis实战》一书正在火热发售中，
该书深入浅出地介绍了 Redis 的五种数据结构，
并通过一系列实用的示例深刻地展示了 Redis 的用法。
此外，
《Redis实战》还介绍了多种扩展和优化 Redis 的方法，
无论是 Redis 新手还是有一定经验的 Redis 使用者，
应该都能从此书中获益。

欢迎访问 [redisinaction.com](http://redisinaction.com) 并了解《Redis实战》的更多相关信息。

## 参加群讨论

欢迎各位《Redis命令参考》读者加入译者开设的 QQ 群，
你可以在里面分享你的 Redis 使用心得，
又或者跟其他群友讨论你在使用 Redis 过程中遇到的问题，
具体的群号请访问译者的[个人主页](http://huangz.me) 查看。

## 讨论 [¶](#discuss "永久链接至标题")

Please enable JavaScript to view the [comments powered by Disqus.](http://disqus.com/?ref_noscript)
[comments powered by Disqus](http://disqus.com)