### Thế nào là thẻ (tag) ?
Tag là một thành phần cơ bản của HTML.

Một tag thường có cấu trúc như sau:

 `<tagname>content</tagname>`
 
 ### Thế nào gọi là thuộc tính (Attribute) và thẻ con (Children)?
Một attribute cung cấp thông tin về một *khía cạnh* nào đó của tag. Ví dụ:
```
<p title="I'm a tooltip">
This is a paragraph.
</p>
```

Ở ví dụ trên, attribute `title` cung cấp thông tin về đề mục của thẻ `<p>`.

### Học về các thẻ sau, cho biết tác dụng và cách sử dụng chúng:

* `<a>`:
>Là một *hyperlink*, dùng để di chuyển từ trang web này sang trang khác. Attribute quan trọng của `<a>` chính là `href`, nó chỉ ra đích đến của *hyperlink*.

Ví dụ: `<a href="http://techkids.vn/">Visit Techkids</a>`

* `<img>`:
>Thành phần hình ảnh trên HTML. Attribute quan trọng của `<img>` là `src`, đường dẫn đến nguồn của ảnh.

Ví dụ: `<img src="http://i.imgur.com/g5ue3ep.jpg">`

* `<div>`:
>Dùng để phân vùng HTML, giống như *"chia để trị"*. Nhóm các tags với nhau trong một `<div>` và sử dụng CSS cho `<div>` đó.

Ví dụ:
```
<div>
	<span>This is a span</span><br>
	<span>Another one</span>
	<span>Third one. And this one doesnt break</span>
</div>
```

* `<br>`:
>Dùng để thêm một lần xuống dòng.

Ví dụ: `<span>This is a span</span><br><span>and it drops</span>`

* `<table>`:
>Một bảng trên HTML. Được sử dụng cùng với các tags `<tr>`, `<th>`, `<td>`.

Ví dụ:
```
<table>
	<tr>
		<th>Name</th>
		<th>Number</th>
	</tr>
	<tr>
		<td>John</td>
		<td>123</td>
	</tr>
</table>
```

* `<ul>`, `<li>`:
>Dùng để tạo một list không có thứ tự.

Ví dụ:
```
<ul>
    <li>One</li>
    <li>Two</li>
    <li>Three</li>
</ul>
```

### Viết 1 file html để demo cho những thẻ trên
<!DOCTYPE html>
<html>
<head>
	<title>"Testing HTML</title>
</head>
<body>
<a href="http://techkids.vn/">Visit Techkids</a>
<img src="http://i.imgur.com/g5ue3ep.jpg">

<a href="http://techkids.vn/"><img src="http://i.imgur.com/g5ue3ep.jpg"></a>

<div>
	<span>This is a span</span><br>
	<span>Another one</span>
	<span>Third one. And this one doesnt break</span>
</div>

<table>
	<tr>
		<th>Name</th>
		<th>Number</th>
	</tr>
	<tr>
		<td>John</td>
		<td>123</td>
	</tr>
</table>

<ul>
<li>One</li>
<li>Two</li>
<li>Three</li>
</ul>
</body>
</html>

### Tìm hiểu xem thế nào là margin và padding của một thẻ