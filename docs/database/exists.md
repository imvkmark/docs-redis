# EXISTS key

> 可用版本： >= 1.0.0
>
> 时间复杂度： O(1)

检查给定 `key` 是否存在。

## 返回值

若 `key` 存在，返回 `1` ，否则返回 `0` 。

## 代码示例

```
redis> SET db "redis"
OK

redis> EXISTS db
(integer) 1

redis> DEL db
(integer) 1

redis> EXISTS db
(integer) 0
```

## 讨论 [¶](#discuss "永久链接至标题")

Please enable JavaScript to view the [comments powered by Disqus.](http://disqus.com/?ref_noscript)
[comments powered by Disqus](http://disqus.com)