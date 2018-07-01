*** Settings ***
Documentation   Suite description
Library  Selenium2Library

*** Test Cases ***
#case1
#    ${count}    get matching xpath count    xpath=
#    run keyword if  ${count}==1
#    ...     run keywords    input text      xpath=      88888
#    ...     AND     click element   xpath=
#    ...     ELSE    mouse over      xpath
#
#case2
#    :FOR  ${i} in RANGE  5
#    \   log  ${i}

case3
    @{list}     create list     10  11  12
    :FOR    ${i}    IN      @{list}
    \   run keyword if      ${i}%2==0   open  testweb
    \   ...     ELSE    log  jishu

*** keywords ***
open testweb
        open browser        http://www.kuaidi100.com/        chrome
