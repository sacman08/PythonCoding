import matplotlib.pyplot as plt
pie_slices = [45, 20, 20, 15]
pie_activities = ['Python', 'Java', 'C', 'PHP']

plt.pie(pie_slices, labels=pie_activities)
plt.show()
