*** Settings ***
Library         Selenium2Library
*** Variable ***
${URL}=        https://www.amazon.com
${BROWSER}=     chrome
${DELAY}=       2s
@{CHROME_OPTIONS}     --headless  --start-maximized   --disable-gpu   --no-sandbox --window-size\=1366,768    --remote-debugging-port=9222
#https://www.theverge.com/   chrome
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

*** Test Cases ***

Open Amazon & Careers
    Open Browser To Amazon
The title is now
    Log Title
Inspect that you on the right page
    Amazon Page Should Be Open

Check the careers page
    Go To       https://www.amazon.jobs/
    Location Should Be      https://www.amazon.jobs/en/
End Test
    Close Browser
