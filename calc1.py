def calculate_mortgage(principal, annual_rate, years):
    monthly_rate = annual_rate / 12 / 100
    months = years * 12
    payment = principal * (monthly_rate * (1 + monthly_rate)**months) / ((1 + monthly_rate)**months - 1)
    return round(payment, 2)

if __name__ == "__main__":
    principal = float(input("Enter loan amount: "))
    annual_rate = float(input("Enter annual interest rate (in %): "))
    years = int(input("Enter loan term (in years): "))
    print(f"Monthly payment: ${calculate_mortgage(principal, annual_rate, years)}")
