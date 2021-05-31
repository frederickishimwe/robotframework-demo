
*** Variable ***
${ENV}=         staging
${URL}=        https://www.amazon.com
${BROWSER}=     chrome
${DELAY}=       2s
@{CHROME_OPTIONS}     --headless  --start-maximized   --disable-gpu   --no-sandbox --window-size\=1366,768    --remote-debugging-port=9222
#https://www.theverge.com/   chrome

*** Settings ***
Library         SeleniumLibrary
Library         dog_test_api.py
Library         dog_test_api.DogCommandQueryHost   ${ENV}       WITH NAME  dog_api


*** Keywords ***
Open Browser To Amazon
    Log To Console  \n testing 1 2 and 3 \n
    chrome_browser
    # headless_browser
    Capture Page Screenshot     
   

chrome_browser
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    # Set Selenium Speed    ${DELAY}


headless_browser  
    ${options}=    Set Chrome Options
    Create WebDriver    Chrome    crm_alias     chrome_options=${options} 


    # Open Browser     https://www.theverge.com/      headlesschrome      #desired_capabilities=${option}
    
    Go To       https://www.theverge.com/

    Capture Page Screenshot     
    Title Should Be     'The Verge'  

Set Chrome Options
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver
    : FOR    ${option}    IN    @{CHROME_OPTIONS}
    \    Call Method    ${options}    add_argument    ${option}
    [Return]    ${options}


Amazon Page Should Be Open
    Title Should Be    Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more
    Capture Page Screenshot     

Validate Response with description
    [Arguments]     ${response}     ${description}
    Run keyword if  ${response.status_code}==${200}    Log   ${response.json()}
    ${status}=  Run keyword and return status   Should be equal as strings  ${response.json()['status']}  Success   
    Run keyword if  ${status}==${FALSE}  Run keyword And Continue On Failure    Log   Fail:${description}      WARN  
    Run keyword if  ${status}==${FALSE}  Run keyword And Continue On Failure    FAIL   ${description}  



Ensure that 4 retrievers returned
    [Arguments]     ${response}
    Run keyword and continue on failure     Should be True  ${response.json()['message']['retriever'].__len__()}>=${4}   msg=4 golden retrievers Not Found

*** Test Cases ***

Open Amazon & Careers
    [Tags]   Ui     api
    Open Browser To Amazon
The title is now
    [Tags]   Ui     api
    Log Title
Inspect that you on the right page
    [Tags]   Ui     api
    Amazon Page Should Be Open

Check the careers page
    [Tags]   Ui     api

    Go To       https://www.amazon.jobs/
    Location Should Be      https://www.amazon.jobs/en/

ApiTest: Get Dog Breed List
    [Tags]   Ui     api
    ${results}=     dog_api.get_dog_breedlist
    Validate Response with description  ${results}   Get Dog Breeding List Failed
    Log   ${results.json()}
    Ensure that 4 retrievers returned   ${results} 



End Test
    [Tags]   Ui   
    Close Browser
