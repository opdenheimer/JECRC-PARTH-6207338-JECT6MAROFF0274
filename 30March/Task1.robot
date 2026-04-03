*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/


*** Test Cases ***
Handling window
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    4s

    Scroll Element Into View    xpath=//button[@id='PopUp']
    Click Element  xpath=//button[@id='PopUp']
    Sleep    3s
    
    @{windows}  Get Window Handles
    @{title}  Get Window Titles
    
   Log To Console    @{title}
   
   Switch Window    @{windows}[0]

   Page Should Contain    Automation Testing Practice
   Sleep    2s
   Close Window