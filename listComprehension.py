numbers = [1,2,3]
double_num = [x*2 for x in numbers]

friends = ["Sam", "Samantha", "Son", "joy"]
starts_s = [friend for friend in friends if friend.startswith("S")]

friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 28}
friend_ages["Rolf"] = 92

student_attendance = {"Rolf": 95, "Bob": 80, "Anne": 100}
for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

attendance_values = student_attendance.values()
print(attendance_values)
print(sum(attendance_values))
print(sum(attendance_values)/ len(attendance_values))


print(friend_ages )
print(starts_s)
print(double_num)