import os
import sys
import requests

def update_tool():
    print("جاري التحديث...")
    repo_url = "https://raw.githubusercontent.com/WASEEM2009a/ps/main/"
    files_to_update = [
        "main.py",
        "config.py",
        "logo.py",
        "core/__init__.py",
        "core/ua_generator.py",
        "core/password_manager.py",
        "core/proxy_manager.py",
        "methods/__init__.py",
        "methods/m1_graph.py",
        "methods/m2_bgraph.py",
        "methods/m3_api.py",
        "menu/__init__.py",
        "menu/main_menu.py"
    ]
    for file in files_to_update:
        try:
            response = requests.get(repo_url + file)
            if response.status_code == 200:
                os.makedirs(os.path.dirname(file), exist_ok=True)
                with open(file, 'w', encoding='utf-8') as f:
                    f.write(response.text)
                print(f"✓ تم تحديث {file}")
            else:
                print(f"✗ فشل تحميل {file}")
        except Exception as e:
            print(f"✗ خطأ في {file}: {e}")
    print("اكتمل التحديث!")
    print("شغّل الأداة: python main.py")

if __name__ == "__main__":
    update_tool()