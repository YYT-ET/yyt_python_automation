*** Settings ***
Documentation  Suite description
Resource    ./keywords_1.robot
Resource    ./varibles.robot
#Library     ../class08_.py

#Test Setup       login kuaidi100 with superuser
#Test Teardown    close browser

*** Test Cases ***
case1
    login kuaidi100 with superuser
    ${count}    Get_check_count
    Check_number
    Get_CompanyName
case2
    ${count}    Get_check_count
    Goto_check_page
    Check_count_shouId be plus one  ${count}
    Check_company_should be right
