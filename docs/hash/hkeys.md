# HKEYS

**HKEYS key**

返回哈希表 `key` 中的所有域。

**可用版本：**
:   >= 2.0.0

**时间复杂度：**
:   O(N)， `N` 为哈希表的大小。

**返回值：**
:   一个包含哈希表中所有域的表。

    当 `key` 不存在时，返回一个空表。

```
# 哈希表非空

redis> HMSET website google www.google.com yahoo www.yahoo.com
OK

redis> HKEYS website
1) "google"
2) "yahoo"


# 空哈希表/key不存在

redis> EXISTS fake_key
(integer) 0

redis> HKEYS fake_key
(empty list or set)
```

## 讨论 [¶](#discuss "永久链接至标题")

Please enable JavaScript to view the [comments powered by Disqus.](http://disqus.com/?ref_noscript)
[comments powered by Disqus](http://disqus.com)