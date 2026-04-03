#robot a keyword driven testing framework
#where the programs are divided into sections
#settings- imports and packages
#Variable-variables will be declared here
#Test Cases-Test Scripts
#Keyword- User defined keywords
#
#Documentation - keyword used for description if under Settings then it would be description for whole file

*** Settings ***
Documentation  Opening of browsers
Library  SeleniumLibrary

#
#*** Variables *** 
##scaler Variables
#${url}  https://www.cricbuzz.com/
##LIST Variables
#@{bikes} ktm kawasaki honda pulsar
##dict variables
#&{cars} nissan=gtr honda=civic

*** Variables ***
${url}  https://www.cricbuzz.com/
@{bikes}  ktm  kawasaki  honda  pulsar
&{cars}  nissan=gtr  honda=civic


*** Test Cases ***
Open cricbuzz in edge
  Open Edge Browser

Opening Chrome Browser
    [Documentation]  Chrome browser navigating to https://www.cricbuzz.com/
    Open Browser  ${url}  chrome
    Maximize Browser Window

    Log  navigated to cricbuzz
    Log To Console  ${bikes}[1]
    Log To Console  ${cars.nissan}
    Sleep   3s

    Close Browser


Opening Chrome headless Browser
    [Documentation]  Chrome browser navigating to https://www.cricbuzz.com/
    [Tags]  smoke
    Open Browser  https://www.cricbuzz.com/  headlesschrome
    Maximize Browser Window

    Log  navigated to cricbuzz
    Log to Console  message
    Sleep   3s

    Close Browser

*** Keywords ***

Open Edge Browser
    [Documentation]  edge browser navigating to https://www.cricbuzz.com/
    [Tags]   edge
    Open Browser  ${url}  edge
    Maximize Browser Window

    Log  navigated to cricbuzz
    Log To Console  ${bikes}[1]
    Log To Console  ${cars.nissan}
    Sleep   3s

    Close Browser
