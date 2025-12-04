# FLUSHDB

> 可用版本： >= 1.0.0
>
> 时间复杂度： O(1)

清空当前数据库中的所有 key。

此命令从不失败。

## 返回值

总是返回 `OK` 。

## 代码示例

```
redis> DBSIZE    # 清空前的 key 数量
(integer) 4

redis> FLUSHDB
OK

redis> DBSIZE    # 清空后的 key 数量
(integer) 0
```

## 讨论 [¶](#discuss "永久链接至标题")

Please enable JavaScript to view the [comments powered by Disqus.](http://disqus.com/?ref_noscript)
[comments powered by Disqus](http://disqus.com)