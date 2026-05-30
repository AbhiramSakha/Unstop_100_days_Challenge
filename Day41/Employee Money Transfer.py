def can_pay_salaries(company_money, employee_names, employee_salaries):
    result = []
    
    for salary in employee_salaries:
        if company_money >= salary:
            result.append(True)
            company_money -= salary
        else:
            result.append(False)
    
    return result

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    company_money = int(data[0])
    employee_count = int(data[1])
    employee_names = data[2].split()
    employee_salaries = list(map(int, data[3].split()))
    
    result = can_pay_salaries(company_money, employee_names, employee_salaries)
    
    print(' '.join(str(x).lower() for x in result))

if __name__ == "__main__":
    main()