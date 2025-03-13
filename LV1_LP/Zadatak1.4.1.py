

def total_euro(working_hours,salary_per_hour):
    return working_hours*salary_per_hour

working_hours=int(input("unesi broj radnih sati: "))
salary_per_hour=float(input("Unesi plaću po satu: "))

print(f"Radni sati: {working_hours}")
print(f"eura/h: {salary_per_hour}")
print(f"Ukupno: {total_euro(working_hours, salary_per_hour)} eura")
