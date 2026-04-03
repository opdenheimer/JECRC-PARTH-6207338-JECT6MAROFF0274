*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/
*** Test Cases ***
Handling simple Alerts
    Open Browser    ${url}   chrome
    Maximize Browser Window
    Sleep    2s

    Scroll Element Into View    xpath=//button[@id='alertBtn']

    Click Button    xpath=//button[@id='alertBtn']
    Sleep
    Handle Alert

Handling Confirm Alerts
    Open Browser    ${url}   chrome
    Maximize Browser Window
    Sleep    2s

    Scroll Element Into View    xpath=//button[id="confirmBtn"]

    Click Button    xpath=//button[id="confirmBtn"]
    Sleep    2s

    Handle Alert    action=DISMISS

    Close Browser

Handling Prompt Alerts
    Open Browser    ${url}   chrome
    Maximize Browser Window
    Sleep    2s

    Scroll Element Into View    xpath=//button[@id="promptBtn"]

    Click Button    xpath=//button[@id="promptBtn"]
    Sleep    2s

    Input Text Into Alert  Harry Potter
    Page Should Contain    Hello Harry Potter! How are you today?
    
    ${text}  Get Text    id=demo
    Log To Console    ${text}

    Sleep    2s

    Close Browser

    Close Browser


