
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    data='''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MY WEBPAGE</title>
</head>
<body background="{% static 'sipadan_cover-1024x511.jpeg' %}"> <br>

    <h3 align="center">
        <br>
        <a href="https://www.wrcok.com/">....</a>
        <font face="lato" size="6"> WROCK </font>
        &nbsp;


        <font face="iange"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
            <a href="https://pyspiders.com/">HOME</a> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
            <a href="https://www.bing.com/images/search?view=detailV2&ccid=9r7PDFQX&id=5CA67A0C35986D4D604CDC84CDB796585FFB3730&thid=OIP.9r7PDFQX_rUP6BFo6XPdgQHaGn&med">IMAGES</a> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
            <a href="https://www.bing.com/videos/search?q=PYSPIDERS&FORM=HDRSC3">VIDEOS</a> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
            <a href="https://pyspiders.com/contact">CONTACT</a> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
            <a href="https://pyspiders.com/about">ABOUT</a>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
        </font>
    </h3>
    <br><br><br>

    <br><br><br>
    <br><br><br>
    <br><br><br>
    <br><br><br><br><br><br>
    <br><br><br><br><br><br>

    <h1 align="center">
       
        <font face="lato" size="6"> CLICK HERE TO JOIN PYSPIDERS</font>
        <br><a href="https://pyspiders.com/python-full-stock/course">click here</a>
</h1>

</body>
</html>
    '''
    return HttpResponse(data)
# Create your views here.
