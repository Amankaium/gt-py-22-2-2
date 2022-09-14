import requests

response = requests.get("https://habr.com/ru/news/")

def function_find_title(txt):
    start_text = """class="tm-article-snippet__title-link"><span>"""
    start_i = txt.find(start_text) + len(start_text)
    end_i = txt.find("""</span></a></h2>""")
    print(txt[start_i:end_i])

txt = response.text
end_i = txt.find("""</span></a></h2>""")
function_find_title(txt)
txt_after = txt[end_i:]
function_find_title(txt_after)

