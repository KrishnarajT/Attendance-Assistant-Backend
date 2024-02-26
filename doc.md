---
title: FastAPI v0.1.0
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
highlight_theme: darkula
headingLevel: 2

---

<!-- Generator: Widdershins v4.0.1 -->

<h1 id="fastapi">FastAPI v0.1.0</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

<h1 id="fastapi-upload-images-or-attendance-info-from-app-website-pi">Upload Images or Attendance Info from App/Website/Pi</h1>

## add_student_face_from_url_upload_add_student_face_from_url_post

<a id="opIdadd_student_face_from_url_upload_add_student_face_from_url_post"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /upload/add_student_face_from_url?student_id=0&face_image_url=string \
  -H 'Accept: application/json'

```

```http
POST /upload/add_student_face_from_url?student_id=0&face_image_url=string HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/upload/add_student_face_from_url?student_id=0&face_image_url=string',
{
  method: 'POST',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.post '/upload/add_student_face_from_url',
  params: {
  'student_id' => 'integer',
'face_image_url' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.post('/upload/add_student_face_from_url', params={
  'student_id': '0',  'face_image_url': 'string'
}, headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/upload/add_student_face_from_url', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/upload/add_student_face_from_url?student_id=0&face_image_url=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/upload/add_student_face_from_url", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /upload/add_student_face_from_url`

*Add Student Face From Url*

Adds a face to the student's row in the student collection in the database. This is going to be one of the base faces of the student, from which the model trains.

:return: URL of the uploaded image.

<h3 id="add_student_face_from_url_upload_add_student_face_from_url_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|student_id|query|integer|true|none|
|face_image_url|query|string|true|none|

> Example responses

> 200 Response

```json
{
  "student_id": "string",
  "face_image_url": "string"
}
```

<h3 id="add_student_face_from_url_upload_add_student_face_from_url_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[AddFaceResponseModel](#schemaaddfaceresponsemodel)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

## add_student_face_upload_add_student_face_post

<a id="opIdadd_student_face_upload_add_student_face_post"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /upload/add_student_face?student_id=0 \
  -H 'Content-Type: multipart/form-data' \
  -H 'Accept: application/json'

```

```http
POST /upload/add_student_face?student_id=0 HTTP/1.1

Content-Type: multipart/form-data
Accept: application/json

```

```javascript
const inputBody = '{
  "face_image": "string"
}';
const headers = {
  'Content-Type':'multipart/form-data',
  'Accept':'application/json'
};

fetch('/upload/add_student_face?student_id=0',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'multipart/form-data',
  'Accept' => 'application/json'
}

result = RestClient.post '/upload/add_student_face',
  params: {
  'student_id' => 'integer'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'multipart/form-data',
  'Accept': 'application/json'
}

r = requests.post('/upload/add_student_face', params={
  'student_id': '0'
}, headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'multipart/form-data',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/upload/add_student_face', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/upload/add_student_face?student_id=0");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"multipart/form-data"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/upload/add_student_face", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /upload/add_student_face`

*Add Student Face*

Uploads face image to firebase. This is going to be one of the base faces of the student, from which the model trains.
:return: URL of the uploaded image.

> Body parameter

```yaml
face_image: string

```

<h3 id="add_student_face_upload_add_student_face_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|student_id|query|integer|true|none|
|body|body|[Body_add_student_face_upload_add_student_face_post](#schemabody_add_student_face_upload_add_student_face_post)|true|none|

> Example responses

> 200 Response

```json
{
  "student_id": "string",
  "face_image_url": "string"
}
```

<h3 id="add_student_face_upload_add_student_face_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[AddFaceResponseModel](#schemaaddfaceresponsemodel)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

## add_class_photo_from_url_upload_add_class_photo_from_url_post

<a id="opIdadd_class_photo_from_url_upload_add_class_photo_from_url_post"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /upload/add_class_photo_from_url?room_id=string&date=string&time=string&class_photo_url=string \
  -H 'Accept: application/json'

```

```http
POST /upload/add_class_photo_from_url?room_id=string&date=string&time=string&class_photo_url=string HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/upload/add_class_photo_from_url?room_id=string&date=string&time=string&class_photo_url=string',
{
  method: 'POST',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.post '/upload/add_class_photo_from_url',
  params: {
  'room_id' => 'string',
'date' => 'string',
'time' => 'string',
'class_photo_url' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.post('/upload/add_class_photo_from_url', params={
  'room_id': 'string',  'date': 'string',  'time': 'string',  'class_photo_url': 'string'
}, headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/upload/add_class_photo_from_url', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/upload/add_class_photo_from_url?room_id=string&date=string&time=string&class_photo_url=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/upload/add_class_photo_from_url", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /upload/add_class_photo_from_url`

*Add Class Photo From Url*

Adds class photo to firebase. This is ideally from PI. Non ideally from teachers phone. 
:return: URL of the uploaded image.

<h3 id="add_class_photo_from_url_upload_add_class_photo_from_url_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|room_id|query|string|true|none|
|date|query|string|true|none|
|time|query|string|true|none|
|class_photo_url|query|string|true|none|

> Example responses

> 200 Response

```json
{
  "room_id": "string",
  "date": "2019-08-24",
  "time": "14:15:22Z",
  "class_photo_url": "string"
}
```

<h3 id="add_class_photo_from_url_upload_add_class_photo_from_url_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[AddClassPhotoResponseModel](#schemaaddclassphotoresponsemodel)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

## add_class_photo_upload_add_class_photo_post

<a id="opIdadd_class_photo_upload_add_class_photo_post"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /upload/add_class_photo?room_id=string&date=string&time=string \
  -H 'Content-Type: multipart/form-data' \
  -H 'Accept: application/json'

```

```http
POST /upload/add_class_photo?room_id=string&date=string&time=string HTTP/1.1

Content-Type: multipart/form-data
Accept: application/json

```

```javascript
const inputBody = '{
  "class_photo": "string"
}';
const headers = {
  'Content-Type':'multipart/form-data',
  'Accept':'application/json'
};

fetch('/upload/add_class_photo?room_id=string&date=string&time=string',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'multipart/form-data',
  'Accept' => 'application/json'
}

result = RestClient.post '/upload/add_class_photo',
  params: {
  'room_id' => 'string',
'date' => 'string',
'time' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'multipart/form-data',
  'Accept': 'application/json'
}

r = requests.post('/upload/add_class_photo', params={
  'room_id': 'string',  'date': 'string',  'time': 'string'
}, headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'multipart/form-data',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/upload/add_class_photo', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/upload/add_class_photo?room_id=string&date=string&time=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"multipart/form-data"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/upload/add_class_photo", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /upload/add_class_photo`

*Add Class Photo*

Adds class photo to firebase. This is ideally from PI. Non ideally from teachers phone.
:return: URL of the uploaded image.

> Body parameter

```yaml
class_photo: string

```

<h3 id="add_class_photo_upload_add_class_photo_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|room_id|query|string|true|none|
|date|query|string|true|none|
|time|query|string|true|none|
|body|body|[Body_add_class_photo_upload_add_class_photo_post](#schemabody_add_class_photo_upload_add_class_photo_post)|true|none|

> Example responses

> 200 Response

```json
{
  "room_id": "string",
  "date": "2019-08-24",
  "time": "14:15:22Z",
  "class_photo_url": "string"
}
```

<h3 id="add_class_photo_upload_add_class_photo_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[AddClassPhotoResponseModel](#schemaaddclassphotoresponsemodel)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

## add_attendance_upload_add_attendance_post

<a id="opIdadd_attendance_upload_add_attendance_post"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /upload/add_attendance \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /upload/add_attendance HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "room_id": "string",
  "subject_id": "string",
  "teacher_id": "string",
  "panel_id": "string",
  "start_time": "2019-08-24T14:15:22Z",
  "end_time": "2019-08-24T14:15:22Z"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/upload/add_attendance',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/upload/add_attendance',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/upload/add_attendance', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/upload/add_attendance', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/upload/add_attendance");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/upload/add_attendance", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /upload/add_attendance`

*Add Attendance*

Adds attendance to the database. This is information from the teachers' app from the teacher.
:param attModel: Attendance model that contains all the necessary information
:return: URL of the uploaded image.

> Body parameter

```json
{
  "room_id": "string",
  "subject_id": "string",
  "teacher_id": "string",
  "panel_id": "string",
  "start_time": "2019-08-24T14:15:22Z",
  "end_time": "2019-08-24T14:15:22Z"
}
```

<h3 id="add_attendance_upload_add_attendance_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[AttendanceModel](#schemaattendancemodel)|true|none|

> Example responses

> 200 Response

```json
{
  "room_id": "string",
  "subject_id": "string",
  "teacher_id": "string",
  "panel_id": "string",
  "start_time": "2019-08-24T14:15:22Z",
  "end_time": "2019-08-24T14:15:22Z"
}
```

<h3 id="add_attendance_upload_add_attendance_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[AttendanceModel](#schemaattendancemodel)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

## add_face_encoding_upload_add_face_encoding_post

<a id="opIdadd_face_encoding_upload_add_face_encoding_post"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /upload/add_face_encoding?student_id=string&number_of_faces=0 \
  -H 'Content-Type: multipart/form-data' \
  -H 'Accept: application/json'

```

```http
POST /upload/add_face_encoding?student_id=string&number_of_faces=0 HTTP/1.1

Content-Type: multipart/form-data
Accept: application/json

```

```javascript
const inputBody = '{
  "face_encoding": "string"
}';
const headers = {
  'Content-Type':'multipart/form-data',
  'Accept':'application/json'
};

fetch('/upload/add_face_encoding?student_id=string&number_of_faces=0',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'multipart/form-data',
  'Accept' => 'application/json'
}

result = RestClient.post '/upload/add_face_encoding',
  params: {
  'student_id' => 'string',
'number_of_faces' => 'integer'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'multipart/form-data',
  'Accept': 'application/json'
}

r = requests.post('/upload/add_face_encoding', params={
  'student_id': 'string',  'number_of_faces': '0'
}, headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'multipart/form-data',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/upload/add_face_encoding', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/upload/add_face_encoding?student_id=string&number_of_faces=0");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"multipart/form-data"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/upload/add_face_encoding", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /upload/add_face_encoding`

*Add Face Encoding*

Adds face encoding to the database. This is done from the server, but a function is written here nonetheless to atomise the process. They are pickle files. 
:param face_encoding_model: Face encoding model that contains all the necessary information
:return: URL of the uploaded image.

> Body parameter

```yaml
face_encoding: string

```

<h3 id="add_face_encoding_upload_add_face_encoding_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|student_id|query|string|true|none|
|number_of_faces|query|integer|true|none|
|body|body|[Body_add_face_encoding_upload_add_face_encoding_post](#schemabody_add_face_encoding_upload_add_face_encoding_post)|true|none|

> Example responses

> 200 Response

```json
{
  "student_id": "string",
  "number_of_faces": 0,
  "encoding": "string"
}
```

<h3 id="add_face_encoding_upload_add_face_encoding_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[FaceEncodingModel](#schemafaceencodingmodel)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

## update_face_encoding_upload_update_face_encoding_post

<a id="opIdupdate_face_encoding_upload_update_face_encoding_post"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /upload/update_face_encoding?old_encoding_url=string&student_id=string&number_of_faces=0 \
  -H 'Content-Type: multipart/form-data' \
  -H 'Accept: application/json'

```

```http
POST /upload/update_face_encoding?old_encoding_url=string&student_id=string&number_of_faces=0 HTTP/1.1

Content-Type: multipart/form-data
Accept: application/json

```

```javascript
const inputBody = '{
  "face_encoding": "string"
}';
const headers = {
  'Content-Type':'multipart/form-data',
  'Accept':'application/json'
};

fetch('/upload/update_face_encoding?old_encoding_url=string&student_id=string&number_of_faces=0',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'multipart/form-data',
  'Accept' => 'application/json'
}

result = RestClient.post '/upload/update_face_encoding',
  params: {
  'old_encoding_url' => 'string',
'student_id' => 'string',
'number_of_faces' => 'integer'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'multipart/form-data',
  'Accept': 'application/json'
}

r = requests.post('/upload/update_face_encoding', params={
  'old_encoding_url': 'string',  'student_id': 'string',  'number_of_faces': '0'
}, headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'multipart/form-data',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/upload/update_face_encoding', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/upload/update_face_encoding?old_encoding_url=string&student_id=string&number_of_faces=0");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"multipart/form-data"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/upload/update_face_encoding", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /upload/update_face_encoding`

*Update Face Encoding*

Updates face encoding in the database. This should also be done from the server, but we cant overwrite or update files in firebase or s3, so we delete the previous file, and we upload the new file, also changing the url in the database, specifically in the student collection. 
:param face_encoding_model: Face encoding model that contains all the necessary information
:return: URL of the uploaded image.

> Body parameter

```yaml
face_encoding: string

```

<h3 id="update_face_encoding_upload_update_face_encoding_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|old_encoding_url|query|string|true|none|
|student_id|query|string|true|none|
|number_of_faces|query|integer|true|none|
|body|body|[Body_update_face_encoding_upload_update_face_encoding_post](#schemabody_update_face_encoding_upload_update_face_encoding_post)|true|none|

> Example responses

> 200 Response

```json
{
  "student_id": "string",
  "number_of_faces": 0,
  "encoding_url": "string"
}
```

<h3 id="update_face_encoding_upload_update_face_encoding_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[FaceEncodingResponseModel](#schemafaceencodingresponsemodel)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="fastapi-students">Students</h1>

## index_student_test_get

<a id="opIdindex_student_test_get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /student/test \
  -H 'Accept: application/json'

```

```http
GET /student/test HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/student/test',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/student/test',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/student/test', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/student/test', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/student/test");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/student/test", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /student/test`

*Test route*

> Example responses

> 200 Response

```json
null
```

<h3 id="index_student_test_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="index_student_test_get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## add_student_student_add_student_post

<a id="opIdadd_student_student_add_student_post"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /student/add_student \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /student/add_student HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "name": "string",
  "prn": "string",
  "panel": "string",
  "email": "string",
  "face_encoding_id": "string",
  "panel_roll_number": 0,
  "faces": [
    null
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/student/add_student',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/student/add_student',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/student/add_student', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/student/add_student', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/student/add_student");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/student/add_student", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /student/add_student`

*Add a student*

> Body parameter

```json
{
  "name": "string",
  "prn": "string",
  "panel": "string",
  "email": "string",
  "face_encoding_id": "string",
  "panel_roll_number": 0,
  "faces": [
    null
  ]
}
```

<h3 id="add_student_student_add_student_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[StudentModel](#schemastudentmodel)|true|none|

> Example responses

> 200 Response

```json
{
  "id": "string",
  "name": "string",
  "prn": "string",
  "panel": "string",
  "panel_roll_number": 0
}
```

<h3 id="add_student_student_add_student_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[StudentResponseModel](#schemastudentresponsemodel)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="fastapi-face-recognition">Face Recognition</h1>

## index_face_rec_test_get

<a id="opIdindex_face_rec_test_get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /face_rec/test \
  -H 'Accept: application/json'

```

```http
GET /face_rec/test HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/face_rec/test',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/face_rec/test',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/face_rec/test', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/face_rec/test', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/face_rec/test");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/face_rec/test", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /face_rec/test`

*Test route*

> Example responses

> 200 Response

```json
null
```

<h3 id="index_face_rec_test_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="index_face_rec_test_get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="fastapi-panels-schools-and-specializations">Panels, Schools and Specializations</h1>

## index_panels_test_get

<a id="opIdindex_panels_test_get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /panels/test \
  -H 'Accept: application/json'

```

```http
GET /panels/test HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/panels/test',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/panels/test',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/panels/test', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/panels/test', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/panels/test");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/panels/test", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /panels/test`

*Test route*

> Example responses

> 200 Response

```json
null
```

<h3 id="index_panels_test_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="index_panels_test_get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="fastapi-rooms-and-buildings">Rooms and Buildings</h1>

## index_college_test_get

<a id="opIdindex_college_test_get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /college/test \
  -H 'Accept: application/json'

```

```http
GET /college/test HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/college/test',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/college/test',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/college/test', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/college/test', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/college/test");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/college/test", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /college/test`

*Test route*

> Example responses

> 200 Response

```json
null
```

<h3 id="index_college_test_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="index_college_test_get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="fastapi-subjects-and-semesters">Subjects and Semesters</h1>

## index_subjects_test_get

<a id="opIdindex_subjects_test_get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /subjects/test \
  -H 'Accept: application/json'

```

```http
GET /subjects/test HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/subjects/test',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/subjects/test',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/subjects/test', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/subjects/test', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/subjects/test");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/subjects/test", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /subjects/test`

*Test route*

> Example responses

> 200 Response

```json
null
```

<h3 id="index_subjects_test_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="index_subjects_test_get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="fastapi-teachers">Teachers</h1>

## index_teachers_test_get

<a id="opIdindex_teachers_test_get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /teachers/test \
  -H 'Accept: application/json'

```

```http
GET /teachers/test HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/teachers/test',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/teachers/test',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/teachers/test', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/teachers/test', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/teachers/test");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/teachers/test", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /teachers/test`

*Test route*

> Example responses

> 200 Response

```json
null
```

<h3 id="index_teachers_test_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="index_teachers_test_get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="fastapi-classes-and-class-images">Classes and Class Images</h1>

## index_classes_test_get

<a id="opIdindex_classes_test_get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /classes/test \
  -H 'Accept: application/json'

```

```http
GET /classes/test HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/classes/test',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/classes/test',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/classes/test', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/classes/test', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/classes/test");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/classes/test", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /classes/test`

*Test route*

> Example responses

> 200 Response

```json
null
```

<h3 id="index_classes_test_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="index_classes_test_get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="fastapi-test">test</h1>

## index_test_get

<a id="opIdindex_test_get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /test \
  -H 'Accept: application/json'

```

```http
GET /test HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/test',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/test',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/test', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/test', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/test");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/test", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /test`

*Test route*

> Example responses

> 200 Response

```json
null
```

<h3 id="index_test_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="index_test_get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

# Schemas

<h2 id="tocS_AddClassPhotoResponseModel">AddClassPhotoResponseModel</h2>
<!-- backwards compatibility -->
<a id="schemaaddclassphotoresponsemodel"></a>
<a id="schema_AddClassPhotoResponseModel"></a>
<a id="tocSaddclassphotoresponsemodel"></a>
<a id="tocsaddclassphotoresponsemodel"></a>

```json
{
  "room_id": "string",
  "date": "2019-08-24",
  "time": "14:15:22Z",
  "class_photo_url": "string"
}

```

AddClassPhotoResponseModel

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|room_id|string|true|none|none|
|date|string(date)|true|none|none|
|time|string(time)|true|none|none|
|class_photo_url|string|true|none|none|

<h2 id="tocS_AddFaceResponseModel">AddFaceResponseModel</h2>
<!-- backwards compatibility -->
<a id="schemaaddfaceresponsemodel"></a>
<a id="schema_AddFaceResponseModel"></a>
<a id="tocSaddfaceresponsemodel"></a>
<a id="tocsaddfaceresponsemodel"></a>

```json
{
  "student_id": "string",
  "face_image_url": "string"
}

```

AddFaceResponseModel

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|student_id|string|true|none|none|
|face_image_url|string|true|none|none|

<h2 id="tocS_AttendanceModel">AttendanceModel</h2>
<!-- backwards compatibility -->
<a id="schemaattendancemodel"></a>
<a id="schema_AttendanceModel"></a>
<a id="tocSattendancemodel"></a>
<a id="tocsattendancemodel"></a>

```json
{
  "room_id": "string",
  "subject_id": "string",
  "teacher_id": "string",
  "panel_id": "string",
  "start_time": "2019-08-24T14:15:22Z",
  "end_time": "2019-08-24T14:15:22Z"
}

```

AttendanceModel

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|room_id|string|true|none|none|
|subject_id|string|true|none|none|
|teacher_id|string|true|none|none|
|panel_id|string|true|none|none|
|start_time|string(date-time)|true|none|none|
|end_time|string(date-time)|true|none|none|

<h2 id="tocS_Body_add_class_photo_upload_add_class_photo_post">Body_add_class_photo_upload_add_class_photo_post</h2>
<!-- backwards compatibility -->
<a id="schemabody_add_class_photo_upload_add_class_photo_post"></a>
<a id="schema_Body_add_class_photo_upload_add_class_photo_post"></a>
<a id="tocSbody_add_class_photo_upload_add_class_photo_post"></a>
<a id="tocsbody_add_class_photo_upload_add_class_photo_post"></a>

```json
{
  "class_photo": "string"
}

```

Body_add_class_photo_upload_add_class_photo_post

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|class_photo|string(binary)|true|none|none|

<h2 id="tocS_Body_add_face_encoding_upload_add_face_encoding_post">Body_add_face_encoding_upload_add_face_encoding_post</h2>
<!-- backwards compatibility -->
<a id="schemabody_add_face_encoding_upload_add_face_encoding_post"></a>
<a id="schema_Body_add_face_encoding_upload_add_face_encoding_post"></a>
<a id="tocSbody_add_face_encoding_upload_add_face_encoding_post"></a>
<a id="tocsbody_add_face_encoding_upload_add_face_encoding_post"></a>

```json
{
  "face_encoding": "string"
}

```

Body_add_face_encoding_upload_add_face_encoding_post

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|face_encoding|string(binary)|true|none|none|

<h2 id="tocS_Body_add_student_face_upload_add_student_face_post">Body_add_student_face_upload_add_student_face_post</h2>
<!-- backwards compatibility -->
<a id="schemabody_add_student_face_upload_add_student_face_post"></a>
<a id="schema_Body_add_student_face_upload_add_student_face_post"></a>
<a id="tocSbody_add_student_face_upload_add_student_face_post"></a>
<a id="tocsbody_add_student_face_upload_add_student_face_post"></a>

```json
{
  "face_image": "string"
}

```

Body_add_student_face_upload_add_student_face_post

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|face_image|string(binary)|true|none|none|

<h2 id="tocS_Body_update_face_encoding_upload_update_face_encoding_post">Body_update_face_encoding_upload_update_face_encoding_post</h2>
<!-- backwards compatibility -->
<a id="schemabody_update_face_encoding_upload_update_face_encoding_post"></a>
<a id="schema_Body_update_face_encoding_upload_update_face_encoding_post"></a>
<a id="tocSbody_update_face_encoding_upload_update_face_encoding_post"></a>
<a id="tocsbody_update_face_encoding_upload_update_face_encoding_post"></a>

```json
{
  "face_encoding": "string"
}

```

Body_update_face_encoding_upload_update_face_encoding_post

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|face_encoding|string(binary)|true|none|none|

<h2 id="tocS_FaceEncodingModel">FaceEncodingModel</h2>
<!-- backwards compatibility -->
<a id="schemafaceencodingmodel"></a>
<a id="schema_FaceEncodingModel"></a>
<a id="tocSfaceencodingmodel"></a>
<a id="tocsfaceencodingmodel"></a>

```json
{
  "student_id": "string",
  "number_of_faces": 0,
  "encoding": "string"
}

```

FaceEncodingModel

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|student_id|string|true|none|none|
|number_of_faces|integer|true|none|none|
|encoding|string(binary)|true|none|none|

<h2 id="tocS_FaceEncodingResponseModel">FaceEncodingResponseModel</h2>
<!-- backwards compatibility -->
<a id="schemafaceencodingresponsemodel"></a>
<a id="schema_FaceEncodingResponseModel"></a>
<a id="tocSfaceencodingresponsemodel"></a>
<a id="tocsfaceencodingresponsemodel"></a>

```json
{
  "student_id": "string",
  "number_of_faces": 0,
  "encoding_url": "string"
}

```

FaceEncodingResponseModel

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|student_id|string|true|none|none|
|number_of_faces|integer|true|none|none|
|encoding_url|string|true|none|none|

<h2 id="tocS_HTTPValidationError">HTTPValidationError</h2>
<!-- backwards compatibility -->
<a id="schemahttpvalidationerror"></a>
<a id="schema_HTTPValidationError"></a>
<a id="tocShttpvalidationerror"></a>
<a id="tocshttpvalidationerror"></a>

```json
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}

```

HTTPValidationError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|detail|[[ValidationError](#schemavalidationerror)]|false|none|none|

<h2 id="tocS_StudentModel">StudentModel</h2>
<!-- backwards compatibility -->
<a id="schemastudentmodel"></a>
<a id="schema_StudentModel"></a>
<a id="tocSstudentmodel"></a>
<a id="tocsstudentmodel"></a>

```json
{
  "name": "string",
  "prn": "string",
  "panel": "string",
  "email": "string",
  "face_encoding_id": "string",
  "panel_roll_number": 0,
  "faces": [
    null
  ]
}

```

StudentModel

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|true|none|none|
|prn|string|true|none|none|
|panel|string|true|none|none|
|email|string|true|none|none|
|face_encoding_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|panel_roll_number|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|faces|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[any]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_StudentResponseModel">StudentResponseModel</h2>
<!-- backwards compatibility -->
<a id="schemastudentresponsemodel"></a>
<a id="schema_StudentResponseModel"></a>
<a id="tocSstudentresponsemodel"></a>
<a id="tocsstudentresponsemodel"></a>

```json
{
  "id": "string",
  "name": "string",
  "prn": "string",
  "panel": "string",
  "panel_roll_number": 0
}

```

StudentResponseModel

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|true|none|none|
|name|string|true|none|none|
|prn|string|true|none|none|
|panel|string|true|none|none|
|panel_roll_number|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_ValidationError">ValidationError</h2>
<!-- backwards compatibility -->
<a id="schemavalidationerror"></a>
<a id="schema_ValidationError"></a>
<a id="tocSvalidationerror"></a>
<a id="tocsvalidationerror"></a>

```json
{
  "loc": [
    "string"
  ],
  "msg": "string",
  "type": "string"
}

```

ValidationError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|loc|[anyOf]|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|msg|string|true|none|none|
|type|string|true|none|none|

