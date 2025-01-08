
from django.shortcuts import render
from django.http import HttpResponse

def upload_picture_view(request):
    return render(request, 'api/upload_picture.html')  # Path to your HTML file



def home(request):
    url = request.build_absolute_uri()
    return HttpResponse(f"""
<body style="background-color:#e8ede6;">
<h1 style="text-align:center;margin-top:6vh;font-family:Sans-serif">
Home page
</h1>

<section style="text-align:center;margin-top:20vh;padding:25px">
<!-- it's admin button -->
<a href='{url}admin/'>
<button
style="color:#5566d9;background-color:#62b840;padding:15px;border-radius:5px;border:none;padding-left:30px;padding-right:30px;font-size:1.3rem;cursor:pointer;">
Admin page
</button>
</a>
<br/>
<br/>

<!-- it's users button -->
<a href='{url}api/v1/users/'>
<button
style="color:#5566d9;background-color:#62b840;padding:15px;border-radius:5px;border:none;padding-left:30px;padding-right:30px;font-size:1.3rem;cursor:pointer;">
Users list page
</button>
</a>
<br/>
<br/>

<!-- it's companie button -->
<a href='{url}api/v1/companies/'>
<button
style="color:#5566d9;background-color:#62b840;padding:15px;border-radius:5px;border:none;padding-left:30px;padding-right:30px;font-size:1.3rem;cursor:pointer;">
Companie list page
</button>
</a>
<br/>
<br/>

<!-- it's Company Member List button -->
<a href='{url}api/v1/company-targeted/'>
<button
style="color:#5566d9;background-color:#62b840;padding:15px;border-radius:5px;border:none;padding-left:30px;padding-right:30px;font-size:1.3rem;cursor:pointer;">
Company User List page
</button>
</a>
<br/>
<br/>

<!-- it's User Photo urls button -->
<a href='{url}api/v1/user-uploads/'>
<button
style="color:#5566d9;background-color:#62b840;padding:15px;border-radius:5px;border:none;padding-left:30px;padding-right:30px;font-size:1.3rem;cursor:pointer;">
User Img Upload page
</button>
</a>
<br/>
<br/>

<!-- it's Html upload file/img button -->
<a href='{url}upload/'>
<button
style="color:#5566d9;background-color:#62b840;padding:15px;border-radius:5px;border:none;padding-left:30px;padding-right:30px;font-size:1.3rem;cursor:pointer;">
Randome Img upload
</button>
</a>
</section>                        
</body>
 """)
