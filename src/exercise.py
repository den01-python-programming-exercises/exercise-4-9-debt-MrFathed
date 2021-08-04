from debt import Debt

def main():
    #write your code below this line
    mortgage = Debt(120000.0, 1.01)
    mortgage.print_balance()

    mortgage.wait_one_year()
    mortgage.print_balance()

    years = 0
    while years < 20:
        mortgage.wait_one_year()
        years += 1

    mortgage.print_balance()

if __name__ == '__main__':
    main()
