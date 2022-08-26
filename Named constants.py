# Named constants.
WAGE_BASE = 117000 # There is no social security benefits
                    # tax on income above this level.
SOCIAL_SECURITY_TAX_RATE = 0.062   # 6.2%
MEDICARE_TAX_RATE = 0.0145   # 1.45%
ADDITIONAL_MEDICARE_TAX_RATE = .009   # 0.9%

def main():
    ## Calculate FICA tax for a single employee.
    ytdEarnings, curEarnings, totalEarnings = obtainEarnings()
    socialSecurityBenTax = calculateBenTax(ytdEarnings, curEarnings,
                                           totalEarnings)
    calculateFICAtax(ytdEarnings, curEarnings, totalEarnings,
                     socialSecurityBenTax)

def obtainEarnings():
    str1 = "Enter total earnings for this year prior to current pay period: "
    ytdEarnings = eval(input(str1)) # year-to-date earnings
    curEarnings = eval(input("Enter earnings for the current pay period: "))
    totalEarnings = ytdEarnings + curEarnings
    return(ytdEarnings, curEarnings, totalEarnings)

def calculateBenTax(ytdEarnings, curEarnings, totalEarnings):
    ## Calculate the Social Security Benefits tax.
    socialSecurityBenTax = 0
    if totalEarnings <= WAGE_BASE:
        socialSecurityBenTax = SOCIAL_SECURITY_TAX_RATE * curEarnings
    elif ytdEarnings < WAGE_BASE:
        socialSecurityBenTax = SOCIAL_SECURITY_TAX_RATE * (WAGE_BASE - ytdEarnings)
    return socialSecurityBenTax

def calculateFICAtax(ytdEarnings, curEarnings, totalEarnings, socialSecurityBenTax):
    ## Calculate and display the FICA tax.
    medicareTax = MEDICARE_TAX_RATE * curEarnings
    if ytdEarnings >= 200000:
        medicareTax += ADDITIONAL_MEDICARE_TAX_RATE * curEarnings
    elif totalEarnings > 200000:
        medicareTax += ADDITIONAL_MEDICARE_TAX_RATE * (totalEarnings - 200000)
    ficaTax = socialSecurityBenTax + medicareTax
    print("FICA tax for the current pay period: ${0:,.2f}".format(ficaTax))

main()