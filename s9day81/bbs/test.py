from bs4 import BeautifulSoup

s = '''
<div class="form">
    <a href="">sdfjlaksdjf</a>
</div>
'''

bs = BeautifulSoup(s, "html.parser")
print(bs.text)
