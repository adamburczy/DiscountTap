from django.shortcuts import render
from django.shortcuts import redirect
from .forms import SearchForm
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def render_home(request):
    if request.method == 'POST':
        global item
        item = SearchForm(request.POST)
        if item.is_valid():
            item = item.cleaned_data['item']
            return redirect('products_scripts:search')
    else: 
        item = SearchForm()
        context ={
        'item':item,
        }
    return render(request, 'index.html', context)

def product_search(request):
    # turn off js (prevent pop-ups)
    options = Options()
    options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.javascript': 2})
    options.add_argument('headless')
    driver = webdriver.Chrome('chromedriver',options=options)
    # go to ceneo
    driver.get('https://www.ceneo.pl/')
    # search for products on ceneo
    search = driver.find_element_by_id('form-head-search-q')
    search.send_keys(item)
    search.send_keys(Keys.RETURN)
    # copy current url
    global current_url
    current_url = driver.current_url
    return render(request, 'index.html', {'current_url': current_url})


def product_click_and_redirect(request):
    # turn off js (prevent pop-ups)
    options = Options()
    options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.javascript': 2})
    options.add_argument('headless')
    driver = webdriver.Chrome('chromedriver',options=options)
    driver.get(current_url)
    driver.find_element_by_xpath('//a[@class="go-to-product js_conv js_clickHash js_seoUrl"]').click()
    driver.find_element_by_xpath('//div[contains(@class,"product-offer-2020__product__offer-details__name short-name")]').click()
    # get link for product
    link = driver.find_element_by_xpath("//div[@class='product-offer-2020__product__offer-details__name short-name']/a").get_attribute('href')
    return redirect(link)


def link1():
    productno = 1
    return productno

def link2():
    productno = 2
    return productno

def link3():
    productno = 3
    return productno

def link4():
    productno = 4
    return productno

def link5():
    productno = 5
    return productno

def choose_productno(request):
    return render(request, 'index.html')




    
