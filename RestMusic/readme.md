### 定义搜索的时候
1. 对于连接song__name 这样查询
2. 排序一定是使用model中的字段song__label
3. 一定是确定了主要的排序方式,然后再去通过其他方式排序
4. 查询可以带多个参数http://example.com/api/users?ordering=username

### 分页

1. 定义一个通用的分页类,在需要的时候进行设置



