import os
import io
import base64
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from django.conf import settings
from django.shortcuts import render

def info_view(request):
    return render(request, 'info.html')

def visualize_data(request):
    graph = None 

    if request.method == "POST":
        var_type = request.POST.get("var_type")  # Lấy loại biến (category/numerical)
        cat_var = request.POST.get("cat_var")  # Lấy biến category nếu có
        num_var = request.POST.get("num_var")  # Lấy biến numerical nếu có
        
        selected_var = cat_var if var_type == "category" else num_var  # Xác định biến được chọn

        if selected_var:
            image_path = os.path.join(settings.STATIC_ROOT, "images", f"{selected_var}.jpg")

            if os.path.exists(image_path):
                with open(image_path, "rb") as image_file:
                    graph = base64.b64encode(image_file.read()).decode("utf-8")  # Chuyển đổi ảnh thành base64

    return render(request, 'info.html', {"graph": graph})
