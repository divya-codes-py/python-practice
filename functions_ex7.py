def student_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

student_info(name="Divya", age=20, city="Bangalore")
