*** Settings ***
Documentation  Handling elements
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/
${prac}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Handling CheckBoxes
    [Documentation]  herokuapp Checkboxes
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    3s
    
    Click Element  xpath=//a[text()="Checkboxes"]
    #assert for checking the checkbox
    Page Should Contain Checkbox    xpath=(//input[@type='checkbox'])[1]
    Sleep    2s
    
    Select Checkbox  xpath=(//input[@type='checkbox'])[1]
    Sleep    2s
    Unselect Checkbox  xpath=(//input[@type='checkbox'])[2]
    Sleep    2s

Handling elements in automation
    [Documentation]    automation Elements
    Open Browser    ${prac}  chrome
    Maximize Browser Window
    Sleep    2s

    Page Should Contain Checkbox    xpath=//input[@id='monday']

    Select Checkbox  xpath=//input[@id='monday']
    Sleep  2s

    Select Checkbox  xpath=//input[@id='tuesday']
    Sleep    2s

    Click Element  xpath=//input[@id='female']
    Sleep  2s