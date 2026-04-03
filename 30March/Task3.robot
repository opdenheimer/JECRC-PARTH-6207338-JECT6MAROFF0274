*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}  https://www.amazon.in/

*** Test Cases ***
Handling Task
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep  2s

    Click Element  xpath=//a[@href="/electronics/b/?ie=UTF8&node=976419031&ref_=nav_cs_electronics"]
    Sleep  2s

    Click Element  xpath=//label[@for="apb-browse-refinements-checkbox_6"]//descendant::i[@class="a-icon a-icon-checkbox"]
    
    ${productname}  Get Text  //div[@class="s-main-slot s-result-list s-search-results sg-row"]//descendant::div[@data-index="6"]//h2
    Log To Console  ${productname}
    
    Click Element  xpath=//div[@class="s-main-slot s-result-list s-search-results sg-row"]//descendant::div[@data-index="6"]
    Sleep  3s
    
    Switch Window  NEW
    
    Page Should Contain  ${productname}
    
    ${disc_percentage}  Get Text  //div[@id="corePriceDisplay_desktop_feature_div"]//descendant::span[@class="a-size-large a-color-price savingPriceOverride aok-align-center reinventPriceSavingsPercentageMargin savingsPercentage apex-savings-percentage"]
    Log To Console  ${disc_percentage}
    
    ${actual_price}  Get Text  //div[@id="corePriceDisplay_desktop_feature_div"]//descendant::span[@class="a-price a-text-price apex-basisprice-value"]
    Log To Console  ${actual_price}
    
    ${disc_price}  Get Text  //div[@id="corePriceDisplay_desktop_feature_div"]//descendant::span[@class="a-price-whole"]
    Log To Console  ${disc_price}

    Scroll Element Into View  xpath=//input[@id="add-to-cart-button"]
    Click Element  xpath=//input[@id="add-to-cart-button"]
    Sleep  2s
    
    Click Element  xpath=//a[@href="/gp/cart/view.html?ref_=nav_cart"]
    Sleep  2s
    
    Page Should Contain  ${product_name}
    Sleep  2s

    Close Browser
    


