import webbrowser
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import login


#for chrome
browser = webdriver.Chrome(executable_path= login.path)

#PS5 link
#browser.get("https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149")

#working test link
browser.get("https://www.bestbuy.com/site/samsung-uj59-series-u32j590uqn-32-led-4k-uhd-freesync-monitor-displayport-hdmi-dark-gray-blue/6293716.p?skuId=6293716")

#Triggers to continue order
buyButton = False   #list of bools maybe?
goToCart = False
checkout = False
signIn= False
placeOrder = False

wait = WebDriverWait(browser, 10)
shortWait = WebDriverWait(browser, 2)


while not buyButton:

    try:    #Refreshes when button is gray'd
        browser.find_element_by_class_name("btn-disabled")
        print("Button is still grey")

        time.sleep(2)
        browser.refresh()

    except:     #clicks add to cart and continues
         wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary"))).click()
         print("BUTTON WAS CLICKED")
         buyButton = True
         goToCart = True

if goToCart:
    try:    #Clicks gotocart link
        browser.find_element_by_class_name("cart-link").click()
        print("Go to cart was Successful")
        checkout = True

    except Exception as e:
        print("Failed to go to cart")
        print(e)

if checkout:
    try:    #Clicks checkout when available
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-lg"))).click()
        # try: #Apply for creditcard popup sometimes appears, closes and reclicks checkout if it does
        #     browser.find_element_by_class_name("c-modal-close-icon").click()
        #     time.sleep(1)
        #     browser.find_element_by_class_name("btn-lg").click()
        # except:
        #     print("No Pop ups")
        print("Checkout was Successful")
        signIn = True

    except Exception as e:
        print("Failed at checkout")
        print(e)

if signIn:
    try:    #Fills in users email, password, and logs in
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='fld-e']"))).send_keys(login.email)
        browser.find_element_by_xpath("//*[@id='fld-p1']").send_keys(login.password)
        browser.find_element_by_xpath("/html/body/div[1]/div/section/main/div[2]/div[1]/div/div/div/div/form/div[3]/button").click()
        print("Sign in Successful")
        placeOrder = True

    except Exception as e:
        print("Failed at sign-in")
        print(e)

if placeOrder:
    try:
         try:   #Switches to shipping
            shortWait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='checkoutApp']/div[2]/div[1]/div[1]/main/div[2]/div[2]/div/div[1]/div/section/div/div[2]/div[2]/div/div/a"))).click()
         except:#if already on shipping, inputs ccv
            browser.find_element_by_id("credit-card-cvv").send_keys(login.ccv)
                #inputs ccv
         wait.until(EC.visibility_of_element_located((By.ID, "credit-card-cvv"))).send_keys(login.ccv)
         browser.find_element_by_class_name("btn-primary").click()
         print("ORDER PLACED")

    except Exception as e:
        print("Failed to place order")
        print(e)
