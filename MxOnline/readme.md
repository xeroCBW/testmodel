### 注意要文件mark as source root

### 设置过滤器/排序/搜索

http://localhost:8000/organization/course-org/?ordering=-click_nums

1. 过滤+排序可以一起
2. 搜索+排序 可以一起
3. 实现多个条件查询序号需要手动
4. 一定要将字段放进去,否则排序将不起作用
```
http://localhost:8000/organization/course-org/?click_nums=&fav_nums=&city=3&search=%E5%8C%97%E4%BA%AC
```


### 不明白的地方
fav_id 13 啥意思